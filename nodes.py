import numpy as np
from wand.image import Image
import torch
from .utils import *

class AdaptiveBlur:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.adaptive_blur.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'adaptive_blur', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class AdaptiveResize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'columns': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'rows': ('INT', {'default': 512, 'min': 1, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.adaptive_resize.__doc__

    CATEGORY = "MagickWand/Resize"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'adaptive_resize', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class AdaptiveSharpen:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.adaptive_sharpen.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'adaptive_sharpen', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class AdaptiveThreshold:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'offset': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.adaptive_threshold.__doc__

    CATEGORY = "MagickWand/Thresold"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'adaptive_threshold', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class AutoGamma:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.auto_gamma.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'auto_gamma', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class AutoLevel:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.auto_level.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'auto_level', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class AutoOrient:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.auto_orient.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'auto_orient', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class AutoThreshold:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'method': (['undefined', 'kapur', 'otsu', 'triangle'], {'default': 'kapur'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.auto_threshold.__doc__

    CATEGORY = "MagickWand/Thresold"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'auto_threshold', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class BlueShift:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'factor': ('FLOAT', {'default': 1.5, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.blue_shift.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'blue_shift', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Blur:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.blur.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'blur', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class BrightnessContrast:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'brightness': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'contrast': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.brightness_contrast.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'brightness_contrast', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Canny:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'lower_percent': ('FLOAT', {'default': 0.1, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'upper_percent': ('FLOAT', {'default': 0.3, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.canny.__doc__

    CATEGORY = "MagickWand/Feature"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'canny', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Charcoal:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.charcoal.__doc__

    CATEGORY = "MagickWand/Feature"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'charcoal', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Chop:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'x': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'y': ('INT', {'default': 0, 'min': 0, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.chop.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'chop', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Clahe:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'number_bins': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'clip_limit': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.clahe.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'clahe', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Clamp:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.clamp.__doc__

    CATEGORY = "MagickWand/Quantize"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'clamp', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Coalesce:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.coalesce.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'coalesce', kwargs, type='whole')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class ColorDecisionList:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'ccc': ('STRING', {'multiline': True, 'default': '<ColorCorrectionCollection xmlns="urn:ASC:CDL:v1.2">\n    <ColorCorrection id="cc03345">\n        <SOPNode>\n            <Slope> 0.9 1.2 0.5 </Slope>\n            <Offset> 0.4 -0.5 0.6 </Offset>\n            <Power> 1.0 0.8 1.5 </Power>\n        </SOPNode>\n        <SATNode>\n            <Saturation> 0.85 </Saturation>\n        </SATNode>\n    </ColorCorrection>\n</ColorCorrectionCollection>'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.color_decision_list.__doc__

    CATEGORY = "MagickWand/Color Matrix & Decision List"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'color_decision_list', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class ColorMatrix:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'matrix': ('STRING', {'multiline': True, 'default': '[\n    [1.0, 0.0, 0.0],\n    [0.0, 1.0, 0.0],\n    [0.0, 0.0, 1.0],\n]'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.color_matrix.__doc__

    CATEGORY = "MagickWand/Color Matrix & Decision List"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'color_matrix', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Combine:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'}), 'colorspace': (['undefined', 'cmy', 'cmyk', 'gray', 'hcl', 'hclp', 'hsb', 'hsi', 'hsl', 'hsv', 'hwb', 'lab', 'lch', 'lchab', 'lchuv', 'log', 'lms', 'luv', 'ohta', 'rec601ycbcr', 'rec709ycbcr', 'rgb', 'scrgb', 'srgb', 'transparent', 'xyy', 'xyz', 'ycbcr', 'ycc', 'ydbdr', 'yiq', 'ypbpr', 'yuv'], {'default': 'cmy'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.combine.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'combine', kwargs, type='whole')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Concat:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'stacked': ('BOOLEAN', {'default': False})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.concat.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'concat', kwargs, type='whole')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Contrast:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'sharpen': ('BOOLEAN', {'default': True})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.contrast.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'contrast', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class ContrastStretch:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'black_point': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'white_point': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.contrast_stretch.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'contrast_stretch', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Crop:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'left': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'top': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'width': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'reset_coords': ('BOOLEAN', {'default': True})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.crop.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'crop', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class CycleColorMap:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'offset': ('INT', {'default': 1, 'min': 0, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.cycle_color_map.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'cycle_color_map', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Decipher:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'passphrase': ('STRING', {'multiline': False, 'default': ''})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.decipher.__doc__

    CATEGORY = "MagickWand/Cipher"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'decipher', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Despeckle:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.despeckle.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'despeckle', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Distort:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'method': (['undefined', 'affine', 'affine_projection', 'scale_rotate_translate', 'perspective', 'perspective_projection', 'bilinear_forward', 'bilinear_reverse', 'polynomial', 'arc', 'polar', 'depolar', 'cylinder_2_plane', 'plane_2_cylinder', 'barrel', 'barrel_inverse', 'shepards', 'resize', 'sentinel', 'rigidaffine'], {'default': 'affine'}), 'arguments': ('STRING', {'multiline': False, 'default': '0, 0, 20, 60, 90, 0, 70, 63, 0, 90, 5, 83, 90, 90, 85, 88'}), 'best_fit': ('BOOLEAN', {'default': False}), 'filter': (['undefined', 'point', 'box', 'triangle', 'hermite', 'hanning', 'hamming', 'blackman', 'gaussian', 'quadratic', 'cubic', 'catrom', 'mitchell', 'jinc', 'sinc', 'sincfast', 'kaiser', 'welsh', 'parzen', 'bohman', 'bartlett', 'lagrange', 'lanczos', 'lanczossharp', 'lanczos2', 'lanczos2sharp', 'robidoux', 'robidouxsharp', 'cosine', 'spline', 'sentinel'], {'default': 'point'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.distort.__doc__

    CATEGORY = "MagickWand/Morphology"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'distort', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Edge:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.edge.__doc__

    CATEGORY = "MagickWand/Feature"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'edge', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Emboss:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.emboss.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'emboss', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Encipher:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'passphrase': ('STRING', {'multiline': False, 'default': ''})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.encipher.__doc__

    CATEGORY = "MagickWand/Cipher"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'encipher', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Enhance:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.enhance.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'enhance', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Equalize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.equalize.__doc__

    CATEGORY = "MagickWand/Statistic"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'equalize', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Evaluate:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'operator': (['undefined', 'abs', 'add', 'addmodulus', 'and', 'cosine', 'divide', 'exponential', 'gaussiannoise', 'impulsenoise', 'laplaciannoise', 'leftshift', 'log', 'max', 'mean', 'median', 'min', 'multiplicativenoise', 'multiply', 'or', 'poissonnoise', 'pow', 'rightshift', 'rootmeansquare', 'set', 'sine', 'subtract', 'sum', 'thresholdblack', 'threshold', 'thresholdwhite', 'uniformnoise', 'xor', 'inverse_log'], {'default': 'abs'}), 'value': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.evaluate.__doc__

    CATEGORY = "MagickWand/Statistic"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'evaluate', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Extent:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'x': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'y': ('INT', {'default': 0, 'min': 0, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.extent.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'extent', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Flip:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.flip.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'flip', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Flop:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.flop.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'flop', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class ForwardFourierTransform:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'magnitude': ('BOOLEAN', {'default': True})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.forward_fourier_transform.__doc__

    CATEGORY = "MagickWand/Fourier"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'forward_fourier_transform', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Function:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'function': (['undefined', 'arcsin', 'arctan', 'polynomial', 'sinusoid'], {'default': 'arcsin'}), 'arguments': ('STRING', {'multiline': False, 'default': '0.5, 1.0'}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.function.__doc__

    CATEGORY = "MagickWand/Statistic"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'function', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Gamma:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'adjustment_value': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.gamma.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'gamma', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class GaussianBlur:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.gaussian_blur.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'gaussian_blur', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class HoughLines:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'threshold': ('INT', {'default': 40, 'min': 0, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.hough_lines.__doc__

    CATEGORY = "MagickWand/Feature"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'hough_lines', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Implode:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'amount': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'method': (['undefined', 'average', 'average9', 'average16', 'background', 'bilinear', 'blend', 'catrom', 'integer', 'mesh', 'nearest', 'spline'], {'default': 'average'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.implode.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'implode', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Kmeans:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'number_colors': ('INT', {'default': 16, 'min': 1, 'max': 1024}), 'max_iterations': ('INT', {'default': 100, 'min': 0, 'max': 1024}), 'tolerance': ('FLOAT', {'default': 0.01, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.kmeans.__doc__

    CATEGORY = "MagickWand/Quantize"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'kmeans', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Kuwahara:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.kuwahara.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'kuwahara', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Level:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'black': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'white': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'gamma': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.level.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'level', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Levelize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'black': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'white': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'gamma': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.levelize.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'levelize', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class LinearStretch:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'black_point': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'white_point': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.linear_stretch.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'linear_stretch', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class LiquidRescale:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'delta_x': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'rigidity': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.liquid_rescale.__doc__

    CATEGORY = "MagickWand/Resize"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'liquid_rescale', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class LocalContrast:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 10, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'strength': ('FLOAT', {'default': 12.5, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.local_contrast.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'local_contrast', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Magnify:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.magnify.__doc__

    CATEGORY = "MagickWand/Resize"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'magnify', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class MeanShift:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'color_distance': ('FLOAT', {'default': 0.1, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.mean_shift.__doc__

    CATEGORY = "MagickWand/Feature"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'mean_shift', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class MergeLayers:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'method': (['merge', 'flatten', 'mosaic', 'trimbounds'], {'default': 'flatten'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.merge_layers.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'merge_layers', kwargs, type='whole')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Mode:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.mode.__doc__

    CATEGORY = "MagickWand/Statistic"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'mode', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Modulate:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'brightness': ('FLOAT', {'default': 100.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'saturation': ('FLOAT', {'default': 100.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'hue': ('FLOAT', {'default': 100.0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.modulate.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'modulate', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Morphology:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'method': (['undefined', 'convolve', 'correlate', 'erode', 'dilate', 'erode_intensity', 'dilate_intensity', 'iterative_distance', 'open', 'close', 'open_intensity', 'close_intensity', 'smooth', 'edgein', 'edgeout', 'edge', 'tophat', 'bottom_hat', 'hit_and_miss', 'thinning', 'thicken', 'distance', 'voronoi'], {'default': 'convolve'}), 'kernel': (['undefined', 'unity', 'gaussian', 'dog', 'log', 'blur', 'comet', 'binomial', 'laplacian', 'sobel', 'frei_chen', 'roberts', 'prewitt', 'compass', 'kirsch', 'diamond', 'square', 'rectangle', 'octagon', 'disk', 'plus', 'cross', 'ring', 'peaks', 'edges', 'corners', 'diagonals', 'line_ends', 'line_junctions', 'ridges', 'convex_hull', 'thin_se', 'skeleton', 'chebyshev', 'manhattan', 'octagonal', 'euclidean', 'user_defined'], {'default': 'unity'}), 'iterations': ('INT', {'default': 1, 'min': 0, 'max': 1024}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.morphology.__doc__

    CATEGORY = "MagickWand/Morphology"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'morphology', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class MotionBlur:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'angle': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.motion_blur.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'motion_blur', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Negate:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'grayscale': ('BOOLEAN', {'default': False}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.negate.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'negate', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Noise:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'noise_type': (['undefined', 'uniform', 'gaussian', 'multiplicative_gaussian', 'impulse', 'laplacian', 'poisson', 'random'], {'default': 'uniform'}), 'attenuate': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.noise.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'noise', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Normalize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'channel': (['red', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha'], {'default': 'cyan'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.normalize.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'normalize', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class OilPaint:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.oil_paint.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'oil_paint', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class OrderedDither:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'threshold_map': ('STRING', {'multiline': False, 'default': 'threshold'}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.ordered_dither.__doc__

    CATEGORY = "MagickWand/Quantize"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'ordered_dither', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Polynomial:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'arguments': ('STRING', {'multiline': False, 'default': '0.5, 1.0'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.polynomial.__doc__

    CATEGORY = "MagickWand/Statistic"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'polynomial', kwargs, type='whole')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Posterize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'levels': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'dither': (['undefined', 'no', 'riemersma', 'floyd_steinberg'], {'default': 'no'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.posterize.__doc__

    CATEGORY = "MagickWand/Quantize"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'posterize', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Quantize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'number_colors': ('INT', {'default': 16, 'min': 1, 'max': 1024}), 'colorspace_type': (['undefined', 'cmy', 'cmyk', 'gray', 'hcl', 'hclp', 'hsb', 'hsi', 'hsl', 'hsv', 'hwb', 'lab', 'lch', 'lchab', 'lchuv', 'log', 'lms', 'luv', 'ohta', 'rec601ycbcr', 'rec709ycbcr', 'rgb', 'scrgb', 'srgb', 'transparent', 'xyy', 'xyz', 'ycbcr', 'ycc', 'ydbdr', 'yiq', 'ypbpr', 'yuv'], {'default': 'cmy'}), 'treedepth': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'dither': (['undefined', 'no', 'riemersma', 'floyd_steinberg'], {'default': 'no'}), 'measure_error': ('BOOLEAN', {'default': False})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.quantize.__doc__

    CATEGORY = "MagickWand/Quantize"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'quantize', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class RandomThreshold:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'low': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'high': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.random_threshold.__doc__

    CATEGORY = "MagickWand/Thresold"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'random_threshold', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class RangeThreshold:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'low_black': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'low_white': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'high_white': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'high_black': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.range_threshold.__doc__

    CATEGORY = "MagickWand/Thresold"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'range_threshold', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Resample:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'x_res': ('FLOAT', {'default': 512, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'y_res': ('FLOAT', {'default': 512, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'filter': (['undefined', 'point', 'box', 'triangle', 'hermite', 'hanning', 'hamming', 'blackman', 'gaussian', 'quadratic', 'cubic', 'catrom', 'mitchell', 'jinc', 'sinc', 'sincfast', 'kaiser', 'welsh', 'parzen', 'bohman', 'bartlett', 'lagrange', 'lanczos', 'lanczossharp', 'lanczos2', 'lanczos2sharp', 'robidoux', 'robidouxsharp', 'cosine', 'spline', 'sentinel'], {'default': 'point'}), 'blur': ('FLOAT', {'default': 1, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.resample.__doc__

    CATEGORY = "MagickWand/Resize"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'resample', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Resize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'filter': (['undefined', 'point', 'box', 'triangle', 'hermite', 'hanning', 'hamming', 'blackman', 'gaussian', 'quadratic', 'cubic', 'catrom', 'mitchell', 'jinc', 'sinc', 'sincfast', 'kaiser', 'welsh', 'parzen', 'bohman', 'bartlett', 'lagrange', 'lanczos', 'lanczossharp', 'lanczos2', 'lanczos2sharp', 'robidoux', 'robidouxsharp', 'cosine', 'spline', 'sentinel'], {'default': 'point'}), 'blur': ('FLOAT', {'default': 1, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.resize.__doc__

    CATEGORY = "MagickWand/Resize"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'resize', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Roll:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'x': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'y': ('INT', {'default': 0, 'min': 0, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.roll.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'roll', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class RotationalBlur:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'angle': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.rotational_blur.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'rotational_blur', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Sample:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.sample.__doc__

    CATEGORY = "MagickWand/Resize"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'sample', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Scale:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'columns': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'rows': ('INT', {'default': 512, 'min': 1, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.scale.__doc__

    CATEGORY = "MagickWand/Resize"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'scale', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class SelectiveBlur:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'threshold': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.selective_blur.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'selective_blur', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class SepiaTone:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'threshold': ('FLOAT', {'default': 0.8, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.sepia_tone.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'sepia_tone', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Shade:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'gray': ('BOOLEAN', {'default': False}), 'azimuth': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'elevation': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.shade.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'shade', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Shadow:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'alpha': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'x': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'y': ('INT', {'default': 0, 'min': 0, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.shadow.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'shadow', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Sharpen:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.sharpen.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'sharpen', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Shave:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'columns': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'rows': ('INT', {'default': 512, 'min': 1, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.shave.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'shave', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class SigmoidalContrast:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'sharpen': ('BOOLEAN', {'default': True}), 'strength': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'midpoint': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.sigmoidal_contrast.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'sigmoidal_contrast', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Sketch:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'angle': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.sketch.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'sketch', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Smush:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'stacked': ('BOOLEAN', {'default': False}), 'offset': ('INT', {'default': 0, 'min': 0, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.smush.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'smush', kwargs, type='whole')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Solarize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'threshold': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.solarize.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'solarize', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Splice:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'x': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'y': ('INT', {'default': 0, 'min': 0, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.splice.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'splice', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Spread:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'method': (['undefined', 'average', 'average9', 'average16', 'background', 'bilinear', 'blend', 'catrom', 'integer', 'mesh', 'nearest', 'spline'], {'default': 'average'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.spread.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'spread', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Statistic:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'stat': (['undefined', 'gradient', 'maximum', 'mean', 'median', 'minimum', 'mode', 'nonpeak', 'root_mean_square', 'standard_deviation'], {'default': 'gradient'}), 'width': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.statistic.__doc__

    CATEGORY = "MagickWand/Statistic"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'statistic', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Swirl:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'degree': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'method': (['undefined', 'average', 'average9', 'average16', 'background', 'bilinear', 'blend', 'catrom', 'integer', 'mesh', 'nearest', 'spline'], {'default': 'average'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.swirl.__doc__

    CATEGORY = "MagickWand/Morphology"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'swirl', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Threshold:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'threshold': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.threshold.__doc__

    CATEGORY = "MagickWand/Thresold"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'threshold', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Thumbnail:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.thumbnail.__doc__

    CATEGORY = "MagickWand/Resize"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'thumbnail', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Transform:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'crop': ('STRING', {'multiline': False, 'default': ''}), 'resize': ('STRING', {'multiline': False, 'default': ''})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.transform.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'transform', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class TransformColorspace:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'colorspace_type': (['undefined', 'cmy', 'cmyk', 'gray', 'hcl', 'hclp', 'hsb', 'hsi', 'hsl', 'hsv', 'hwb', 'lab', 'lch', 'lchab', 'lchuv', 'log', 'lms', 'luv', 'ohta', 'rec601ycbcr', 'rec709ycbcr', 'rgb', 'scrgb', 'srgb', 'transparent', 'xyy', 'xyz', 'ycbcr', 'ycc', 'ydbdr', 'yiq', 'ypbpr', 'yuv'], {'default': 'cmy'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.transform_colorspace.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'transform_colorspace', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Transparentize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'transparency': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.transparentize.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'transparentize', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Transpose:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.transpose.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'transpose', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Transverse:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.transverse.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'transverse', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class UnsharpMask:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'amount': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'threshold': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.unsharp_mask.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'unsharp_mask', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Vignette:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'x': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'y': ('INT', {'default': 0, 'min': 0, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.vignette.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'vignette', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Wave:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'amplitude': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'wave_length': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'method': (['undefined', 'average', 'average9', 'average16', 'background', 'bilinear', 'blend', 'catrom', 'integer', 'mesh', 'nearest', 'spline'], {'default': 'average'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.wave.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'wave', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class WaveletDenoise:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'threshold': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'softness': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.wavelet_denoise.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'wavelet_denoise', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class WhiteBalance:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.white_balance.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        kwargs = preprocess_kwargs(**kwargs)
        apply_to_wand_seq(wand_img, 'white_balance', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )

NODE_CLASS_MAPPINGS = {
    "ImageMagick Adaptive Blur": AdaptiveBlur,
    "ImageMagick Adaptive Resize": AdaptiveResize,
    "ImageMagick Adaptive Sharpen": AdaptiveSharpen,
    "ImageMagick Adaptive Threshold": AdaptiveThreshold,
    "ImageMagick Auto Gamma": AutoGamma,
    "ImageMagick Auto Level": AutoLevel,
    "ImageMagick Auto Orient": AutoOrient,
    "ImageMagick Auto Threshold": AutoThreshold,
    "ImageMagick Blue Shift": BlueShift,
    "ImageMagick Blur": Blur,
    "ImageMagick Brightness Contrast": BrightnessContrast,
    "ImageMagick Canny": Canny,
    "ImageMagick Charcoal": Charcoal,
    "ImageMagick Chop": Chop,
    "ImageMagick Clahe": Clahe,
    "ImageMagick Clamp": Clamp,
    "ImageMagick Coalesce": Coalesce,
    "ImageMagick Color Decision List": ColorDecisionList,
    "ImageMagick Color Matrix": ColorMatrix,
    "ImageMagick Combine": Combine,
    "ImageMagick Concat": Concat,
    "ImageMagick Contrast": Contrast,
    "ImageMagick Contrast Stretch": ContrastStretch,
    "ImageMagick Crop": Crop,
    "ImageMagick Cycle Color Map": CycleColorMap,
    "ImageMagick Decipher": Decipher,
    "ImageMagick Despeckle": Despeckle,
    "ImageMagick Distort": Distort,
    "ImageMagick Edge": Edge,
    "ImageMagick Emboss": Emboss,
    "ImageMagick Encipher": Encipher,
    "ImageMagick Enhance": Enhance,
    "ImageMagick Equalize": Equalize,
    "ImageMagick Evaluate": Evaluate,
    "ImageMagick Extent": Extent,
    "ImageMagick Flip": Flip,
    "ImageMagick Flop": Flop,
    "ImageMagick Forward Fourier Transform": ForwardFourierTransform,
    "ImageMagick Function": Function,
    "ImageMagick Gamma": Gamma,
    "ImageMagick Gaussian Blur": GaussianBlur,
    "ImageMagick Hough Lines": HoughLines,
    "ImageMagick Implode": Implode,
    "ImageMagick Kmeans": Kmeans,
    "ImageMagick Kuwahara": Kuwahara,
    "ImageMagick Level": Level,
    "ImageMagick Levelize": Levelize,
    "ImageMagick Linear Stretch": LinearStretch,
    "ImageMagick Liquid Rescale": LiquidRescale,
    "ImageMagick Local Contrast": LocalContrast,
    "ImageMagick Magnify": Magnify,
    "ImageMagick Mean Shift": MeanShift,
    "ImageMagick Merge Layers": MergeLayers,
    "ImageMagick Mode": Mode,
    "ImageMagick Modulate": Modulate,
    "ImageMagick Morphology": Morphology,
    "ImageMagick Motion Blur": MotionBlur,
    "ImageMagick Negate": Negate,
    "ImageMagick Noise": Noise,
    "ImageMagick Normalize": Normalize,
    "ImageMagick Oil Paint": OilPaint,
    "ImageMagick Ordered Dither": OrderedDither,
    "ImageMagick Polynomial": Polynomial,
    "ImageMagick Posterize": Posterize,
    "ImageMagick Quantize": Quantize,
    "ImageMagick Random Threshold": RandomThreshold,
    "ImageMagick Range Threshold": RangeThreshold,
    "ImageMagick Resample": Resample,
    "ImageMagick Resize": Resize,
    "ImageMagick Roll": Roll,
    "ImageMagick Rotational Blur": RotationalBlur,
    "ImageMagick Sample": Sample,
    "ImageMagick Scale": Scale,
    "ImageMagick Selective Blur": SelectiveBlur,
    "ImageMagick Sepia Tone": SepiaTone,
    "ImageMagick Shade": Shade,
    "ImageMagick Shadow": Shadow,
    "ImageMagick Sharpen": Sharpen,
    "ImageMagick Shave": Shave,
    "ImageMagick Sigmoidal Contrast": SigmoidalContrast,
    "ImageMagick Sketch": Sketch,
    "ImageMagick Smush": Smush,
    "ImageMagick Solarize": Solarize,
    "ImageMagick Splice": Splice,
    "ImageMagick Spread": Spread,
    "ImageMagick Statistic": Statistic,
    "ImageMagick Swirl": Swirl,
    "ImageMagick Threshold": Threshold,
    "ImageMagick Thumbnail": Thumbnail,
    "ImageMagick Transform": Transform,
    "ImageMagick Transform Colorspace": TransformColorspace,
    "ImageMagick Transparentize": Transparentize,
    "ImageMagick Transpose": Transpose,
    "ImageMagick Transverse": Transverse,
    "ImageMagick Unsharp Mask": UnsharpMask,
    "ImageMagick Vignette": Vignette,
    "ImageMagick Wave": Wave,
    "ImageMagick Wavelet Denoise": WaveletDenoise,
    "ImageMagick White Balance": WhiteBalance,
}
