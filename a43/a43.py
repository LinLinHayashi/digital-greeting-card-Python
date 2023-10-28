#!/usr/bin/env python3
'''a43'''
print(__doc__)


from typing import IO
import sys
sys.path.append("..")

from a41.a41 import Circle
from a41.a41 import Rectangle
from a41.a41 import ProEpilogue
from a41.a41 import drawCircleLine
from a41.a41 import drawRectangleLine
from a41.a41 import openSVGcanvas
from a41.a41 import closeSVGcanvas
from a41.a41 import writeHTMLHeader
from a42.a42 import ArtConfig
from a42.a42 import GenRandom


def genArtRandom(f: IO[str], t: int, loop: int):
    '''genArtRandom method'''
    i: int = 0
    for i in range(loop):
        if GenRandom(ArtConfig(0, 2)).number == 0: # Draw a circle.
            cx: int = GenRandom(ArtConfig(0, 1001)).number
            cy: int = GenRandom(ArtConfig(0, 601)).number
            rad: int = GenRandom(ArtConfig(0, 101)).number
            r: int = GenRandom(ArtConfig(0, 256)).number
            g: int = GenRandom(ArtConfig(0, 256)).number
            b: int = GenRandom(ArtConfig(0, 256)).number
            op: float = float(GenRandom(ArtConfig(0, 11)).number * 0.1)
            drawCircleLine(f, t, Circle((cx, cy, rad),(r, g, b, op)))
        else: # Draw a Rectangle.
            rx: int = GenRandom(ArtConfig(0, 1001)).number
            ry: int = GenRandom(ArtConfig(0, 601)).number
            w: int = GenRandom(ArtConfig(10, 31)).number
            h: int = GenRandom(ArtConfig(10, 31)).number
            r: int = GenRandom(ArtConfig(0, 256)).number
            g: int = GenRandom(ArtConfig(0, 256)).number
            b: int = GenRandom(ArtConfig(0, 256)).number
            op: float = float(GenRandom(ArtConfig(0, 11)).number * 0.1)
            drawRectangleLine(f, t, Rectangle((rx, ry, w, h),(r, g, b, op)))

def writeHTMLRandom():
    '''writeHTMLRandom method'''
    fnam: str = "myPart1Art.html"
    winTitle: ProEpilogue = ProEpilogue("My Art")
    f: IO[str] = open(fnam, "w")
    writeHTMLHeader(f, winTitle)
    openSVGcanvas(f, 1, (600,1000))
    genArtRandom(f, 2, 800)
    closeSVGcanvas(f, 1, winTitle)
    f.close()

def main():
    '''main method'''
    writeHTMLRandom()

main()                                                                                                                                                                                                                                                                                       