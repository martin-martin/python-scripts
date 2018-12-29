from PIL import Image, ImageOps
from pathlib import Path


imgs = sorted(Path('./mun_fases').iterdir(), key=lambda f: f.stat().st_mtime)
print(len(imgs))


size = (640, 890)

leftright = size[1] - size[0]

num = 103
for i in imgs:
    img = Image.open(i)
    img_with_border = ImageOps.expand(img, border=(leftright, 0), fill='white')
    img_with_border.save(f'bordered/mun_fases_{num}.jpg')
    num -= 1
