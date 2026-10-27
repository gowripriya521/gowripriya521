"""Generate dark/light animated dot-portrait GitHub banners from assets/priya.jpeg.
Run: python generate_banner.py
Requires Pillow: python -m pip install Pillow
"""
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
from pathlib import Path
import random

ROOT = Path(__file__).parent
PHOTO = ROOT / 'assets' / 'priya.jpeg'
OUT = ROOT
W, H = 1180, 610
PANEL_X, PANEL_Y, PANEL_W, PANEL_H = 44, 118, 360, 430
random.seed(24)

def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def make_svg(dark=True):
    bg = '#0A101F' if dark else '#F8FAFC'
    panel = '#10192B' if dark else '#FFFFFF'
    fg = '#E2E8F0' if dark else '#0F172A'
    muted = '#94A3B8' if dark else '#64748B'
    portrait = '#A78BFA' if dark else '#7C3AED'
    cyan = '#22D3EE' if dark else '#0891B2'
    green = '#10B981'
    red = '#FB7185'
    im = Image.open(PHOTO).convert('RGB')
    # Preserve the entire source photo: contain it inside the dot grid instead of cropping/stretching.
    im.thumbnail((76, 92), Image.Resampling.LANCZOS)
    canvas = Image.new('RGB', (76, 92), (235, 235, 235))
    canvas.paste(im, ((76 - im.width) // 2, (92 - im.height) // 2))
    im = ImageOps.grayscale(canvas)
    im = ImageEnhance.Contrast(im).enhance(1.3)
    im = ImageOps.autocontrast(im, cutoff=1)
    im = im.filter(ImageFilter.UnsharpMask(radius=2, percent=120, threshold=3))
    dots=[]
    for y in range(im.height):
        for x in range(im.width):
            bright=im.getpixel((x,y))/255
            # brighter pixels have fewer/smaller dots; preserve portrait silhouette with density
            r = 1.0 + (1-bright)*1.5
            opacity = max(0.12, min(1, 1.1-bright*0.85))
            px=PANEL_X+35+x*3.65
            py=PANEL_Y+23+y*4.15
            delay=random.random()*2.0
            dots.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r:.2f}" fill="{portrait}" opacity="{opacity:.2f}"><animate attributeName="opacity" values="0.05;{opacity:.2f};{opacity:.2f}" dur="3.2s" begin="{delay:.2f}s" fill="freeze"/></circle>')
    dots='\n'.join(dots)
    rows=[('SUBJECT','Gaddam Gowri Priya'),('ROLE','Full-Stack Developer'),('ORIGIN','Bangulore, Madanapalle'),('EDUCATION','B.Tech'),('STATUS','BUILDING · LEARNING · SHIPPING'),('TOOLCHAIN','VS Code · Git · Python'),('CORE.LANG','Python · JavaScript'),('CORE.FRONTEND','HTML · CSS · JavaScript'),('CORE.BACKEND','FastAPI · Pydantic AI'),('CORE.INFRA','GitHub · Vercel')]
    info=[]
    y=190
    for label,value in rows:
        info.append(f'<text x="455" y="{y}" fill="{muted}" font-size="13" letter-spacing="1">{esc(label)}</text><path d="M 575 {y-4} H 700" stroke="{muted}" stroke-opacity=".45" stroke-dasharray="2 5"/><text x="720" y="{y}" fill="{fg}" font-size="14">{esc(value)}</text>')
        y += 28
    mode='DARK' if dark else 'LIGHT'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<title>Priya — animated GitHub profile banner ({mode.lower()} mode)</title>
<rect width="1180" height="610" rx="26" fill="{bg}"/>
<rect x="1" y="1" width="1178" height="608" rx="25" fill="none" stroke="{cyan}" stroke-opacity=".6"/>
<rect x="1" y="1" width="1178" height="52" rx="25" fill="{panel}"/><path d="M1 52H1179" stroke="{cyan}" stroke-opacity=".5"/>
<circle cx="27" cy="27" r="6" fill="#FB7185"/><circle cx="49" cy="27" r="6" fill="#FBBF24"/><circle cx="71" cy="27" r="6" fill="{green}"/>
<text x="590" y="33" text-anchor="middle" fill="{muted}" font-family="monospace" font-size="15">profile.sh --live</text>
<text x="42" y="88" fill="{cyan}" font-family="monospace" font-size="14" letter-spacing="2">VISUAL.MAP</text>
<rect x="32" y="101" width="384" height="462" rx="16" fill="{panel}" stroke="{portrait}" stroke-opacity=".8"/>
{dots}
<text x="455" y="90" fill="{cyan}" font-family="monospace" font-size="14" letter-spacing="2">SYSTEM.INFO</text>
<rect x="1030" y="69" width="104" height="29" rx="14" fill="{red}" fill-opacity=".15" stroke="{red}"/><circle cx="1047" cy="83" r="4" fill="{red}"><animate attributeName="opacity" values="1;.25;1" dur="1.2s" repeatCount="indefinite"/></circle><text x="1060" y="88" fill="{red}" font-family="monospace" font-size="12">LIVE</text>
{''.join(info)}
<g font-family="monospace" font-weight="700" font-size="24" text-anchor="middle">
  <text x="930" y="535" fill="{cyan}" opacity="0">PYTHON<animate attributeName="opacity" values="1;1;0;0;0;0;0;0;1" keyTimes="0;0.22;0.24;0.33;0.35;0.56;0.58;0.9;1" dur="8s" repeatCount="indefinite"/></text>
  <text x="930" y="535" fill="{green}" opacity="0">FASTAPI<animate attributeName="opacity" values="0;0;1;1;0;0;0" keyTimes="0;0.24;0.27;0.48;0.51;0.9;1" dur="8s" repeatCount="indefinite"/></text>
  <text x="930" y="535" fill="{portrait}" opacity="0">PYDANTIC<animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;0.5;0.54;0.82;1" dur="8s" repeatCount="indefinite"/></text>
</g>
<rect x="455" y="548" width="315" height="35" rx="17" fill="{portrait}" fill-opacity=".16" stroke="{portrait}"/><text x="612" y="570" text-anchor="middle" fill="{portrait}" font-family="monospace" font-size="15">@gowripriya521</text>
<text x="1135" y="584" text-anchor="end" fill="{muted}" font-family="monospace" font-size="11">{mode} MODE · ANIMATED SVG</text>
</svg>'''

for is_dark, name in [(True,'dark.svg'),(False,'light.svg')]:
    (OUT/name).write_text(make_svg(is_dark), encoding='utf-8')
print('Generated dark.svg and light.svg')
