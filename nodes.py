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
        return safe_wand_execute(image, 'adaptive_blur', kwargs, apply_type='iterative')


class AdaptiveResize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'columns': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'rows': ('INT', {'default': 512, 'min': 1, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.adaptive_resize.__doc__

    CATEGORY = "MagickWand/Resize"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'adaptive_resize', kwargs, apply_type='iterative')


class AdaptiveSharpen:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.adaptive_sharpen.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'adaptive_sharpen', kwargs, apply_type='iterative')


class AdaptiveThreshold:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'offset': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.adaptive_threshold.__doc__

    CATEGORY = "MagickWand/Thresold"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'adaptive_threshold', kwargs, apply_type='iterative')


class AutoGamma:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.auto_gamma.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'auto_gamma', kwargs, apply_type='iterative')


class AutoLevel:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.auto_level.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'auto_level', kwargs, apply_type='iterative')


class AutoOrient:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.auto_orient.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'auto_orient', kwargs, apply_type='iterative')


class AutoThreshold:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'method': (['undefined', 'kapur', 'otsu', 'triangle'], {'default': 'kapur'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.auto_threshold.__doc__

    CATEGORY = "MagickWand/Thresold"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'auto_threshold', kwargs, apply_type='iterative')


class BlueShift:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'factor': ('FLOAT', {'default': 1.5, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.blue_shift.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'blue_shift', kwargs, apply_type='iterative')


class Blur:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.blur.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'blur', kwargs, apply_type='iterative')


class BrightnessContrast:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'brightness': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'contrast': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.brightness_contrast.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'brightness_contrast', kwargs, apply_type='iterative')


class Canny:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'lower_percent': ('FLOAT', {'default': 0.1, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'upper_percent': ('FLOAT', {'default': 0.3, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.canny.__doc__

    CATEGORY = "MagickWand/Feature"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'canny', kwargs, apply_type='iterative')


class Charcoal:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.charcoal.__doc__

    CATEGORY = "MagickWand/Feature"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'charcoal', kwargs, apply_type='iterative')


class Chop:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'x': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'y': ('INT', {'default': 0, 'min': 0, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.chop.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'chop', kwargs, apply_type='iterative')


class Clahe:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'number_bins': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'clip_limit': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.clahe.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'clahe', kwargs, apply_type='iterative')


class Clamp:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.clamp.__doc__

    CATEGORY = "MagickWand/Quantize"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'clamp', kwargs, apply_type='iterative')


class Coalesce:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.coalesce.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'coalesce', kwargs, apply_type='whole')


class ColorDecisionList:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'ccc': ('STRING', {'multiline': True, 'default': '<ColorCorrectionCollection xmlns="urn:ASC:CDL:v1.2">\n    <ColorCorrection id="cc03345">\n        <SOPNode>\n            <Slope> 0.9 1.2 0.5 </Slope>\n            <Offset> 0.4 -0.5 0.6 </Offset>\n            <Power> 1.0 0.8 1.5 </Power>\n        </SOPNode>\n        <SATNode>\n            <Saturation> 0.85 </Saturation>\n        </SATNode>\n    </ColorCorrection>\n</ColorCorrectionCollection>'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.color_decision_list.__doc__

    CATEGORY = "MagickWand/Color Matrix & Decision List"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'color_decision_list', kwargs, apply_type='iterative')


class ColorMatrix:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'matrix': ('STRING', {'multiline': True, 'default': '[\n    [1.0, 0.0, 0.0],\n    [0.0, 1.0, 0.0],\n    [0.0, 0.0, 1.0],\n]'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.color_matrix.__doc__

    CATEGORY = "MagickWand/Color Matrix & Decision List"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'color_matrix', kwargs, apply_type='iterative')


class Combine:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'}), 'colorspace': (['undefined', 'cmy', 'cmyk', 'gray', 'hcl', 'hclp', 'hsb', 'hsi', 'hsl', 'hsv', 'hwb', 'lab', 'lch', 'lchab', 'lchuv', 'log', 'lms', 'luv', 'ohta', 'rec601ycbcr', 'rec709ycbcr', 'rgb', 'scrgb', 'srgb', 'transparent', 'xyy', 'xyz', 'ycbcr', 'ycc', 'ydbdr', 'yiq', 'ypbpr', 'yuv'], {'default': 'cmy'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.combine.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'combine', kwargs, apply_type='whole')


class Concat:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'stacked': ('BOOLEAN', {'default': False})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.concat.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'concat', kwargs, apply_type='whole')


class Contrast:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'sharpen': ('BOOLEAN', {'default': True})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.contrast.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'contrast', kwargs, apply_type='iterative')


