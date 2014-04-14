from fontTools.misc.bezierTools import splitCubicAtT
import math

offset = 20
t = 1.1

def getOffset(offset, (x1, y1), (x2, y2)):
    
    length = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    ox = (x2-x1)/length*offset
    oy = (y2-y1)/length*offset
    
    return int(round(ox)), int(round(oy))


def offsetSegment(prevSegment, segment, reverse=False):
    
    if segment.type == "line":
        
        if reverse:
            prevSegment, segment = segment, prevSegment
        
        p1 = prevSegment.onCurve
        p2 = segment.onCurve
                
        x1, y1 = p1.x, p1.y
        x2, y2 = p2.x, p2.y
        
        ox, oy = getOffset(offset, (x1, y1), (x2, y2))

        segment.move((ox, oy))
    
    if segment.type == "curve":
        
        p1 = prevSegment.onCurve
        p2, p3 = segment.offCurve
        p4 = segment.onCurve
        
        if reverse:
            p1, p2, p3, p4 = p4, p3, p2, p1
                
        p1 = p1.x, p1.y
        p2 = p2.x, p2.y
        p3 = p3.x, p3.y
        p4 = p4.x, p4.y
        
        curves = splitCubicAtT(p1, p2, p3, p4, t)
        curve = curves[1]
        
        x1, y1 = curve[3]
        x2, y2 = curve[2]
        
        ox, oy = getOffset(offset, (x1, y1), (x2, y2))
        
        if reverse:
            prevSegment, segment = segment, prevSegment
        
        segment.onCurve.move((ox, oy))
        
        

def addOverlap():
    glyph = CurrentGlyph()

    selection = [segment for contour in glyph for segment in contour if segment.onCurve.selected]

    if len(selection) == 1:
    
        s = selection[0]
    
        glyph.prepareUndo("addOverlap")
    
        contour = s.getParent()
            
        indexB = contour.segments.index(s)
        
        pointB = s.onCurve
        pointB.selected = False
        
        # doubling the point B to C
        bx, by = pointB.x, pointB.y
        
        index = indexB
        insertIndex = (index+1) % len(contour)   
            
        contour.insertSegment(insertIndex, "line", [(bx, by)])
        
        """
          C--B
           \/
           /\
          /  \
         /    \
        A      D
        """
        
        # index shift, annoying fix for index error when inserting segment
        j = 0
        # check if first or last point
        if insertIndex == 0 or insertIndex == len(contour)-1:
            # but if is last point and curve don't shift
            if insertIndex == len(contour)-1 and contour[-1].type == "curve":
                j = 0
            else:
                j = 1 
                        
        indexA = (index-1+j) % len(contour)
        indexB = (index+0+j) % len(contour)
        indexC = (index+1+j) % len(contour)
        indexD = (index+2+j) % len(contour)
                
        segmentA = contour[indexA]
        segmentB = contour[indexB]
        segmentC = contour[indexC]
        segmentD = contour[indexD]
                
        offsetSegment(segmentA, segmentB)
        offsetSegment(segmentC, segmentD, True)
            
        glyph.performUndo()
    
        glyph.update()


addOverlap()