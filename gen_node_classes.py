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

        if param_type.isupper():
            input_type = list(getattr(wand.image, param_type))
            type_config = {"default": "rgb" if param_type == "CHANNELS" else input_type[0]}
        
        elif param_type == "float" or param_type == "numbers.Real":
            input_type = "FLOAT"
            if type(default_value).__name__ in ['type', 'NoneType']:
                default_value = 0
            type_config = {"default": default_value, "min": 0, "max": 100, "step": 0.01}

        elif param_type == "bool": 
            input_type = "BOOLEAN"
            if type(default_value).__name__ in ['type', 'NoneType']:
                default_value = False
            type_config = {"default": default_value}

        elif param_type == "numbers.Integral": 
            input_type = "INT"
            if type(default_value).__name__ in ['type', 'NoneType']:
                default_value = 0
            type_config = {"default": default_value, "min": 0, "max": 100}

        elif (param_type == "basestring") or (param_type == "floats"): 
            input_type = "STRING"
            type_config = {"multiline": False}
        assert input_type, param_type
        input_types[param] = (input_type, type_config)
    img.close()
    return {"required": input_types}

with open("wand_methods.json", 'r') as f:
    wand_methods_dict = json.load(f)

NODE_CLASS_TEMPLATE = \
"""
class {node_class_name}:
    @classmethod
    def INPUT_TYPES(s):
        return {comfy_input_types}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            with Image.from_array(image) as img_wand:
                getattr(img_wand, '{img_method}')(**kwargs)
                out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)
"""

with open("nodes.py", 'w') as f:
    f.write("import numpy as np\n")
    f.write("from wand.image import Image\n")
    f.write("import torch\n")
    f.write("from .utils import HWC3\n")
    for method_name, param_dict in wand_methods_dict.items():
        node_class_name = method_name[0].upper()+method_name[1:]
        node_class_str = NODE_CLASS_TEMPLATE.format(
            node_class_name=node_class_name,
            comfy_input_types=gen_comfy_input_types(method_name, param_dict),
            img_method=method_name
        )
        f.write(node_class_str + '\n')

    f.write("NODE_CLASS_MAPPINGS = {\n")
    for method_name in wand_methods_dict:
        node_class_name = method_name[0].upper()+method_name[1:]
        f.write(' ' * 4)
        f.write(f'"ImageMagick {node_class_name}": {node_class_name},')
        f.write('\n')
    f.write('}\n')