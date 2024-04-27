import json
import wand.image
import inspect

CCC_DEFAULT_VALUE = \
"""<ColorCorrectionCollection xmlns="urn:ASC:CDL:v1.2">
    <ColorCorrection id="cc03345">
        <SOPNode>
            <Slope> 0.9 1.2 0.5 </Slope>
            <Offset> 0.4 -0.5 0.6 </Offset>
            <Power> 1.0 0.8 1.5 </Power>
        </SOPNode>
        <SATNode>
            <Saturation> 0.85 </Saturation>
        </SATNode>
    </ColorCorrection>
</ColorCorrectionCollection>"""

MATRIX_DEFAULT_VALUE = \
"""[
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0],
]"""

def gen_comfy_input_types(method_name, param_items):
    img = wand.image.Image(filename='rose:')
    input_types = {"image": ("IMAGE",)}
    method_signature = inspect.signature(getattr(img, method_name)).parameters
    for param, param_type in param_items:
        input_type, type_config = None, None
        default_value = method_signature[param].default
        if not param_type: continue
        if param_type.isupper():
            input_type = list(getattr(wand.image, param_type))
            if (method_name == "normalize") and (param == "channel"):
                input_type = [value for value in input_type if "copy_" + value in wand.image.COMPOSITE_OPERATORS]
            if (method_name == "merge_layers") and (param == "method"):
                input_type = ['merge', 'flatten', 'mosaic', 'trimbounds']
            type_config = {"default": input_type[1]} # first method is usally "undefined"
        
        elif param_type == "float" or param_type == "numbers.Real":
            input_type, min = "FLOAT", 0.0
            if type(default_value).__name__ in ['type', 'NoneType']:
                default_value = 0
            if param in ['width', 'height', 'x_res', 'y_res']:
                default_value = 512
            type_config = {"default": default_value, "min": min, "max": 1024, "step": 0.01}

        elif param_type == "bool": 
            input_type = "BOOLEAN"
            if type(default_value).__name__ in ['type', 'NoneType']:
                default_value = False
            type_config = {"default": default_value}

        elif param_type == "numbers.Integral": 
            input_type, min = "INT", 0
            if type(default_value).__name__ in ['type', 'NoneType']:
                default_value = 0
            if param in ['width', 'height', 'x_res', 'y_res', 'columns', 'rows']:
                default_value = 512
                min = 1
            # make kmeans and quantize working
            if param == "number_colors":
                default_value = 16
                min = 1
            # https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.crop
            # height & width are kept as they are more useful
            # right & bottom can be converted to height and width using math nodes
            if method_name == 'crop' and param in ['right', 'bottom']:
                continue 
                
            type_config = {"default": default_value, "min": min, "max": 1024}

        elif (param_type == "basestring") or (param_type == "floats"): 
            input_type, multiline = "STRING", False
            if type(default_value).__name__ in ['type', 'NoneType']:
                default_value = ''
            if param == "arguments": 
                if method_name == "distort":
                    default_value = "0, 0, 20, 60, 90, 0, 70, 63, 0, 90, 5, 83, 90, 90, 85, 88"
                else:
                    default_value = '0.5, 1.0'
            if param == "ccc":
                multiline = True
                default_value = CCC_DEFAULT_VALUE
            if param == "matrix":
                multiline = True
                default_value = MATRIX_DEFAULT_VALUE
            type_config = {"multiline": multiline, "default": default_value}
        assert input_type, param_type
        input_types[param] = (input_type, type_config)
    img.close()
    return {"required": input_types}

with open("wand_methods.json", 'r') as f:
    wand_methods_dict = json.load(f)
with open("method_category.json", 'r') as f:
    method_category_dict = json.load(f)
    method_category_dict_copy = {**method_category_dict}

NODE_CLASS_TEMPLATE = \
"""
class {node_class_name}:
    @classmethod
    def INPUT_TYPES(s):
        return {comfy_input_types}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.{img_method}.__doc__

    CATEGORY = "{category}"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, '{img_method}', kwargs, type='{apply_type}')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )
"""

apply_whole_methods = ['concat', 'smush', 'coalesce', 'combine', 'complex', 'merge_layers', 'polynomial']

with open("nodes.py", 'w') as f:
    f.write("import numpy as np\n")
    f.write("from wand.image import Image\n")
    f.write("import torch\n")
    f.write("from .utils import *\n")
    img_wand = wand.image.Image(filename='rose:')
    for method_name, param_dict in wand_methods_dict.items():
        node_class_name = ''.join([name_part[0].upper() + name_part[1:] for name_part in method_name.split('_')])
        node_class_str = NODE_CLASS_TEMPLATE.format(
            node_class_name=node_class_name,
            comfy_input_types=gen_comfy_input_types(method_name, param_dict),
            img_method=method_name,
            category=f"MagickWand/{method_category_dict[method_name]}" if method_name in method_category_dict else "MagickWand",
            apply_type="whole" if method_name in apply_whole_methods else "iterative"
        )
        del method_category_dict[method_name]
        f.write(node_class_str + '\n')
    f.write("NODE_CLASS_MAPPINGS = {\n")
    assert not method_category_dict, f"Redundant in method category: {method_category_dict}"
    method_name_node_id = {}
    for method_name in wand_methods_dict:
        node_id = ' '.join([name_part[0].upper() + name_part[1:] for name_part in method_name.split('_')])
        node_class_name = ''.join([name_part[0].upper() + name_part[1:] for name_part in method_name.split('_')])
        f.write(' ' * 4)
        f.write(f'"ImageMagick {node_id}": {node_class_name},')
        f.write('\n')
        method_name_node_id[method_name] = node_id
    f.write('}\n')

    print("Method name - Node ID")
    for method_name, node_id in method_name_node_id.items():
        print(method_name, ':', node_id.replace(' ', '') + "Image")
    print('\n' * 4)
    
    print("Markdown")
    category_markdown = {}
    for method_name, node_id in method_name_node_id.items():
        category = method_category_dict_copy[method_name]
        if category not in category_markdown:
            category_markdown[category] = ''
        category_markdown[category] += \
            f"* ImageMagick {node_id}: [{method_name}](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.{method_name}) \n"
    for category, markdown in category_markdown.items():
        print(f'### {category}')
        print(markdown)