# ComfyUI MagickWand
Proper implementation of ImageMagick - the famous software suite for editing and manipulating digital images to ComfyUI using [wandpy](https://github.com/emcconville/wand)
## Example workflow
[magickwand_playground.json](./magickwand_playground.json)
![](./example_image.png)
## Installation
### Install ImageMagick on Windows
* Windows 32-bit: https://imagemagick.org/archive/binaries/ImageMagick-7.1.1-30-Q16-HDRI-x86-dll.exe
* Windows 64-bit: https://imagemagick.org/archive/binaries/ImageMagick-7.1.1-30-Q16-HDRI-x64-dll.exe

For other CPU architectures, please download dynamic builds (ones have "file" in filename). A static or portable build won't work as it doesn't have necessary DLL files
### Install ImageMagick on Debian/Ubuntu
If you’re using Linux distributions based on Debian like Ubuntu, it can be easily installed using APT:
```sh
sudo apt-get install libmagickwand-dev
```
### Install ImageMagick on Fedora/CentOS
If you’re using Linux distributions based on Redhat like Fedora or CentOS, it can be installed using Yum:
```sh
yum update
yum install ImageMagick-devel
```
### Install ImageMagick on Mac
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
## Supported methods (58)
* ImageMagick Blur
* ImageMagick Canny
* ImageMagick Charcoal
* ImageMagick Chop
* ImageMagick Clahe
* ImageMagick Clamp
* ImageMagick Combine
* ImageMagick Concat
* ImageMagick Contrast
* ImageMagick Crop
* ImageMagick Decipher
* ImageMagick Deskew
* ImageMagick Distort
* ImageMagick Edge
* ImageMagick Emboss
* ImageMagick Encipher
* ImageMagick Equalize
* ImageMagick Evaluate
* ImageMagick Extent
* ImageMagick Function
* ImageMagick Gamma
* ImageMagick Implode
* ImageMagick Kmeans
* ImageMagick Kuwahara
* ImageMagick Level
* ImageMagick Levelize
* ImageMagick Mode
* ImageMagick Modulate
* ImageMagick Morphology
* ImageMagick Negate
* ImageMagick Noise
* ImageMagick Normalize
* ImageMagick Polynomial
* ImageMagick Posterize
* ImageMagick Pseudo
* ImageMagick Quantize
* ImageMagick Resample
* ImageMagick Resize
* ImageMagick Roll
* ImageMagick Sample
* ImageMagick Scale
* ImageMagick Shade
* ImageMagick Shadow
* ImageMagick Sharpen
* ImageMagick Shave
* ImageMagick Sketch
* ImageMagick Smush
* ImageMagick Solarize
* ImageMagick Splice
* ImageMagick Spread
* ImageMagick Statistic
* ImageMagick Swirl
* ImageMagick Threshold
* ImageMagick Thumbnail
* ImageMagick Transform
* ImageMagick Transparentize
* ImageMagick Vignette
* ImageMagick Wave