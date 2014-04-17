"""
This script will create an overlap for the selected point.
If the segment is a curve, it will use the offCurves for the overlap direction.
"""
import math

offset = 30


def getLength((x1, y1), (x2, y2)):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
    

def getOffset(offset, (x1, y1), (x2, y2)):
    
    length = getLength((x1, y1), (x2, y2))
    
    if length == 0:
        return None
    
    ox = (x2-x1)/length*offset
    oy = (y2-y1)/length*offset
    
    return int(round(ox)), int(round(oy))


def offsetSegment(prevSegment, segment, reverse=False):
    
    p1 = prevSegment.onCurve
    p2 = segment.onCurve
    
    p1 = p1.x, p1.y
    p2 = p2.x, p2.y
    
    if reverse: # change direction
        p1, p2 = p2, p1
    
    isCurve = False
    if segment.type == "curve":
        
        q1, q2 = segment.offCurve
        
        q1 = q1.x, q1.y
        q2 = q2.x, q2.y
        
        if reverse: # change direction
            q1, q2 = q2, q1
        
        # check that off curves are not overlapping
        if q2 != p2:
            isCurve = True
        
    if isCurve:
        
        x1, y1 = q2
        x2, y2 = p2
    
    else: # is line
        
        x1, y1 = p1
        x2, y2 = p2
        
    o = getOffset(offset, (x1, y1), (x2, y2))

    if o:
        ox, oy = o
    else:
        return
    
    if reverse: # change direction
        prevSegment, segment = segment, prevSegment

    segment.onCurve.move((ox, oy))
        

def addOverlap():
    glyph = CurrentGlyph()

    selection = [segment for contour in glyph for segment in contour if segment.onCurve.selected]

    if len(selection) == 1:
    
        glyph.prepareUndo("addOverlap")

        s = selection[0]    
        
        contour = s.getParent()            
        
        point = s.onCurve
        point.selected = False
        
        x, y = point.x, point.y
        
        index = contour.segments.index(s)
        insertIndex = (index+1) % len(contour)
            
        contour.insertSegment(insertIndex, "line", [(x, y)])
        
        # get the new index from the initial segment
        index = contour.segments.index(s)
                        
        indexA = (index-1) % len(contour)
        indexB = (index+0) % len(contour)
        indexC = (index+1) % len(contour)
        indexD = (index+2) % len(contour)
                
        segmentA = contour[indexA]
        segmentB = contour[indexB]
        segmentC = contour[indexC]
        segmentD = contour[indexD]
                
        offsetSegment(segmentA, segmentB)
        offsetSegment(segmentC, segmentD, True)
            
        glyph.performUndo()
    
        glyph.update()


addOverlap()