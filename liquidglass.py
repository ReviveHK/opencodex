import random
from PIL import Image, ImageDraw, ImageFilter


def generate_liquid_glass(width=512, height=512, shapes=5, output="liquidglass.png"):
    """Generate a LiquidGlass style image.

    Parameters
    ----------
    width: int
        Width of the output image.
    height: int
        Height of the output image.
    shapes: int
        Number of translucent shapes to draw.
    output: str
        Path to save the generated image.
    """

    # Create gradient background
    img = Image.new("RGBA", (width, height))
    draw = ImageDraw.Draw(img)
    for y in range(height):
        r = int(127 + 128 * y / height)
        g = int(127 + 128 * (height - y) / height)
        b = 255
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    o_draw = ImageDraw.Draw(overlay)

    for _ in range(shapes):
        radius = random.randint(width // 8, width // 3)
        x = random.randint(0, width)
        y = random.randint(0, height)
        color = (
            random.randint(150, 255),
            random.randint(150, 255),
            random.randint(150, 255),
            random.randint(100, 180),
        )
        bbox = [
            (x - radius, y - radius),
            (x + radius, y + radius),
        ]
        o_draw.ellipse(bbox, fill=color)

    overlay = overlay.filter(ImageFilter.GaussianBlur(radius=25))
    img = Image.alpha_composite(img, overlay)
    img = img.filter(ImageFilter.GaussianBlur(radius=1))
    img.save(output)
    print(f"Saved {output}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate a LiquidGlass style image")
    parser.add_argument("--width", type=int, default=512, help="image width")
    parser.add_argument("--height", type=int, default=512, help="image height")
    parser.add_argument("--shapes", type=int, default=5, help="number of shapes")
    parser.add_argument("--output", type=str, default="liquidglass.png", help="output file")
    args = parser.parse_args()

    generate_liquid_glass(
        width=args.width,
        height=args.height,
        shapes=args.shapes,
        output=args.output,
    )
