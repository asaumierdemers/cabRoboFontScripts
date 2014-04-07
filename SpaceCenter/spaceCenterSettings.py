from mojo.UI import CurrentSpaceCenter

pointSize = 200
percentLineHeight = 1.2
tracking = 0

lineHeight = percentLineHeight * 1000 - 1000

spaceCenter = CurrentSpaceCenter()
spaceCenter.setPointSize(pointSize)
spaceCenter.setTracking(tracking)
spaceCenter.glyphLineView.setLineHeight(lineHeight)