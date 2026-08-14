#!/usr/bin/env python3
"""Generate brand PNG assets: og-image 1200x630 + apple-touch-icon 180x180."""
from PIL import Image, ImageDraw, ImageFont
import os

NAVY = (10, 17, 32)
NAVY2 = (13, 23, 48)
NAVY3 = (20, 33, 61)
GOLD = (212, 175, 55)
GOLD_BRIGHT = (240, 215, 138)
CREAM = (232, 238, 247)
MUTED = (143, 160, 184)

OUT = os.path.join(os.path.dirname(__file__), '..', 'public', 'images')
os.makedirs(OUT, exist_ok=True)

def vgrad(w, h, c1, c2):
    img = Image.new('RGB', (w, h))
    d = ImageDraw.Draw(img)
    for y in range(h):
        t = y / h
        d.line([(0, y), (w, y)], fill=tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3)))
    return img

def mountains(d, w, h, color, pts):
    d.polygon(pts, fill=color)

def find_font(size, bold=True):
    cands = [
        '/System/Library/Fonts/Supplemental/Arial Bold.ttf',
        '/System/Library/Fonts/Supplemental/Arial.ttf',
        '/Library/Fonts/Arial.ttf',
    ]
    for c in cands:
        if os.path.exists(c):
            try:
                return ImageFont.truetype(c, size)
            except Exception:
                pass
    return ImageFont.load_default()

def mono_font(size):
    cands = ['/System/Library/Fonts/Supplemental/Courier New.ttf', '/Library/Fonts/Courier New.ttf']
    for c in cands:
        if os.path.exists(c):
            try:
                return ImageFont.truetype(c, size)
            except Exception:
                pass
    return ImageFont.load_default()

# ============ OG IMAGE 1200x630 ============
W, H = 1200, 630
img = vgrad(W, H, NAVY, NAVY3)
d = ImageDraw.Draw(img)

# sun glow + disc
for r, a in [(190, 70), (150, 100), (110, 140)]:
    d.ellipse([940 - r, 240 - r, 940 + r, 240 + r], fill=(GOLD[0], GOLD[1], GOLD[2], a) if False else tuple(int(GOLD[i] * 0.55 + NAVY[i] * 0.45) for i in range(3)))
d.ellipse([890, 190, 990, 290], fill=GOLD_BRIGHT)
d.ellipse([900, 200, 980, 280], fill=GOLD)

# ridges
mountains(d, W, H, (16, 32, 56), [(0, 430), (240, 300), (420, 400), (640, 260), (860, 410), (1080, 300), (1200, 380), (1200, 630), (0, 630)])
mountains(d, W, H, NAVY, [(0, 520), (200, 420), (420, 500), (680, 390), (900, 510), (1120, 420), (1200, 470), (1200, 630), (0, 630)])

# PUN block
d.rounded_rectangle([70, 80, 290, 160], radius=10, fill=GOLD)
f = find_font(52)
d.text((180, 108), 'PUN', font=f, fill=NAVY, anchor='mm')

f2 = find_font(46)
d.text((70, 220), 'PT. PRIMA UTAMA NASIONAL', font=f2, fill=CREAM)
f3 = find_font(22)
d.text((70, 272), 'CONTRACTOR · MINING · TRADING', font=f3, fill=GOLD)
f4 = mono_font(19)
d.text((70, 330), 'Kontraktor pertambangan, eksplorasi hutan & konstruksi.', font=f4, fill=MUTED)
d.text((70, 358), 'Sejak 2023 — Kepuasan pelanggan, kebanggaan kami.', font=f4, fill=MUTED)

d.rectangle([70, 420, 1130, 423], fill=GOLD)
d.rounded_rectangle([70, 460, 250, 530], radius=8, fill=GOLD)
f5 = find_font(30)
d.text((160, 495), 'EST. 2023', font=f5, fill=NAVY, anchor='mm')

img.save(os.path.join(OUT, 'og-cover.png'))
print('og-cover.png saved')

# ============ APPLE TOUCH ICON 180x180 ============
S = 180
icon = vgrad(S, S, NAVY2, NAVY)
di = ImageDraw.Draw(icon)
di.polygon([(34, 130), (74, 68), (96, 102), (118, 56), (152, 130)], fill=GOLD)
di.rectangle([34, 136, 152, 152], fill=GOLD_BRIGHT)
icon.save(os.path.join(OUT, 'apple-touch-icon.png'))
print('apple-touch-icon.png saved')

# ============ FAVICON PNG 64x64 ============
F = 64
fav = vgrad(F, F, NAVY2, NAVY)
df = ImageDraw.Draw(fav)
df.polygon([(12, 46), (26, 24), (34, 36), (42, 20), (54, 46)], fill=GOLD)
df.rounded_rectangle([12, 48, 54, 53], radius=2, fill=GOLD_BRIGHT)
fav.save(os.path.join(OUT, 'favicon.png'))
print('favicon.png saved')
