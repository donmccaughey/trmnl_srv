import json
import sys

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


def write_at(draw, x, y, text):
    draw.text((x, y), text, fill=0, font=font)


print('Rendering...')

content_dir = Path('../tmp')
content_dir.mkdir(parents=True, exist_ok=True)
content_file = content_dir / 'content.json'
with content_file.open('r') as f:
    content = json.load(f)

width, height = 800, 480
image = Image.new('1', (width, height), color=1)
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

write_at(draw, 20, 20, 'Hello, TRMNL!')
write_at(draw, 20, 40, content['updated'])

image_dir = Path('../tmp')
image_dir.mkdir(parents=True, exist_ok=True)
image_file = image_dir / 'content.bmp'
image.save(image_file)

sys.exit(0)
