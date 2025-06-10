# opencodex

This repository contains a simple **LiquidGlass** style image generator implemented in Python. The generator creates images similar to Apple's liquid glass aesthetic by layering translucent shapes over a gradient background and applying blur filters.

## Requirements

- Python 3.8+
- Pillow (`pip install pillow`)

## Usage

Generate a default image (512x512 pixels):

```bash
python3 liquidglass.py
```

You can customize the size, number of shapes, and output path:

```bash
python3 liquidglass.py --width 800 --height 600 --shapes 8 --output result.png
```

The generated image will be saved to the specified output path.