class ContrastStretch:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'black_point': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'white_point': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.contrast_stretch.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'contrast_stretch', kwargs, apply_type='iterative')


class Crop:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'left': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'top': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'width': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'reset_coords': ('BOOLEAN', {'default': True})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.crop.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'crop', kwargs, apply_type='iterative')


class CycleColorMap:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'offset': ('INT', {'default': 1, 'min': 0, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.cycle_color_map.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'cycle_color_map', kwargs, apply_type='iterative')


class Decipher:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'passphrase': ('STRING', {'multiline': False, 'default': ''})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.decipher.__doc__

    CATEGORY = "MagickWand/Cipher"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'decipher', kwargs, apply_type='iterative')


class Despeckle:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.despeckle.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'despeckle', kwargs, apply_type='iterative')


class Distort:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'method': (['undefined', 'affine', 'affine_projection', 'scale_rotate_translate', 'perspective', 'perspective_projection', 'bilinear_forward', 'bilinear_reverse', 'polynomial', 'arc', 'polar', 'depolar', 'cylinder_2_plane', 'plane_2_cylinder', 'barrel', 'barrel_inverse', 'shepards', 'resize', 'sentinel', 'rigidaffine'], {'default': 'affine'}), 'arguments': ('STRING', {'multiline': False, 'default': '0, 0, 20, 60, 90, 0, 70, 63, 0, 90, 5, 83, 90, 90, 85, 88'}), 'best_fit': ('BOOLEAN', {'default': False}), 'filter': (['undefined', 'point', 'box', 'triangle', 'hermite', 'hanning', 'hamming', 'blackman', 'gaussian', 'quadratic', 'cubic', 'catrom', 'mitchell', 'jinc', 'sinc', 'sincfast', 'kaiser', 'welsh', 'parzen', 'bohman', 'bartlett', 'lagrange', 'lanczos', 'lanczossharp', 'lanczos2', 'lanczos2sharp', 'robidoux', 'robidouxsharp', 'cosine', 'spline', 'sentinel'], {'default': 'point'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.distort.__doc__

    CATEGORY = "MagickWand/Morphology"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'distort', kwargs, apply_type='iterative')


class Edge:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.edge.__doc__

    CATEGORY = "MagickWand/Feature"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'edge', kwargs, apply_type='iterative')


class Emboss:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.emboss.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'emboss', kwargs, apply_type='iterative')


class Encipher:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'passphrase': ('STRING', {'multiline': False, 'default': ''})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.encipher.__doc__

    CATEGORY = "MagickWand/Cipher"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'encipher', kwargs, apply_type='iterative')


class Enhance:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.enhance.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'enhance', kwargs, apply_type='iterative')


class Equalize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.equalize.__doc__

    CATEGORY = "MagickWand/Statistic"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'equalize', kwargs, apply_type='iterative')


class Evaluate:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'operator': (['undefined', 'abs', 'add', 'addmodulus', 'and', 'cosine', 'divide', 'exponential', 'gaussiannoise', 'impulsenoise', 'laplaciannoise', 'leftshift', 'log', 'max', 'mean', 'median', 'min', 'multiplicativenoise', 'multiply', 'or', 'poissonnoise', 'pow', 'rightshift', 'rootmeansquare', 'set', 'sine', 'subtract', 'sum', 'thresholdblack', 'threshold', 'thresholdwhite', 'uniformnoise', 'xor', 'inverse_log'], {'default': 'abs'}), 'value': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.evaluate.__doc__

    CATEGORY = "MagickWand/Statistic"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'evaluate', kwargs, apply_type='iterative')


