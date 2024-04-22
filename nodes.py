import numpy as np
from wand.image import Image
import torch
from .utils import *

class Blur:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'blur').__doc__

    CATEGORY = "MagickWand/Effects"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'blur', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Canny:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'lower_percent': ('FLOAT', {'default': 0.1, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'upper_percent': ('FLOAT', {'default': 0.3, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'canny').__doc__

    CATEGORY = "MagickWand/Effects"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
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
    DESCRIPTION = getattr(Image, 'charcoal').__doc__

    CATEGORY = "MagickWand/Effects"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'charcoal', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Chop:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 128, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 128, 'min': 1, 'max': 1024}), 'x': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'y': ('INT', {'default': 0, 'min': 0, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'chop').__doc__

    CATEGORY = "MagickWand/Resizing and cropping"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'chop', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Clahe:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 128, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 128, 'min': 1, 'max': 1024}), 'number_bins': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'clip_limit': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'clahe').__doc__

    CATEGORY = "MagickWand/Effects"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'clahe', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Clamp:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'clamp').__doc__

    CATEGORY = "MagickWand/Effects"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'clamp', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Combine:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'}), 'colorspace': (['undefined', 'cmy', 'cmyk', 'gray', 'hcl', 'hclp', 'hsb', 'hsi', 'hsl', 'hsv', 'hwb', 'lab', 'lch', 'lchab', 'lchuv', 'log', 'lms', 'luv', 'ohta', 'rec601ycbcr', 'rec709ycbcr', 'rgb', 'scrgb', 'srgb', 'transparent', 'xyy', 'xyz', 'ycbcr', 'ycc', 'ydbdr', 'yiq', 'ypbpr', 'yuv'], {'default': 'cmy'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'combine').__doc__

    CATEGORY = "MagickWand/Effects"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
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
    DESCRIPTION = getattr(Image, 'concat').__doc__

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
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
    DESCRIPTION = getattr(Image, 'contrast').__doc__

    CATEGORY = "MagickWand/Effects"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'contrast', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Crop:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'left': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'top': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'width': ('INT', {'default': 128, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 128, 'min': 1, 'max': 1024}), 'reset_coords': ('BOOLEAN', {'default': True})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'crop').__doc__

    CATEGORY = "MagickWand/Resizing and cropping"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'crop', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Decipher:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'passphrase': ('STRING', {'multiline': True})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'decipher').__doc__

    CATEGORY = "MagickWand/Cipher"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'decipher', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Deskew:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'threshold': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'deskew').__doc__

    CATEGORY = "MagickWand/Transformation"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'deskew', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Distort:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'method': (['undefined', 'affine', 'affine_projection', 'scale_rotate_translate', 'perspective', 'perspective_projection', 'bilinear_forward', 'bilinear_reverse', 'polynomial', 'arc', 'polar', 'depolar', 'cylinder_2_plane', 'plane_2_cylinder', 'barrel', 'barrel_inverse', 'shepards', 'resize', 'sentinel', 'rigidaffine'], {'default': 'affine'}), 'arguments': ('STRING', {'multiline': True}), 'best_fit': ('BOOLEAN', {'default': False}), 'filter': (['undefined', 'point', 'box', 'triangle', 'hermite', 'hanning', 'hamming', 'blackman', 'gaussian', 'quadratic', 'cubic', 'catrom', 'mitchell', 'jinc', 'sinc', 'sincfast', 'kaiser', 'welsh', 'parzen', 'bohman', 'bartlett', 'lagrange', 'lanczos', 'lanczossharp', 'lanczos2', 'lanczos2sharp', 'robidoux', 'robidouxsharp', 'cosine', 'spline', 'sentinel'], {'default': 'point'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'distort').__doc__

    CATEGORY = "MagickWand/Distortion"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
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
    DESCRIPTION = getattr(Image, 'edge').__doc__

    CATEGORY = "MagickWand/Effects"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
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
    DESCRIPTION = getattr(Image, 'emboss').__doc__

    CATEGORY = "MagickWand/Effects"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'emboss', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Encipher:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'passphrase': ('STRING', {'multiline': True})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'encipher').__doc__

    CATEGORY = "MagickWand/Cipher"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'encipher', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Equalize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'equalize').__doc__

    CATEGORY = "MagickWand/Effects"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'equalize', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Evaluate:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'operator': (['undefined', 'abs', 'add', 'addmodulus', 'and', 'cosine', 'divide', 'exponential', 'gaussiannoise', 'impulsenoise', 'laplaciannoise', 'leftshift', 'log', 'max', 'mean', 'median', 'min', 'multiplicativenoise', 'multiply', 'or', 'poissonnoise', 'pow', 'rightshift', 'rootmeansquare', 'set', 'sine', 'subtract', 'sum', 'thresholdblack', 'threshold', 'thresholdwhite', 'uniformnoise', 'xor', 'inverse_log'], {'default': 'abs'}), 'value': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'evaluate').__doc__

    CATEGORY = "MagickWand/Color Enhancement"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'evaluate', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Extent:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 128, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 128, 'min': 1, 'max': 1024}), 'x': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'y': ('INT', {'default': 0, 'min': 0, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'extent').__doc__

    CATEGORY = "MagickWand/Resizing and cropping"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'extent', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Function:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'function': (['undefined', 'arcsin', 'arctan', 'polynomial', 'sinusoid'], {'default': 'arcsin'}), 'arguments': ('STRING', {'multiline': True}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'function').__doc__

    CATEGORY = "MagickWand/Color Enhancement"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'function', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Gamma:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'adjustment_value': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'gamma').__doc__

    CATEGORY = "MagickWand/Color Enhancement"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'gamma', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Implode:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'amount': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'method': (['undefined', 'average', 'average9', 'average16', 'background', 'bilinear', 'blend', 'catrom', 'integer', 'mesh', 'nearest', 'spline'], {'default': 'average'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'implode').__doc__

    CATEGORY = "MagickWand/Distortion"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
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
    DESCRIPTION = getattr(Image, 'kmeans').__doc__

    CATEGORY = "MagickWand/Quantize"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
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
    DESCRIPTION = getattr(Image, 'kuwahara').__doc__

    CATEGORY = "MagickWand/Effects"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'kuwahara', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Level:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'black': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'white': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'gamma': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'level').__doc__

    CATEGORY = "MagickWand/Color Enhancement"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'level', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Levelize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'black': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'white': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'gamma': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'levelize').__doc__

    CATEGORY = "MagickWand/Color Enhancement"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'levelize', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Mode:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 128, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 128, 'min': 1, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'mode').__doc__

    CATEGORY = "MagickWand/Transformation"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
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
    DESCRIPTION = getattr(Image, 'modulate').__doc__

    CATEGORY = "MagickWand/Transformation"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'modulate', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Morphology:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'method': (['undefined', 'convolve', 'correlate', 'erode', 'dilate', 'erode_intensity', 'dilate_intensity', 'iterative_distance', 'open', 'close', 'open_intensity', 'close_intensity', 'smooth', 'edgein', 'edgeout', 'edge', 'tophat', 'bottom_hat', 'hit_and_miss', 'thinning', 'thicken', 'distance', 'voronoi'], {'default': 'convolve'}), 'kernel': (['undefined', 'unity', 'gaussian', 'dog', 'log', 'blur', 'comet', 'binomial', 'laplacian', 'sobel', 'frei_chen', 'roberts', 'prewitt', 'compass', 'kirsch', 'diamond', 'square', 'rectangle', 'octagon', 'disk', 'plus', 'cross', 'ring', 'peaks', 'edges', 'corners', 'diagonals', 'line_ends', 'line_junctions', 'ridges', 'convex_hull', 'thin_se', 'skeleton', 'chebyshev', 'manhattan', 'octagonal', 'euclidean', 'user_defined'], {'default': 'unity'}), 'iterations': ('INT', {'default': 1, 'min': 0, 'max': 1024}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'morphology').__doc__

    CATEGORY = "MagickWand/Morphology"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'morphology', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Negate:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'grayscale': ('BOOLEAN', {'default': False}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'negate').__doc__

    CATEGORY = "MagickWand/Effects"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'negate', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Noise:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'noise_type': (['undefined', 'uniform', 'gaussian', 'multiplicative_gaussian', 'impulse', 'laplacian', 'poisson', 'random'], {'default': 'uniform'}), 'attenuate': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'noise').__doc__

    CATEGORY = "MagickWand/Effects"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'noise', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Normalize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'normalize').__doc__

    CATEGORY = "MagickWand/Effects"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'normalize', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Polynomial:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'arguments': ('STRING', {'multiline': True})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'polynomial').__doc__

    CATEGORY = "MagickWand/Distortion"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
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
    DESCRIPTION = getattr(Image, 'posterize').__doc__

    CATEGORY = "MagickWand/Quantize"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'posterize', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Pseudo:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 128, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 128, 'min': 1, 'max': 1024}), 'pseudo': ('STRING', {'multiline': True})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'pseudo').__doc__

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'pseudo', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Quantize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'number_colors': ('INT', {'default': 16, 'min': 1, 'max': 1024}), 'colorspace_type': (['undefined', 'cmy', 'cmyk', 'gray', 'hcl', 'hclp', 'hsb', 'hsi', 'hsl', 'hsv', 'hwb', 'lab', 'lch', 'lchab', 'lchuv', 'log', 'lms', 'luv', 'ohta', 'rec601ycbcr', 'rec709ycbcr', 'rgb', 'scrgb', 'srgb', 'transparent', 'xyy', 'xyz', 'ycbcr', 'ycc', 'ydbdr', 'yiq', 'ypbpr', 'yuv'], {'default': 'cmy'}), 'treedepth': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'dither': (['undefined', 'no', 'riemersma', 'floyd_steinberg'], {'default': 'no'}), 'measure_error': ('BOOLEAN', {'default': False})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'quantize').__doc__

    CATEGORY = "MagickWand/Quantize"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'quantize', kwargs, type='whole')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Resample:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'x_res': ('FLOAT', {'default': 128, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'y_res': ('FLOAT', {'default': 128, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'filter': (['undefined', 'point', 'box', 'triangle', 'hermite', 'hanning', 'hamming', 'blackman', 'gaussian', 'quadratic', 'cubic', 'catrom', 'mitchell', 'jinc', 'sinc', 'sincfast', 'kaiser', 'welsh', 'parzen', 'bohman', 'bartlett', 'lagrange', 'lanczos', 'lanczossharp', 'lanczos2', 'lanczos2sharp', 'robidoux', 'robidouxsharp', 'cosine', 'spline', 'sentinel'], {'default': 'point'}), 'blur': ('FLOAT', {'default': 1, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'resample').__doc__

    CATEGORY = "MagickWand/Resizing and cropping"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'resample', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Resize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 128, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 128, 'min': 1, 'max': 1024}), 'filter': (['undefined', 'point', 'box', 'triangle', 'hermite', 'hanning', 'hamming', 'blackman', 'gaussian', 'quadratic', 'cubic', 'catrom', 'mitchell', 'jinc', 'sinc', 'sincfast', 'kaiser', 'welsh', 'parzen', 'bohman', 'bartlett', 'lagrange', 'lanczos', 'lanczossharp', 'lanczos2', 'lanczos2sharp', 'robidoux', 'robidouxsharp', 'cosine', 'spline', 'sentinel'], {'default': 'point'}), 'blur': ('FLOAT', {'default': 1, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'resize').__doc__

    CATEGORY = "MagickWand/Resizing and cropping"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
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
    DESCRIPTION = getattr(Image, 'roll').__doc__

    CATEGORY = "MagickWand/Transformation"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'roll', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Sample:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 128, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 128, 'min': 1, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'sample').__doc__

    CATEGORY = "MagickWand/Resizing and cropping"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'sample', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Scale:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'columns': ('INT', {'default': 1, 'min': 0, 'max': 1024}), 'rows': ('INT', {'default': 1, 'min': 0, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'scale').__doc__

    CATEGORY = "MagickWand/Distortion"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'scale', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Shade:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'gray': ('BOOLEAN', {'default': False}), 'azimuth': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'elevation': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'shade').__doc__

    CATEGORY = "MagickWand/Effects"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
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
    DESCRIPTION = getattr(Image, 'shadow').__doc__

    CATEGORY = "MagickWand/Effects"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'shadow', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Sharpen:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'sharpen').__doc__

    CATEGORY = "MagickWand/Effects"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'sharpen', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Shave:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'columns': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'rows': ('INT', {'default': 0, 'min': 0, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'shave').__doc__

    CATEGORY = "MagickWand/Resizing and cropping"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'shave', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Sketch:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'angle': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'sketch').__doc__

    CATEGORY = "MagickWand/Effects"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
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
    DESCRIPTION = getattr(Image, 'smush').__doc__

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'smush', kwargs, type='whole')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Solarize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'threshold': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'solarize').__doc__

    CATEGORY = "MagickWand/Effects"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'solarize', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Splice:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 128, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 128, 'min': 1, 'max': 1024}), 'x': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'y': ('INT', {'default': 0, 'min': 0, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'splice').__doc__

    CATEGORY = "MagickWand/Resizing and cropping"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
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
    DESCRIPTION = getattr(Image, 'spread').__doc__

    CATEGORY = "MagickWand/Effects"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'spread', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Statistic:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'stat': (['undefined', 'gradient', 'maximum', 'mean', 'median', 'minimum', 'mode', 'nonpeak', 'root_mean_square', 'standard_deviation'], {'default': 'gradient'}), 'width': ('INT', {'default': 128, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 128, 'min': 1, 'max': 1024}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'statistic').__doc__

    CATEGORY = "MagickWand/Transformation"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
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
    DESCRIPTION = getattr(Image, 'swirl').__doc__

    CATEGORY = "MagickWand/Effects"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'swirl', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Threshold:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'threshold': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'threshold').__doc__

    CATEGORY = "MagickWand/Threshold"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'threshold', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Thumbnail:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 128, 'min': 1, 'max': 1024}), 'height': ('INT', {'default': 128, 'min': 1, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'thumbnail').__doc__

    CATEGORY = "MagickWand/Resizing and cropping"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'thumbnail', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Transform:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'crop': ('STRING', {'multiline': True}), 'resize': ('STRING', {'multiline': True})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'transform').__doc__

    CATEGORY = "MagickWand/Resizing and cropping"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'transform', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Transparentize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'transparency': ('FLOAT', {'default': 0, 'min': 0.0, 'max': 1024, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'transparentize').__doc__

    CATEGORY = "MagickWand/Effects"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'transparentize', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )


