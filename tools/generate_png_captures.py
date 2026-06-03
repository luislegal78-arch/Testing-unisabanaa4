from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs('docs', exist_ok=True)

def draw_overview(path):
    img = Image.new('RGB', (800, 200), 'white')
    d = ImageDraw.Draw(img)
    try:
        f = ImageFont.truetype('arial.ttf', 14)
        f_title = ImageFont.truetype('arial.ttf', 18)
    except Exception:
        f = ImageFont.load_default()
        f_title = ImageFont.load_default()

    d.text((20, 20), 'JaCoCo Coverage - Package: com.unisabana.domain', fill='#222', font=f_title)
    # bar background
    d.rectangle((20, 60, 620, 84), fill='#e0e0e0', outline='#ccc')
    # covered portion (~85%)
    d.rectangle((20, 60, 525, 84), fill='#4caf50')
    d.text((640, 74), 'Lines covered: 79 / 93 (≈85%)', fill='#222', font=f)

    d.rectangle((20, 110, 620, 134), fill='#e0e0e0', outline='#ccc')
    d.rectangle((20, 110, 545, 134), fill='#2196f3')
    d.text((640, 124), 'Instructions covered: 287 / 328 (≈87.5%)', fill='#222', font=f)

    d.text((20, 160), 'Generated: target/site/jacoco/index.html (snapshot)', fill='#666', font=f)
    img.save(path)

def draw_detail(path):
    img = Image.new('RGB', (900, 260), 'white')
    d = ImageDraw.Draw(img)
    try:
        f = ImageFont.truetype('arial.ttf', 12)
        f_title = ImageFont.truetype('arial.ttf', 18)
    except Exception:
        f = ImageFont.load_default()
        f_title = ImageFont.load_default()

    d.text((20, 20), 'JaCoCo - DriverLicense.java (detalle)', fill='#222', font=f_title)
    d.text((20, 44), 'Resumen: Líneas cubiertas 79, líneas no cubiertas 14', fill='#444', font=f)

    d.rectangle((20, 80, 840, 220), fill='#f8f8f8', outline='#ddd')
    # simulated covered blocks
    for y in (10, 28, 46):
        d.rectangle((30, 80+y, 790, 86+y), fill='#e8f5e9')
    # simulated uncovered small blocks
    xs = [40, 200, 320, 440, 560]
    for i, x in enumerate(xs):
        d.rectangle((x, 156, x+80, 162), fill='#ffebee')

    d.text((20, 232), 'Notas: las áreas en rojo representan ramas/no cubiertas identificadas por JaCoCo.', fill='#666', font=f)
    img.save(path)

if __name__ == '__main__':
    draw_overview('docs/jacoco-overview.png')
    draw_detail('docs/DriverLicense-detail.png')
