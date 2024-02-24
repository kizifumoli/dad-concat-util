#!/usr/bin/env python3

import random
import argparse
from typing import Dict, Any, List
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
from pathlib import Path

def gen_random_color():
    return (random.randint(175, 255), random.randint(175, 255), random.randint(175, 255))

def create_numbered_images(n_colors: int, output_dir: Path):
    text_font = ImageFont.truetype(
        str(Path.home() / ".local/share/fonts/FiraCode-Regular.ttf"),
        50)

    ascent, descent = text_font.getmetrics()

    square_length = 200

    image_width = square_length
    image_height = square_length


    colors = [gen_random_color() for i in range(n_colors)]
    # Draw the color
    for color_index in range(n_colors):
        image = Image.new(mode="RGB", size=(image_width, image_height))
        draw = ImageDraw.Draw(image)

        color_coordinates = [(0, 0),
                             (square_length, square_length)]
        draw.rectangle(color_coordinates, colors[color_index])

        color_text = f"{color_index}"

        color_text_width = text_font.getlength(color_text)
        color_text_height = text_font.getmask(color_text).getbbox()[3] + descent

        text_coordinates = [
            int((square_length - color_text_width) / 2),
            int(((square_length - color_text_height) / 2)),
        ]

        draw.text(text_coordinates, color_text, (0, 0, 0), font_size = "10px", font=text_font)
        image.save(output_dir / f"{color_index}.jpg")
        print(f"Saved {output_dir / str(color_index)}.jpg")

def create_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_images", default=20, type=int, help="How many square images with numbers to generate")
    parser.add_argument("--output-dir", type=Path, help="Directory where the output image will be written to",
                        default=Path("/tmp/"))

    parser.set_defaults(func=lambda args: create_numbered_images(args.n_images, args.output_dir))

    return parser

def main():
    parser = create_argparser()
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
