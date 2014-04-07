# This simple script will save the current space center to a PDF in your current font folder.

from mojo.UI import CurrentSpaceCenter, SpaceCenterToPDF
import time
import os

font = CurrentFont()

if font and CurrentSpaceCenter():
    
    ufoPath = font.path
    ufoDirectory = os.path.dirname(ufoPath)
    fileName, fileExtension = os.path.splitext(ufoPath)
    
    t = time.strftime("_%Y-%m-%d_%H-%M")
    
    pdf = fileName + t + ".pdf"
    path = os.path.join(ufoDirectory, pdf)

    SpaceCenterToPDF(path)
    
    cmd = "open %s" % path
    os.system(cmd)