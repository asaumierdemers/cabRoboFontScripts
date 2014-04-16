font = CurrentFont()

selection = font.selection

if len(selection) == 2:
        
    one, two = selection
    
    # save the current glyph order, including the template glyphs
    order = font.lib['public.glyphOrder']
    
    # swap unicodes
    uni1 = font[one].unicodes
    uni2 = font[two].unicodes
    font[one].unicodes, font[two].unicodes = uni2, uni1
    
    tmp = "temporaryName"
    # swap glyph names
    font.renameGlyph(one, tmp)
    font.renameGlyph(two, one)
    font.renameGlyph(tmp, two)
        
    # restore the glyph order
    a, b = order.index(one), order.index(two)
    order[a], order[b] = order[b], order[a]
    font.glyphOrder = order
        
    font.update()