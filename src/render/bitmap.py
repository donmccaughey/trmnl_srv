from __future__ import annotations

import sys

from importlib import resources
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from PIL.ImageFont import FreeTypeFont
from utils import atomic_write

from .screen import Screen


BLACK = 0
ONE_BIT = '1'
WHITE = 1


def write_bitmap(screen: Screen, web_root: Path):
    image = Image.new(ONE_BIT, screen.size, color=WHITE)
    draw = ImageDraw.Draw(image)

    draw.rectangle(screen.rectangle, outline=BLACK, width=1)

    font = load_font(screen.cell_height)
    for j, line in enumerate(screen.grid):
        for i, ch in enumerate(line):
            x = i * screen.cell_width
            y = j * screen.cell_height
            draw.text((x, y), ch, fill=BLACK, font=font)

    atomic_write(
        web_root / 'content/bitmap/index.png',
        lambda f: image.save(f),
        is_binary=True
    )


def load_font(cell_height: int) -> FreeTypeFont | ImageFont:
    if package_name := __package__:
        with resources.path(package_name, 'AtkinsonHyperlegibleMono-Regular.otf') as font_path:
            return ImageFont.truetype(font_path, cell_height)
    else:
        sys.stderr.write('Unable to load font.\n')
        return ImageFont.load_default(size=cell_height - 1)
