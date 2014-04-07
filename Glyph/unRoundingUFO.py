### Thanks to Mark Frömberg for the idea :)

# line intersection method
# http://math.stackexchange.com/questions/27388/intersection-of-2-lines-in-2d-via-general-form-linear-equations
def getIntersection((x0, y0), (x1, y1), (x2, y2), (x3, y3)):
    a = y0 - y1
    b = x1 - x0
    c = (y1 - y0) * x0 - (x1 - x0) * y0
    d = y2 - y3
    e = x3 - x2
    f = (y3 - y2) * x2 - (x3 - x2) * y2
    if (-d*b + a*e) != 0:
        y = (c*d - f*a) / (-d*b + a*e)
        x = (b*f - c*e) / (-d*b + a*e)
        return x, y
    else:
        return None
        
g = CurrentGlyph()

# get all the selected curve segments
for contour in g:
    segmentList = []
    for i, segment in enumerate(contour):
        if segment.selected and segment.type == "curve":
            segmentList.append(i)
    j = 0 # needed to update the index when a segment is added
    for i in segmentList:
        s = i+j # get the new segment index
        prev = (s-1) % len(contour)
        p0 = contour[prev].onCurve
        p1, p2 = contour[s].offCurve
        p3 = contour[s].onCurve
        intersection = getIntersection((p0.x, p0.y), (p1.x, p1.y), (p2.x, p2.y), (p3.x, p3.y))
        if intersection: # unround!
            g.prepareUndo("unround")
            contour[s].type = "line"
            contour.insertSegment(s, "line", [intersection])
            g.round()
            g.update()
            g.performUndo()
            j+=1 # set the new segment index