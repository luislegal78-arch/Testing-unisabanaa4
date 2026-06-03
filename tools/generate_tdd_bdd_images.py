from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs('docs', exist_ok=True)

# Dibuja un diagrama simple del ciclo TDD (Rojo-Verde-Refactor)
def draw_tdd_cycle(path):
    img = Image.new('RGB', (900, 300), 'white')
    d = ImageDraw.Draw(img)
    try:
        f_title = ImageFont.truetype('arial.ttf', 22)
        f = ImageFont.truetype('arial.ttf', 14)
    except Exception:
        f_title = ImageFont.load_default()
        f = ImageFont.load_default()

    d.text((20, 20), 'Ciclo TDD - Rojo / Verde / Refactor', fill='#111', font=f_title)

    # Cajas
    boxes = [
        (50, 80, 260, 180, 'Rojo\n(Escribir test que falla)', '#e57373'),
        (330, 80, 540, 180, 'Verde\n(Hacer el mínimo para pasar)', '#81c784'),
        (610, 80, 820, 180, 'Refactor\n(Limpiar sin romper)', '#64b5f6')
    ]

    for x1, y1, x2, y2, text, color in boxes:
        d.rectangle((x1, y1, x2, y2), fill=color, outline='#333')
        # centrar texto
        lines = text.split('\n')
        ty = y1 + 20
        for line in lines:
            w, h = d.textsize(line, font=f)
            d.text(((x1+x2-w)/2, ty), line, fill='#111', font=f)
            ty += h + 4

    # Flechas
    d.line((260, 130, 330, 130), fill='#333', width=3)
    d.polygon([(328,125),(338,130),(328,135)], fill='#333')
    d.line((540, 130, 610, 130), fill='#333', width=3)
    d.polygon([(608,125),(618,130),(608,135)], fill='#333')
    # Flecha de retorno
    d.line((830, 140, 450, 230), fill='#333', width=2)
    d.polygon([(454,226),(450,236),(444,227)], fill='#333')

    d.text((20, 240), 'Notas: Repetir ciclo hasta cumplir la especificación.', fill='#333', font=f)
    img.save(path)

# Dibuja una imagen ilustrativa con ejemplos BDD
def draw_bdd_scenarios(path):
    img = Image.new('RGB', (900, 380), 'white')
    d = ImageDraw.Draw(img)
    try:
        f_title = ImageFont.truetype('arial.ttf', 20)
        f = ImageFont.truetype('arial.ttf', 14)
    except Exception:
        f_title = ImageFont.load_default()
        f = ImageFont.load_default()

    d.text((20, 20), 'Escenarios BDD - Given / When / Then', fill='#111', font=f_title)

    scenarios = [
        ('Given: solicitante 15 años', 'When: solicita licencia', 'Then: rechazado'),
        ('Given: solicitante 16 años', 'When: solicita licencia restringida', 'Then: aceptado (restringido)'),
        ('Given: solicitante 22 años', 'When: solicita licencia pública', 'Then: rechazado (edad mínima 23)')
    ]

    y = 70
    for g, w, t in scenarios:
        d.rectangle((40, y, 860, y+80), fill='#f5f5f5', outline='#ddd')
        d.text((60, y+8), g, fill='#1b5e20', font=f)
        d.text((60, y+30), w, fill='#0d47a1', font=f)
        d.text((60, y+52), t, fill='#b71c1c', font=f)
        y += 100

    d.text((20, 340), 'Consejo: escribir escenarios BDD legibles y automáticos para facilitar aceptación.', fill='#333', font=f)
    img.save(path)

if __name__ == '__main__':
    draw_tdd_cycle('docs/tdd-cycle.png')
    draw_bdd_scenarios('docs/bdd-scenarios.png')
