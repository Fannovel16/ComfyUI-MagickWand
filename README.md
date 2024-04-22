# ComfyUI MagickWand
Proper implementation of ImageMagick - the famous software suite for editing and manipulating digital images to ComfyUI using [wandpy](https://github.com/emcconville/wand)
## Example workflow
* [magickwand_playground.json](./magickwand_playground.json)
* [Input image 1](./000002.jpg), [Input image 2](./015316.jpg)
![](./example_image.png)
## Installation
### Install ImageMagick on your system
#### Install ImageMagick on Windows
* Windows 32-bit: https://imagemagick.org/archive/binaries/ImageMagick-7.1.1-30-Q16-HDRI-x86-dll.exe
* Windows 64-bit: https://imagemagick.org/archive/binaries/ImageMagick-7.1.1-30-Q16-HDRI-x64-dll.exe

For other CPU architectures, please download dynamic builds (ones have "dll" in name). A static or portable build won't work as it doesn't have necessary DLL files
#### Install ImageMagick on Debian/Ubuntu
If you’re using Linux distributions based on Debian like Ubuntu, it can be easily installed using APT:
```sh
sudo apt-get install libmagickwand-dev
```
#### Install ImageMagick on Fedora/CentOS
If you’re using Linux distributions based on Redhat like Fedora or CentOS, it can be installed using Yum:
```sh
yum update
yum install ImageMagick-devel
```
#### Install ImageMagick on Mac
You need one of Homebrew or MacPorts to install ImageMagick.

Homebrew:
```sh
brew install imagemagick
```
MacPorts:
```sh
sudo port install imagemagick
```
If your Python in not installed using MacPorts, you have to export MAGICK_HOME path as well. Because Python that is not installed using MacPorts doesn’t look up /opt/local, the default path prefix of MacPorts packages.
```sh
export MAGICK_HOME=/opt/local
```
### Install custom node suite
There are two ways:
1. Through [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
2. Run the following command, assuming your terminal is already in ComfyUI folder:
```
cd custom_nodes
git clone https://github.com/Fannovel16/ComfyUI-MagickWand
pip install -r requirements.txt
```
## Supported methods (99)
* ImageMagick Adaptive Blur: [adaptive_blur](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.adaptive_blur)
* ImageMagick Adaptive Resize: [adaptive_resize](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.adaptive_resize)
* ImageMagick Adaptive Sharpen: [adaptive_sharpen](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.adaptive_sharpen)
* ImageMagick Adaptive Threshold: [adaptive_threshold](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.adaptive_threshold)
* ImageMagick Auto Gamma: [auto_gamma](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.auto_gamma)
* ImageMagick Auto Level: [auto_level](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.auto_level)
* ImageMagick Auto Orient: [auto_orient](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.auto_orient)
* ImageMagick Auto Threshold: [auto_threshold](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.auto_threshold)
* ImageMagick Blue Shift: [blue_shift](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.blue_shift)
* ImageMagick Blur: [blur](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.blur)
* ImageMagick Brightness Contrast: [brightness_contrast](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.brightness_contrast)
* ImageMagick Canny: [canny](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.canny)
* ImageMagick Charcoal: [charcoal](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.charcoal)
* ImageMagick Chop: [chop](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.chop)
* ImageMagick Clahe: [clahe](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.clahe)
* ImageMagick Clamp: [clamp](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.clamp)
* ImageMagick Coalesce: [coalesce](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.coalesce)
* ImageMagick Color Decision List: [color_decision_list](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.color_decision_list)
* ImageMagick Color Matrix: [color_matrix](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.color_matrix)
* ImageMagick Combine: [combine](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.combine)
* ImageMagick Concat: [concat](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.concat)
* ImageMagick Contrast: [contrast](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.contrast)
* ImageMagick Contrast Stretch: [contrast_stretch](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.contrast_stretch)
* ImageMagick Crop: [crop](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.crop)
* ImageMagick Cycle Color Map: [cycle_color_map](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.cycle_color_map)
* ImageMagick Decipher: [decipher](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.decipher)
* ImageMagick Despeckle: [despeckle](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.despeckle)
* ImageMagick Distort: [distort](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.distort)
* ImageMagick Edge: [edge](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.edge)
* ImageMagick Emboss: [emboss](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.emboss)
* ImageMagick Encipher: [encipher](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.encipher)
* ImageMagick Enhance: [enhance](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.enhance)
* ImageMagick Equalize: [equalize](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.equalize)
* ImageMagick Evaluate: [evaluate](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.evaluate)
* ImageMagick Extent: [extent](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.extent)
* ImageMagick Flip: [flip](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.flip)
* ImageMagick Flop: [flop](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.flop)
* ImageMagick Forward Fourier Transform: [forward_fourier_transform](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.forward_fourier_transform)
* ImageMagick Function: [function](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.function)
* ImageMagick Gamma: [gamma](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.gamma)
* ImageMagick Gaussian Blur: [gaussian_blur](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.gaussian_blur)
* ImageMagick Hough Lines: [hough_lines](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.hough_lines)
* ImageMagick Implode: [implode](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.implode)
* ImageMagick Kmeans: [kmeans](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.kmeans)
* ImageMagick Kuwahara: [kuwahara](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.kuwahara)
* ImageMagick Level: [level](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.level)
* ImageMagick Levelize: [levelize](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.levelize)
* ImageMagick Linear Stretch: [linear_stretch](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.linear_stretch)
* ImageMagick Liquid Rescale: [liquid_rescale](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.liquid_rescale)
* ImageMagick Local Contrast: [local_contrast](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.local_contrast)
* ImageMagick Magnify: [magnify](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.magnify)
* ImageMagick Mean Shift: [mean_shift](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.mean_shift)
* ImageMagick Merge Layers: [merge_layers](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.merge_layers)
* ImageMagick Mode: [mode](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.mode)
* ImageMagick Modulate: [modulate](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.modulate)
* ImageMagick Morphology: [morphology](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.morphology)
* ImageMagick Motion Blur: [motion_blur](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.motion_blur)
* ImageMagick Negate: [negate](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.negate)
* ImageMagick Noise: [noise](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.noise)
* ImageMagick Normalize: [normalize](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.normalize)
* ImageMagick Oil Paint: [oil_paint](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.oil_paint)
* ImageMagick Ordered Dither: [ordered_dither](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.ordered_dither)
* ImageMagick Polynomial: [polynomial](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.polynomial)
* ImageMagick Posterize: [posterize](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.posterize)
* ImageMagick Quantize: [quantize](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.quantize)
* ImageMagick Random Threshold: [random_threshold](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.random_threshold)
* ImageMagick Range Threshold: [range_threshold](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.range_threshold)
* ImageMagick Resample: [resample](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.resample)
* ImageMagick Resize: [resize](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.resize)
* ImageMagick Roll: [roll](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.roll)
* ImageMagick Rotational Blur: [rotational_blur](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.rotational_blur)
* ImageMagick Sample: [sample](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.sample)
* ImageMagick Scale: [scale](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.scale)
* ImageMagick Selective Blur: [selective_blur](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.selective_blur)
* ImageMagick Sepia Tone: [sepia_tone](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.sepia_tone)
* ImageMagick Shade: [shade](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.shade)
* ImageMagick Shadow: [shadow](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.shadow)
* ImageMagick Sharpen: [sharpen](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.sharpen)
* ImageMagick Shave: [shave](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.shave)
* ImageMagick Sigmoidal Contrast: [sigmoidal_contrast](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.sigmoidal_contrast)
* ImageMagick Sketch: [sketch](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.sketch)
* ImageMagick Smush: [smush](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.smush)
* ImageMagick Solarize: [solarize](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.solarize)
* ImageMagick Splice: [splice](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.splice)
* ImageMagick Spread: [spread](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.spread)
* ImageMagick Statistic: [statistic](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.statistic)
* ImageMagick Swirl: [swirl](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.swirl)
* ImageMagick Threshold: [threshold](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.threshold)
* ImageMagick Thumbnail: [thumbnail](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.thumbnail)
* ImageMagick Transform: [transform](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.transform)
* ImageMagick Transform Colorspace: [transform_colorspace](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.transform_colorspace)
* ImageMagick Transparentize: [transparentize](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.transparentize)
* ImageMagick Transpose: [transpose](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.transpose)
* ImageMagick Transverse: [transverse](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.transverse)
* ImageMagick Unsharp Mask: [unsharp_mask](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.unsharp_mask)
* ImageMagick Vignette: [vignette](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.vignette)
* ImageMagick Wave: [wave](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.wave)
* ImageMagick Wavelet Denoise: [wavelet_denoise](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.wavelet_denoise)
* ImageMagick White Balance: [white_balance](https://docs.wand-py.org/en/0.6.12/wand/image.html#wand.image.BaseImage.white_balance)