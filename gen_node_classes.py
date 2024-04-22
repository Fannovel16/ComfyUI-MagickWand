import json
import wand.image
import inspect

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
            type_config = {"default": "rgb" if param_type == "CHANNELS" else input_type[1]} # first method is usally "undefined"
        
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
            if param in ['width', 'height', 'x_res', 'y_res']:
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
            input_type = "STRING"
            default_value = ''
            if param == "arguments": 
                if method_name == "distort":
                    default_value = "0, 0, 20, 60, 90, 0, 70, 63, 0, 90, 5, 83, 90, 90, 85, 88"
                else:
                    default_value = '0.5, 1.0'
            type_config = {"multiline": True}
        assert input_type, param_type
        input_types[param] = (input_type, type_config)
    img.close()
    return {"required": input_types}

with open("wand_methods.json", 'r') as f:
    wand_methods_dict = json.load(f)
with open("method_category.json", 'r') as f:
    method_category_dict = json.load(f)

NODE_CLASS_TEMPLATE = \
"""
class {node_class_name}:
    @classmethod
    def INPUT_TYPES(s):
        return {comfy_input_types}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, '{img_method}').__doc__

    CATEGORY = "{category}"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, '{img_method}', kwargs, type='{apply_type}')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )
"""

apply_whole_methods = ['concat', 'smush', 'coalesce', 'combine', 'complex', 'merge_layers', 'polynomial', 'quantize']

with open("nodes.py", 'w') as f:
    f.write("import numpy as np\n")
    f.write("from wand.image import Image\n")
    f.write("import torch\n")
    f.write("from .utils import *\n")
    img_wand = wand.image.Image(filename='rose:')
    for method_name, param_dict in wand_methods_dict.items():
        node_class_name = method_name[0].upper()+method_name[1:]
        node_class_str = NODE_CLASS_TEMPLATE.format(
            node_class_name=node_class_name,
            comfy_input_types=gen_comfy_input_types(method_name, param_dict),
            img_method=method_name,
            category=f"MagickWand/{method_category_dict[method_name]}" if method_name in method_category_dict else "MagickWand",
            apply_type="whole" if method_name in apply_whole_methods else "iterative"
        )
        f.write(node_class_str + '\n')

    f.write("NODE_CLASS_MAPPINGS = {\n")
    for method_name in wand_methods_dict:
        if method_name == "pseudo": continue
        node_class_name = method_name[0].upper()+method_name[1:]
        f.write(' ' * 4)
        f.write(f'"ImageMagick {node_class_name}": {node_class_name},')
        f.write('\n')
    f.write('}\n')