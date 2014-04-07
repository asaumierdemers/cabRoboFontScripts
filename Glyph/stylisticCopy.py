font = CurrentFont()
glyph = CurrentGlyph()

name = glyph.name.split(".")[0]

others = [n for n in font.keys() if n.startswith(str(name+'.ss'))]

otherNumbers = sorted([n.split(".ss")[1] for n in others])

missingNumber = None
for i, n in enumerate(otherNumbers, 1):
    if i != int(n):
        missingNumber = i
        break

if missingNumber:
    number = missingNumber
else:
    number = len(others) + 1

newName = name + '.ss' + str(number).zfill(2)

font.insertGlyph(glyph, name=newName)

font.update()