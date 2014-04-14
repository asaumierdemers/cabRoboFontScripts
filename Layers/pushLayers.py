def pushLayers(glyph):

    if glyph is None:
        print "Nothing to push!"
        return

    layers = font.layerOrder
    layerNumber = len(font.layerOrder)
    
    if layers:
        firstLayer = glyph.getLayer(layers[0])
    
    if layerNumber == 1 and not firstLayer.contours and not firstLayer.components:
        # one layer and empty
        glyph.copyToLayer(layers[0])
        print "foreground \t>>\t", layers[0]
        return
        
    newLayer = 'background' + str(layerNumber)
    
    lastLayer = glyph.getLayer(layers[-1])
    
    if lastLayer.contours or lastLayer.components:
        # this create the new layer
        glyph.getLayer(newLayer)
        layerNumber+=1
        
    for i in range(1, layerNumber):
        prevLayer = layers[-i-1]
        nextLayer = layers[-i]
        glyph.getLayer(prevLayer).swapToLayer(nextLayer)
        print prevLayer, "\t->\t", nextLayer
    
    glyph.copyToLayer(layers[0])
    print "foreground \t>>\t", layers[0]
        
    font.update()
    
    
font = CurrentFont()
glyph = CurrentGlyph()

pushLayers(glyph)