class Extent:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'x': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'y': ('INT', {'default': 0, 'min': 0, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.extent.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'extent', kwargs, apply_type='iterative')


class Flip:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.flip.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'flip', kwargs, apply_type='iterative')


class Flop:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.flop.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'flop', kwargs, apply_type='iterative')


class ForwardFourierTransform:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'magnitude': ('BOOLEAN', {'default': True})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.forward_fourier_transform.__doc__

    CATEGORY = "MagickWand/Fourier"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'forward_fourier_transform', kwargs, apply_type='iterative')


class Function:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'function': (['undefined', 'arcsin', 'arctan', 'polynomial', 'sinusoid'], {'default': 'arcsin'}), 'arguments': ('STRING', {'multiline': False, 'default': '0.5, 1.0'}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.function.__doc__

    CATEGORY = "MagickWand/Statistic"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'function', kwargs, apply_type='iterative')


class Gamma:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'adjustment_value': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.gamma.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'gamma', kwargs, apply_type='iterative')


class GaussianBlur:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.gaussian_blur.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'gaussian_blur', kwargs, apply_type='iterative')


class HoughLines:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'threshold': ('INT', {'default': 40, 'min': 0, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.hough_lines.__doc__

    CATEGORY = "MagickWand/Feature"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'hough_lines', kwargs, apply_type='iterative')


class Implode:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'amount': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'method': (['undefined', 'average', 'average9', 'average16', 'background', 'bilinear', 'blend', 'catrom', 'integer', 'mesh', 'nearest', 'spline'], {'default': 'average'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.implode.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'implode', kwargs, apply_type='iterative')


class Kmeans:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'number_colors': ('INT', {'default': 16, 'min': 1, 'max': 1024}), 'max_iterations': ('INT', {'default': 100, 'min': 0, 'max': 1024}), 'tolerance': ('FLOAT', {'default': 0.01, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.kmeans.__doc__

    CATEGORY = "MagickWand/Quantize"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'kmeans', kwargs, apply_type='iterative')


class Kuwahara:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.kuwahara.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'kuwahara', kwargs, apply_type='iterative')


class Level:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'black': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'white': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'gamma': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.level.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'level', kwargs, apply_type='iterative')


class Levelize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'black': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'white': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'gamma': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.levelize.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'levelize', kwargs, apply_type='iterative')


class LinearStretch:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'black_point': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'white_point': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.linear_stretch.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'linear_stretch', kwargs, apply_type='iterative')


class LiquidRescale:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'delta_x': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'rigidity': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.liquid_rescale.__doc__

    CATEGORY = "MagickWand/Resize"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'liquid_rescale', kwargs, apply_type='iterative')


class LocalContrast:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 10, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'strength': ('FLOAT', {'default': 12.5, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.local_contrast.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'local_contrast', kwargs, apply_type='iterative')


class Magnify:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.magnify.__doc__

    CATEGORY = "MagickWand/Resize"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'magnify', kwargs, apply_type='iterative')


