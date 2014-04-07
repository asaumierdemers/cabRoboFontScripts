import math

pt = 2
gap = 10

f = CurrentFont()

baseline = 0
descender = f.info.descender
xHeight = f.info.xHeight
capHeight = f.info.capHeight
ascender = f.info.ascender
angle = f.info.italicAngle

metrics = [baseline, descender, xHeight, capHeight, ascender]

g = f.newGlyph("fontmetrics")

p = g.getPen()
g.width = w = 500

if not angle:
    angle = 0

a = math.radians(angle)

# robofont negative angle
a = -a

for m in metrics:
    
    offset = math.tan(a) * m
    
    p.moveTo((gap+offset, m))
    p.lineTo((gap+offset, m+pt))
    p.lineTo((w+offset, m+pt))
    p.lineTo((w+offset, m))
    p.closePath()