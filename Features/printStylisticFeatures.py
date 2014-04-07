font = CurrentFont()

stylisticGlyphNames = [name for name in font.keys() if ".ss" in name]

# make a unique list of the suffix 2 digits
stylisticSets = sorted(set([n[-2:] for n in stylisticGlyphNames]))

for ss in stylisticSets:
    
    glyphSet = sorted([name for name in stylisticGlyphNames if ss in name])
    
    feature = "ss" + ss
    print "features %s {" % feature
    for glyph in glyphSet:
        baseGlyph = glyph.split("."+feature)[0]
        print "\tsub %s by %s;" % (baseGlyph, glyph)
    print "} %s;" % feature
    print