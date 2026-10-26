"""Regenerate the UML SVG and PNG. Optional tooling: Python 3 + Pillow."""
from pathlib import Path
from html import escape
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
W, H = 1800, 1200
image = Image.new("RGB", (W, H), "#f4f7fb")
draw = ImageDraw.Draw(image)
svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
       '<rect width="1800" height="1200" fill="#f4f7fb"/>']
FONT = Path("C:/Windows/Fonts")
def font(size, bold=False):
    return ImageFont.truetype(str(FONT / ("arialbd.ttf" if bold else "arial.ttf")), size)
def text(x, y, value, size=22, bold=False, color="#24364b"):
    draw.text((x,y), value, font=font(size,bold), fill=color)
    svg.append(f'<text x="{x}" y="{y+size}" font-family="Arial, sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" fill="{color}">{escape(value)}</text>')
def line(points, color="#51647c", dashed=False, width=2):
    if dashed:
        for a,b in zip(points,points[1:]):
            dx,dy=b[0]-a[0],b[1]-a[1]
            length=(dx*dx+dy*dy)**0.5
            for start in range(0,int(length),14):
                end=min(start+8,length)
                draw.line([(a[0]+dx*start/length,a[1]+dy*start/length),
                           (a[0]+dx*end/length,a[1]+dy*end/length)],fill=color,width=width)
    else:
        draw.line(points,fill=color,width=width)
    coords=" ".join(f"{x},{y}" for x,y in points)
    dash=' stroke-dasharray="8 6"' if dashed else ""
    svg.append(f'<polyline points="{coords}" fill="none" stroke="{color}" stroke-width="{width}"{dash}/>')
def triangle(x,y):
    points=[(x,y),(x-12,y+22),(x+12,y+22)]
    draw.polygon(points,fill="white",outline="#51647c",width=2)
    svg.append(f'<polygon points="{x},{y} {x-12},{y+22} {x+12},{y+22}" fill="white" stroke="#51647c" stroke-width="2"/>')
def arrow(x,y,direction="right"):
    if direction=="right": line([(x-14,y-8),(x,y),(x-14,y+8)])
    elif direction=="up": line([(x-8,y+14),(x,y),(x+8,y+14)])
    else: line([(x-8,y-14),(x,y),(x+8,y-14)])
def box(x,y,w,title,fields,methods,stereo=None):
    header=78 if stereo else 56
    h=header+max(42,len(fields)*34+18)+len(methods)*34+24
    draw.rounded_rectangle((x,y,x+w,y+h),radius=8,fill="white",outline="#aebfd0",width=2)
    draw.rectangle((x+1,y+1,x+w-1,y+header),fill="#dce9f6")
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="white" stroke="#aebfd0" stroke-width="2"/>')
    svg.append(f'<path d="M{x+1} {y+header}V{y+8}Q{x+1} {y+1} {x+8} {y+1}H{x+w-8}Q{x+w-1} {y+1} {x+w-1} {y+8}V{y+header}Z" fill="#dce9f6"/>')
    if stereo:
        text(x+20,y+8,stereo,18)
        text(x+20,y+34,title,25,True)
    else: text(x+20,y+13,title,25,True)
    line([(x,y+header),(x+w,y+header)],"#aebfd0")
    fy=y+header+12
    for item in fields:
        text(x+18,fy,item,21);fy+=34
    sep=y+header+max(42,len(fields)*34+18)
    line([(x,sep),(x+w,sep)],"#aebfd0")
    for i,item in enumerate(methods): text(x+18,sep+12+i*34,item,21)
    return h

text(54,30,"CALCULATOR / STRATEGY PATTERN",34,True)
text(54,82,"Java 17  •  Option B  •  Core production classes",23)
# Main roles, with explicit method compartments.
box(60,170,630,"Calculator",["- strategy: OperationStrategy"],
    ["+ Calculator(strategy: OperationStrategy)",
     "+ setStrategy(strategy: OperationStrategy): void",
     "+ calculate(left: double, right: double): double"])
box(1000,170,690,"OperationStrategy",[],
    ["+ execute(left: double, right: double): double"],"«interface»")
# Context navigable association: exactly one stored strategy.
line([(690,240),(1000,240)]);arrow(1000,240)
text(762,200,"strategy",22)
text(965,245,"1",21)
# Concrete realization paths are separate until the shared interface bus.
for x in (320,900,1480):
    line([(x,638),(x,490),(1345,490),(1345,370)],dashed=True)
triangle(1345,348)
text(1140,446,"implements",21)
for x,name in ((60,"AddStrategy"),(640,"SubtractStrategy"),(1220,"MultiplyStrategy")):
    box(x,638,520,name,[],["+ execute(left: double,","    right: double): double"])
# Client dependency routing uses outer lanes, no node crossings.
box(60,960,630,"Client",["- Client()"],["+ main(args: String[]): void {static}"])
line([(60,1020),(28,1020),(28,270),(60,270)],dashed=True);arrow(60,270)
text(50,545,"creates / calls Context",20)
line([(690,1032),(1750,1032),(1750,900),(320,900)],dashed=True)
for x in (320,900,1480):
    line([(x,900),(x,828)],dashed=True);arrow(x,828,"up")
text(1180,1060,"creates concrete strategies",20)
text(60,1150,"+ public   - private   |   dashed triangle: realization   |   dashed arrow: dependency",20)
svg.append("</svg>")
(ROOT/"strategy-uml.svg").write_text("\n".join(svg),encoding="utf-8")
image.save(ROOT/"strategy-uml.png")