class MeanShift:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'color_distance': ('FLOAT', {'default': 0.1, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.mean_shift.__doc__

    CATEGORY = "MagickWand/Feature"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'mean_shift', kwargs, apply_type='iterative')


class MergeLayers:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'method': (['merge', 'flatten', 'mosaic', 'trimbounds'], {'default': 'flatten'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.merge_layers.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'merge_layers', kwargs, apply_type='whole')


class Mode:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.mode.__doc__

    CATEGORY = "MagickWand/Statistic"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'mode', kwargs, apply_type='iterative')


class Modulate:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'brightness': ('FLOAT', {'default': 100.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'saturation': ('FLOAT', {'default': 100.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'hue': ('FLOAT', {'default': 100.0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.modulate.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'modulate', kwargs, apply_type='iterative')


class Morphology:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'method': (['undefined', 'convolve', 'correlate', 'erode', 'dilate', 'erode_intensity', 'dilate_intensity', 'iterative_distance', 'open', 'close', 'open_intensity', 'close_intensity', 'smooth', 'edgein', 'edgeout', 'edge', 'tophat', 'bottom_hat', 'hit_and_miss', 'thinning', 'thicken', 'distance', 'voronoi'], {'default': 'convolve'}), 'kernel': (['undefined', 'unity', 'gaussian', 'dog', 'log', 'blur', 'comet', 'binomial', 'laplacian', 'sobel', 'frei_chen', 'roberts', 'prewitt', 'compass', 'kirsch', 'diamond', 'square', 'rectangle', 'octagon', 'disk', 'plus', 'cross', 'ring', 'peaks', 'edges', 'corners', 'diagonals', 'line_ends', 'line_junctions', 'ridges', 'convex_hull', 'thin_se', 'skeleton', 'chebyshev', 'manhattan', 'octagonal', 'euclidean', 'user_defined'], {'default': 'unity'}), 'iterations': ('INT', {'default': 1, 'min': 0, 'max': 1024}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.morphology.__doc__

    CATEGORY = "MagickWand/Morphology"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'morphology', kwargs, apply_type='iterative')


class MotionBlur:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'angle': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.motion_blur.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'motion_blur', kwargs, apply_type='iterative')


class Negate:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'grayscale': ('BOOLEAN', {'default': False}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.negate.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'negate', kwargs, apply_type='iterative')


class Noise:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'noise_type': (['undefined', 'uniform', 'gaussian', 'multiplicative_gaussian', 'impulse', 'laplacian', 'poisson', 'random'], {'default': 'uniform'}), 'attenuate': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.noise.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'noise', kwargs, apply_type='iterative')


class Normalize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'channel': (['red', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha'], {'default': 'cyan'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.normalize.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'normalize', kwargs, apply_type='iterative')


class OilPaint:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.oil_paint.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'oil_paint', kwargs, apply_type='iterative')


class OrderedDither:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'threshold_map': ('STRING', {'multiline': False, 'default': 'threshold'}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.ordered_dither.__doc__

    CATEGORY = "MagickWand/Quantize"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'ordered_dither', kwargs, apply_type='iterative')


class Polynomial:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'arguments': ('STRING', {'multiline': False, 'default': '0.5, 1.0'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.polynomial.__doc__

    CATEGORY = "MagickWand/Statistic"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'polynomial', kwargs, apply_type='whole')


class Posterize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'levels': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'dither': (['undefined', 'no', 'riemersma', 'floyd_steinberg'], {'default': 'no'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.posterize.__doc__

    CATEGORY = "MagickWand/Quantize"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'posterize', kwargs, apply_type='iterative')


class Quantize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'number_colors': ('INT', {'default': 16, 'min': 1, 'max': 1024}), 'colorspace_type': (['undefined', 'cmy', 'cmyk', 'gray', 'hcl', 'hclp', 'hsb', 'hsi', 'hsl', 'hsv', 'hwb', 'lab', 'lch', 'lchab', 'lchuv', 'log', 'lms', 'luv', 'ohta', 'rec601ycbcr', 'rec709ycbcr', 'rgb', 'scrgb', 'srgb', 'transparent', 'xyy', 'xyz', 'ycbcr', 'ycc', 'ydbdr', 'yiq', 'ypbpr', 'yuv'], {'default': 'cmy'}), 'treedepth': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'dither': (['undefined', 'no', 'riemersma', 'floyd_steinberg'], {'default': 'no'}), 'measure_error': ('BOOLEAN', {'default': False})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.quantize.__doc__

    CATEGORY = "MagickWand/Quantize"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'quantize', kwargs, apply_type='iterative')


class RandomThreshold:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'low': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'high': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.random_threshold.__doc__

    CATEGORY = "MagickWand/Thresold"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'random_threshold', kwargs, apply_type='iterative')


class RangeThreshold:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'low_black': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'low_white': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'high_white': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'high_black': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.range_threshold.__doc__

    CATEGORY = "MagickWand/Thresold"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'range_threshold', kwargs, apply_type='iterative')


class Resample:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'x_res': ('FLOAT', {'default': 512, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'y_res': ('FLOAT', {'default': 512, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'filter': (['undefined', 'point', 'box', 'triangle', 'hermite', 'hanning', 'hamming', 'blackman', 'gaussian', 'quadratic', 'cubic', 'catrom', 'mitchell', 'jinc', 'sinc', 'sincfast', 'kaiser', 'welsh', 'parzen', 'bohman', 'bartlett', 'lagrange', 'lanczos', 'lanczossharp', 'lanczos2', 'lanczos2sharp', 'robidoux', 'robidouxsharp', 'cosine', 'spline', 'sentinel'], {'default': 'point'}), 'blur': ('FLOAT', {'default': 1, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.resample.__doc__

    CATEGORY = "MagickWand/Resize"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'resample', kwargs, apply_type='iterative')


class Resize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'filter': (['undefined', 'point', 'box', 'triangle', 'hermite', 'hanning', 'hamming', 'blackman', 'gaussian', 'quadratic', 'cubic', 'catrom', 'mitchell', 'jinc', 'sinc', 'sincfast', 'kaiser', 'welsh', 'parzen', 'bohman', 'bartlett', 'lagrange', 'lanczos', 'lanczossharp', 'lanczos2', 'lanczos2sharp', 'robidoux', 'robidouxsharp', 'cosine', 'spline', 'sentinel'], {'default': 'point'}), 'blur': ('FLOAT', {'default': 1, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.resize.__doc__

    CATEGORY = "MagickWand/Resize"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'resize', kwargs, apply_type='iterative')


class Roll:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'x': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'y': ('INT', {'default': 0, 'min': 0, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.roll.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'roll', kwargs, apply_type='iterative')


class RotationalBlur:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'angle': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.rotational_blur.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'rotational_blur', kwargs, apply_type='iterative')


class Sample:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.sample.__doc__

    CATEGORY = "MagickWand/Resize"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'sample', kwargs, apply_type='iterative')


class Scale:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'columns': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'rows': ('INT', {'default': 512, 'min': 1, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.scale.__doc__

    CATEGORY = "MagickWand/Resize"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'scale', kwargs, apply_type='iterative')


class SelectiveBlur:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'threshold': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.selective_blur.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'selective_blur', kwargs, apply_type='iterative')


class SepiaTone:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'threshold': ('FLOAT', {'default': 0.8, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.sepia_tone.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'sepia_tone', kwargs, apply_type='iterative')


class Shade:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'gray': ('BOOLEAN', {'default': False}), 'azimuth': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'elevation': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.shade.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'shade', kwargs, apply_type='iterative')


class Shadow:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'alpha': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'x': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'y': ('INT', {'default': 0, 'min': 0, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.shadow.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'shadow', kwargs, apply_type='iterative')


class Sharpen:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.sharpen.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'sharpen', kwargs, apply_type='iterative')


class Shave:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'columns': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'rows': ('INT', {'default': 512, 'min': 1, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.shave.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'shave', kwargs, apply_type='iterative')


class SigmoidalContrast:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'sharpen': ('BOOLEAN', {'default': True}), 'strength': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'midpoint': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.sigmoidal_contrast.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'sigmoidal_contrast', kwargs, apply_type='iterative')


class Sketch:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'angle': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.sketch.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'sketch', kwargs, apply_type='iterative')


class Smush:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'stacked': ('BOOLEAN', {'default': False}), 'offset': ('INT', {'default': 0, 'min': 0, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.smush.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'smush', kwargs, apply_type='whole')


class Solarize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'threshold': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.solarize.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'solarize', kwargs, apply_type='iterative')


class Splice:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'x': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'y': ('INT', {'default': 0, 'min': 0, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.splice.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'splice', kwargs, apply_type='iterative')


class Spread:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'method': (['undefined', 'average', 'average9', 'average16', 'background', 'bilinear', 'blend', 'catrom', 'integer', 'mesh', 'nearest', 'spline'], {'default': 'average'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.spread.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'spread', kwargs, apply_type='iterative')


class Statistic:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'stat': (['undefined', 'gradient', 'maximum', 'mean', 'median', 'minimum', 'mode', 'nonpeak', 'root_mean_square', 'standard_deviation'], {'default': 'gradient'}), 'width': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.statistic.__doc__

    CATEGORY = "MagickWand/Statistic"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'statistic', kwargs, apply_type='iterative')


class Swirl:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'degree': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'method': (['undefined', 'average', 'average9', 'average16', 'background', 'bilinear', 'blend', 'catrom', 'integer', 'mesh', 'nearest', 'spline'], {'default': 'average'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.swirl.__doc__

    CATEGORY = "MagickWand/Morphology"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'swirl', kwargs, apply_type='iterative')


class Threshold:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'threshold': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.threshold.__doc__

    CATEGORY = "MagickWand/Thresold"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'threshold', kwargs, apply_type='iterative')


class Thumbnail:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 512, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.thumbnail.__doc__

    CATEGORY = "MagickWand/Resize"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'thumbnail', kwargs, apply_type='iterative')


class Transform:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'crop': ('STRING', {'multiline': False, 'default': ''}), 'resize': ('STRING', {'multiline': False, 'default': ''})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.transform.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'transform', kwargs, apply_type='iterative')


class TransformColorspace:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'colorspace_type': (['undefined', 'cmy', 'cmyk', 'gray', 'hcl', 'hclp', 'hsb', 'hsi', 'hsl', 'hsv', 'hwb', 'lab', 'lch', 'lchab', 'lchuv', 'log', 'lms', 'luv', 'ohta', 'rec601ycbcr', 'rec709ycbcr', 'rgb', 'scrgb', 'srgb', 'transparent', 'xyy', 'xyz', 'ycbcr', 'ycc', 'ydbdr', 'yiq', 'ypbpr', 'yuv'], {'default': 'cmy'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.transform_colorspace.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'transform_colorspace', kwargs, apply_type='iterative')


class Transparentize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'transparency': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.transparentize.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'transparentize', kwargs, apply_type='iterative')


class Transpose:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.transpose.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'transpose', kwargs, apply_type='iterative')


class Transverse:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.transverse.__doc__

    CATEGORY = "MagickWand/Transform"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'transverse', kwargs, apply_type='iterative')


class UnsharpMask:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'amount': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'threshold': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'red'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.unsharp_mask.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'unsharp_mask', kwargs, apply_type='iterative')


class Vignette:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'x': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'y': ('INT', {'default': 0, 'min': 0, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.vignette.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'vignette', kwargs, apply_type='iterative')


class Wave:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'amplitude': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'wave_length': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'method': (['undefined', 'average', 'average9', 'average16', 'background', 'bilinear', 'blend', 'catrom', 'integer', 'mesh', 'nearest', 'spline'], {'default': 'average'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.wave.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'wave', kwargs, apply_type='iterative')


class WaveletDenoise:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'threshold': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'softness': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.wavelet_denoise.__doc__

    CATEGORY = "MagickWand/Effect"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'wavelet_denoise', kwargs, apply_type='iterative')


class WhiteBalance:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = Image.white_balance.__doc__

    CATEGORY = "MagickWand/Enhance"

    def execute(self, image, **kwargs):
        return safe_wand_execute(image, 'white_balance', kwargs, apply_type='iterative')

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
