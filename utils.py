import numpy as np
import re
from wand.image import Image
import torch
import numbers
import json
import gc
import sys
from collections import deque

# Execution counter for periodic cleanup
_execution_count = 0

# Memory monitoring for debugging
_memory_history = deque(maxlen=100)
_enable_memory_logging = False  # Set to True to enable logging
_enable_aggressive_memory_compaction = False  # Set to True if experiencing memory fragmentation issues

# Configure ImageMagick resource limits on import
def _configure_imagemagick_limits():
    """Configure ImageMagick resource limits to prevent resource exhaustion"""
    try:
        from wand.resource import limits

        # Set generous but finite limits to prevent unbounded growth
        # These can be tuned based on your system
        limits['memory'] = 16 * 1024 * 1024 * 1024   # 16 GiB memory limit
        limits['map'] = 32 * 1024 * 1024 * 1024      # 32 GiB memory-mapped limit
        limits['disk'] = 64 * 1024 * 1024 * 1024     # 64 GiB disk limit
        limits['thread'] = 4                          # 4 threads max
        limits['time'] = 3600                         # 1 hour max operation time

        return True
    except Exception as e:
        print(f"Warning: Could not configure ImageMagick limits: {e}")
        return False

# Try to configure limits on module load
_imagemagick_configured = _configure_imagemagick_limits()

def get_memory_info():
    """Get basic memory information without external dependencies"""
    try:
        import psutil
        mem = psutil.virtual_memory()
        process = psutil.Process()
        return {
            'system_available_gb': mem.available / (1024**3),
            'system_used_pct': mem.percent,
            'process_rss_gb': process.memory_info().rss / (1024**3)
        }
    except ImportError:
        # Fallback without psutil - just get process memory
        import os
        if sys.platform == 'win32':
            try:
                import ctypes
                # Get process memory on Windows
                class PROCESS_MEMORY_COUNTERS(ctypes.Structure):
                    _fields_ = [
                        ('cb', ctypes.c_ulong),
                        ('PageFaultCount', ctypes.c_ulong),
                        ('PeakWorkingSetSize', ctypes.c_size_t),
                        ('WorkingSetSize', ctypes.c_size_t),
                        ('QuotaPeakPagedPoolUsage', ctypes.c_size_t),
                        ('QuotaPagedPoolUsage', ctypes.c_size_t),
                        ('QuotaPeakNonPagedPoolUsage', ctypes.c_size_t),
                        ('QuotaNonPagedPoolUsage', ctypes.c_size_t),
                        ('PagefileUsage', ctypes.c_size_t),
                        ('PeakPagefileUsage', ctypes.c_size_t),
                    ]

                counters = PROCESS_MEMORY_COUNTERS()
                counters.cb = ctypes.sizeof(PROCESS_MEMORY_COUNTERS)
                kernel32 = ctypes.windll.kernel32
                kernel32.K32GetProcessMemoryInfo(
                    kernel32.GetCurrentProcess(),
                    ctypes.byref(counters),
                    ctypes.sizeof(counters)
                )
                return {
                    'process_rss_gb': counters.WorkingSetSize / (1024**3),
                    'process_pagefile_gb': counters.PagefileUsage / (1024**3)
                }
            except:
                pass
        # Minimal fallback
        return {'available': True}

def print_imagemagick_diagnostics():
    """Print diagnostic information about ImageMagick resource usage"""
    try:
        from wand.resource import limits, resources

        print("\n=== ImageMagick Diagnostics ===")
        print("Resource Limits:")
        for key in ['memory', 'map', 'disk', 'thread', 'time', 'area', 'width', 'height']:
            try:
                print(f"  {key}: {limits.get(key, 'N/A')}")
            except:
                pass

        print("\nCurrent Resource Usage:")
        for key in ['memory', 'map', 'disk', 'thread', 'time', 'area']:
            try:
                print(f"  {key}: {resources.get(key, 'N/A')}")
            except:
                pass
        print("=" * 40 + "\n")
    except Exception as e:
        print(f"Could not get ImageMagick diagnostics: {e}")

