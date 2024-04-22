from wand.image import Image
import re
from collections import defaultdict 
import json

image_method_info = defaultdict(list)

all_types = []

PARAM_CONST_TYPE_MAP = dict(
    channel="CHANNELS",
    gravity=None,
    colorspace="COLORSPACE_TYPES",
    colorspace_type="COLORSPACE_TYPES",
    kernel="KERNEL_INFO_TYPES",
    function="FUNCTION_TYPES",
    noise_type="NOISE_TYPES",
    dither="DITHER_METHODS",
    filter="FILTER_TYPES",
    stat="STATISTIC_TYPES"
)

METHOD_CONST_TYPE_MAP = dict(
    clut="PIXEL_INTERPOLATE_METHODS",
    distort="DISTORTION_METHODS",
    implode="PIXEL_INTERPOLATE_METHODS",
    morphology="MORPHOLOGY_METHODS",
    remap="DISTORTION_METHODS",
    swirl="PIXEL_INTERPOLATE_METHODS",
    wave="PIXEL_INTERPOLATE_METHODS",
    auto_threshold="AUTO_THRESHOLD_METHODS",
    merge_layers="IMAGE_LAYER_METHOD"
)

blacklist = ["allocate", "cdl", "clear", "close", "deconstruct", "destroy", "strip", 'fft', 'ift', 'pseudo', 'raise_exception', 'optimize_layers', 'optimize_transparency', 'reset_coords', 'reset_sequence', 'image_get', 'image_remove', 'import_pixels', 'unique_colors', 'complex', 'image_swap', 'deskew']

with Image(filename='rose:') as img:
    method_list = [func for func in dir(img) if (func not in blacklist) and (not func.startswith("iterator")) and (not func.startswith('_')) and callable(getattr(img, func))]
    for method_name in method_list:
        method_doc = getattr(img, method_name).__doc__ 
        if not method_doc: continue
        method_doc = method_doc \
            .replace(":type: ", ":type ") \
            .replace(":params", ":param") \
            .replace(": `basestring`", ": :class:`basestring`") \
            .replace(":type file: file object", ":type file: :class:`file_object`") \
            .replace(":type tile: :class:`Image <wand.image.BaseImage>`", ":type tile: :class:`wand.image.BaseImage`") \
            .replace(":class:`collections.abc.Sequence`", ":class:`floats`")
            
        # Typo in composite, deskew, morphology, ping, posterize, spread, texture, trim
        params = [
            result.group(1)
            for result in list(re.finditer(r":param ([a-zA-Z_]+):", method_doc))
        ]
        types = [
            result.group(1).replace('~', '').replace('<', '').replace('>', '')
            for result in re.finditer(r":type [a-zA-Z_]+: :(?:const|class):`([~a-zA-Z._<>]+)`", method_doc)
        ]
        types = ["Image" if "Image" in type else type for type in types]

        if ":returns:" in method_doc: continue
        if "file_object" in types: continue
        elif ("wand.font.Font" in types) or ("wand.color.Color" in types) or ("wand.drawing.Drawing" in types) or ("Image" in types) or ("Color" in types) or ("abc.Mapping" in types): 
            continue #TODO: Support this
        if method_name == "spread": types.append("PIXEL_INTERPOLATE_METHODS")
        elif method_name == "trim": params.remove("background_color")
        
        #assert len(params) == len(types), print(method_doc, '\n\n', params, types, method_name)

        params = list(zip(params, types))
        for id in range(len(params)):
            param, old_type = params[id]
            new_type = PARAM_CONST_TYPE_MAP.get(param, old_type)
            if param == "operator": 
                if method_name == "evaluate": new_type = "EVALUATE_OPS" 
                else: new_type = f"{method_name.upper()}_OPERATORS"
            if param == "method": new_type = METHOD_CONST_TYPE_MAP.get(method_name, old_type)
            params[id] = (param, new_type)
            all_types.append(new_type)
        image_method_info[method_name] = params

all_types = list(set(all_types))
with open("wand_methods.json", 'w') as f:
    json.dump(image_method_info, f, indent=4)
print(all_types)