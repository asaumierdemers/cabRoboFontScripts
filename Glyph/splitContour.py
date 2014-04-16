glyph = CurrentGlyph()

selection = glyph.selection

if len(selection) == 2:
    
    p1, p2 = selection
    
    contour = p1.getParent()
    
    if contour == p2.getParent():
        
        index = glyph.contours.index(contour)

        otherContours = glyph.contours
        otherContours.pop(index)
        
        glyph.prepareUndo("splitContour")
        
        copy = glyph.copy()
        copy.clear()
        pen = copy.getPointPen()
                
        path1 = []
        path2 = []
        
        paths = [path1, path2]
        
        i = 0
        for pt in contour.points:
            
            if pt.selected:
                paths[i].append(pt)
                i = not i

            paths[i].append(pt)

        for path in paths:
            pen.beginPath()
            for p in path:
                if p.type == "line" or p.type == "curve":
                    pen.addPoint((p.x, p.y), p.type, p.smooth)
                else:
                    pen.addPoint((p.x, p.y))
            pen.endPath()
        
        for c in otherContours:
            copy.appendContour(c)
                    
        glyph.clear()

        glyph.appendGlyph(copy)
                
        glyph.update()
        
        glyph.performUndo()
        
        