def compact_process_memory():
    """Attempt to compact process memory and reduce working set (Windows only)"""
    global _enable_aggressive_memory_compaction

    # Only run if explicitly enabled
    if not _enable_aggressive_memory_compaction:
        return False

    if sys.platform != 'win32':
        return False

    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32

        # Get current process handle
        process_handle = kernel32.GetCurrentProcess()

        # Use gentler working set reduction
        # Don't use -1,-1 which can be too aggressive and cause paging issues
        # Instead, just trim the working set slightly
        kernel32.SetProcessWorkingSetSize(process_handle, 0xFFFFFFFF, 0xFFFFFFFF)

        # Skip EmptyWorkingSet - it's too aggressive and can cause issues
        # during other operations like model loading

        return True
    except Exception as e:
        return False

def log_memory_stats():
    """Log memory statistics if enabled"""
    global _memory_history, _enable_memory_logging, _execution_count

    if not _enable_memory_logging:
        return

    if _execution_count % 10 == 0:  # Log every 10 executions
        mem_info = get_memory_info()
        mem_info['execution_count'] = _execution_count
        _memory_history.append(mem_info)

        if _execution_count % 50 == 0:  # Print summary every 50 executions
            print(f"\n=== MagickWand Memory Stats (execution #{_execution_count}) ===")
            if 'process_rss_gb' in mem_info:
                print(f"  Process Memory: {mem_info['process_rss_gb']:.2f} GB")
            if 'system_available_gb' in mem_info:
                print(f"  System Available: {mem_info['system_available_gb']:.1f} GB ({mem_info['system_used_pct']:.1f}% used)")
            if 'process_pagefile_gb' in mem_info:
                print(f"  Process Pagefile: {mem_info['process_pagefile_gb']:.2f} GB")

            # Show trend if we have history
            if len(_memory_history) >= 5:
                recent = list(_memory_history)[-5:]
                if all('process_rss_gb' in m for m in recent):
                    trend = recent[-1]['process_rss_gb'] - recent[0]['process_rss_gb']
                    print(f"  Memory Trend (last 5 samples): {trend:+.3f} GB")
            print("=" * 55 + "\n")

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
    """Convert ComfyUI image to Wand with explicit cleanup"""
    img_batch_np = comfy_img.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
    img_wand = Image()
    try:
        for img_np in img_batch_np:
            # Create frame and add to sequence
            frame = Image.from_array(img_np)
            img_wand.sequence.append(frame)
            # Explicitly close the frame after it's added to sequence
            # The sequence holds its own reference, so this is safe
            frame.close()
            del frame
        return img_wand
    except Exception as e:
        # Cleanup on error
        img_wand.close()
        raise

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
    """Convert Wand image to ComfyUI format with aggressive resource cleanup"""
    global _execution_count
    out_imgs = []
    wand_img.iterator_reset()

    try:
        # Extract all frames with immediate cleanup using clone
        num_frames = len(wand_img.sequence)

        # Log large sequences
        if num_frames >= 50:
            print(f"Processing large sequence: {num_frames} frames ({num_frames * 1024 * 816 * 3 * 4 / (1024**2):.1f} MB estimated)")

        for sub_idx in range(num_frames):
            # Clone the frame to get independent copy, then immediately convert
            # This ensures the Wand C-level memory is released as soon as possible
            with wand_img.sequence[sub_idx].clone() as frame_clone:
                # Force copy to ensure NumPy array is independent of Wand memory
                frame_array = np.array(frame_clone, copy=True)
                out_imgs.append(HWC3(frame_array))
                del frame_array

            # Periodic quick cleanup during large batches to prevent accumulation
            if sub_idx > 0 and sub_idx % 10 == 0:
                gc.collect(generation=0)  # Quick gen-0 collection only

        # Stack into uint8 array
        out_imgs_uint8 = np.stack(out_imgs)

        # Explicitly delete the list to free memory before large allocation
        del out_imgs
        gc.collect(generation=0)  # Quick cleanup before big allocation

        # Convert to float32 - use in-place operations to avoid extra copy
        # Pre-allocate float32 array to avoid astype creating a copy
        out_imgs_float = np.empty(out_imgs_uint8.shape, dtype=np.float32)
        np.divide(out_imgs_uint8, 255.0, out=out_imgs_float)

        # Delete uint8 array immediately after conversion
        del out_imgs_uint8

        # Convert to torch tensor
        result = torch.from_numpy(out_imgs_float)

        # Delete numpy array after torch conversion (torch may hold reference)
        del out_imgs_float

        # Increment execution counter and do periodic full cleanup
        _execution_count += 1

        # For large batches (30+ frames), do aggressive cleanup
        if num_frames >= 30:
            gc.collect()  # Full GC for large batches
            compact_process_memory()  # Compact memory on Windows

        # Periodic cleanup even for small batches
        if _execution_count % 50 == 0:
            gc.collect()  # Full collection every 50 executions
            compact_process_memory()  # Periodic memory compaction

        return result
    except Exception as e:
        # Ensure cleanup even on exception
        out_imgs = None
        gc.collect()

        # Print diagnostics on memory errors
        if 'memory' in str(e).lower() or 'allocate' in str(e).lower():
            print(f"\n!!! Memory error encountered after {_execution_count} executions !!!")
            print(f"Error: {e}")
            print_imagemagick_diagnostics()
            mem_info = get_memory_info()
            if 'process_rss_gb' in mem_info:
                print(f"Process memory: {mem_info['process_rss_gb']:.2f} GB")
            if 'system_available_gb' in mem_info:
                print(f"System available: {mem_info['system_available_gb']:.1f} GB\n")

        raise