class Vignette:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024, 'step': 0.01}), 'x': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'y': ('INT', {'default': 0, 'min': 0, 'max': 1024})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    DESCRIPTION = getattr(Image, 'vignette').__doc__

    CATEGORY = "MagickWand/Resizing and cropping"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
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
    DESCRIPTION = getattr(Image, 'wave').__doc__

    CATEGORY = "MagickWand/Effects"

    def execute(self, image, **kwargs):
        wand_img = to_wand_img(image)
        if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
        apply_to_wand_seq(wand_img, 'wave', kwargs, type='iterative')
        out = to_comfy_img(wand_img)
        wand_img.close()
        return (out, )

NODE_CLASS_MAPPINGS = {
    "ImageMagick Blur": Blur,
    "ImageMagick Canny": Canny,
    "ImageMagick Charcoal": Charcoal,
    "ImageMagick Chop": Chop,
    "ImageMagick Clahe": Clahe,
    "ImageMagick Clamp": Clamp,
    "ImageMagick Combine": Combine,
    "ImageMagick Concat": Concat,
    "ImageMagick Contrast": Contrast,
    "ImageMagick Crop": Crop,
    "ImageMagick Decipher": Decipher,
    "ImageMagick Deskew": Deskew,
    "ImageMagick Distort": Distort,
    "ImageMagick Edge": Edge,
    "ImageMagick Emboss": Emboss,
    "ImageMagick Encipher": Encipher,
    "ImageMagick Equalize": Equalize,
    "ImageMagick Evaluate": Evaluate,
    "ImageMagick Extent": Extent,
    "ImageMagick Function": Function,
    "ImageMagick Gamma": Gamma,
    "ImageMagick Implode": Implode,
    "ImageMagick Kmeans": Kmeans,
    "ImageMagick Kuwahara": Kuwahara,
    "ImageMagick Level": Level,
    "ImageMagick Levelize": Levelize,
    "ImageMagick Mode": Mode,
    "ImageMagick Modulate": Modulate,
    "ImageMagick Morphology": Morphology,
    "ImageMagick Negate": Negate,
    "ImageMagick Noise": Noise,
    "ImageMagick Normalize": Normalize,
    "ImageMagick Polynomial": Polynomial,
    "ImageMagick Posterize": Posterize,
    "ImageMagick Quantize": Quantize,
    "ImageMagick Resample": Resample,
    "ImageMagick Resize": Resize,
    "ImageMagick Roll": Roll,
    "ImageMagick Sample": Sample,
    "ImageMagick Scale": Scale,
    "ImageMagick Shade": Shade,
    "ImageMagick Shadow": Shadow,
    "ImageMagick Sharpen": Sharpen,
    "ImageMagick Shave": Shave,
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
    "ImageMagick Transparentize": Transparentize,
    "ImageMagick Vignette": Vignette,
    "ImageMagick Wave": Wave,
}
