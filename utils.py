import numpy as np
import re
from wand.image import Image
import torch
import numbers
import json

def HWC3(x):
    assert x.dtype == np.uint8
    if x.ndim == 2:
        x = x[:, :, None]
    assert x.ndim == 3
    H, W, C = x.shape
    assert C == 1 or C == 3 or C == 4
    if C == 3:
        return x
    if C == 1:
        return np.concatenate([x, x, x], axis=2)
    if C == 4:
        color = x[:, :, 0:3].astype(np.float32)
        alpha = x[:, :, 3:4].astype(np.float32) / 255.0
        y = color * alpha + 255.0 * (1.0 - alpha)
        y = y.clip(0, 255).astype(np.uint8)
        return y

def remove_comments(string):
    pattern = r"#.*$"
    regex = re.compile(pattern, re.MULTILINE)
    return regex.sub("", string)

def to_wand_img(comfy_img):
    img_batch_np = comfy_img.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
    img_wand = Image()
    for img_np in img_batch_np:
        img_wand.sequence.append(Image.from_array(img_np))
    return img_wand

def check_iterable(key, value, idx=0):
    return key != "arguments" and hasattr(value, '__getitem__') and isinstance(value[0], numbers.Number)

def safe_index(list, value):
    return list[value] if value < len(list) else list[-1]

def apply_to_wand_seq(wand_img, method, method_kwargs, type="iterative"):
    wand_img.iterator_reset()
    if type == "iterative":
        for sub_idx in range(len(wand_img.sequence)):
            _kwargs = {
                key: safe_index(value, sub_idx)
                    if check_iterable(key, value) else value
                    for key, value in method_kwargs.items()
            }
            with wand_img.sequence[sub_idx] as frame:
                getattr(frame, method)(**_kwargs)
    elif type == "whole":
        _kwargs = {key: value[0] if check_iterable(key, value) else value for key, value in method_kwargs.items()}
        getattr(wand_img, method)(**_kwargs)
        wand_img.sequence = wand_img.sequence[:1]
    else:
        raise NotImplementedError(type)
    return wand_img

def to_comfy_img(wand_img):
    out_imgs = []
    wand_img.iterator_reset()
    for sub_idx in range(len(wand_img.sequence)):
        frame = wand_img.sequence[sub_idx]
        out_imgs.append(HWC3(np.array(frame)))
    out_imgs = np.stack(out_imgs)
    out_imgs = torch.from_numpy(out_imgs.astype(np.float32) / 255.)
    return out_imgs

def preprocess_kwargs(**kwargs):
    if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
    if "matrix" in kwargs:
        list_of_lists = json.loads(kwargs["matrix"])
        kwargs["matrix"] = [[float(element) for element in sublist] for sublist in list_of_lists]
    return kwargs