def safe_wand_execute(image, method_name, kwargs, apply_type='iterative'):
    """
    Wrapper for safe Wand image execution with guaranteed cleanup.

    This ensures that Wand Image objects are always properly closed,
    even if exceptions occur during processing. This prevents C-level
    ImageMagick memory leaks that can accumulate over time.

    Args:
        image: ComfyUI image tensor
        method_name: String name of the Wand Image method to apply
        kwargs: Keyword arguments for the method
        apply_type: 'iterative' or 'whole' - how to apply the method

    Returns:
        Tuple containing the processed image
    """
    wand_img = None
    try:
        # Convert to Wand format
        wand_img = to_wand_img(image)

        # Preprocess arguments
        kwargs = preprocess_kwargs(**kwargs)

        # Apply the ImageMagick operation
        apply_to_wand_seq(wand_img, method_name, kwargs, type=apply_type)

        # Convert back to ComfyUI format
        out = to_comfy_img(wand_img)

        # Log memory stats if enabled
        log_memory_stats()

        return (out, )
    finally:
        # Ensure cleanup happens even on exception
        if wand_img is not None:
            try:
                # Clear the sequence to release frame references
                while len(wand_img.sequence) > 0:
                    try:
                        wand_img.sequence.pop().close()
                    except:
                        pass  # Best effort cleanup

                # Close the main image
                wand_img.close()
            except:
                pass  # Best effort cleanup

            # Explicitly delete the reference
            del wand_img

        # Quick cleanup to release resources promptly
        gc.collect(generation=0)

def preprocess_kwargs(**kwargs):
    if "arguments" in kwargs:
            kwargs["arguments"] = [float(x.strip()) for x in remove_comments(kwargs["arguments"]).split(',') if x.strip()]
    if "matrix" in kwargs:
        list_of_lists = json.loads(kwargs["matrix"])
        kwargs["matrix"] = [[float(element) for element in sublist] for sublist in list_of_lists]
    return kwargs
