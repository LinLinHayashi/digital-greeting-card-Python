#!/usr/bin/env python3
'''a41'''
print(__doc__)

from typing import IO

class Circle:
    '''Circle class'''
    def __init__(self, cir: tuple, col: tuple):
        self.cx: int = cir[0]
        self.cy: int = cir[1]
        self.rad: int = cir[2]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]

class Rectangle:
    '''Rectangle class'''
    def __init__(self, rec: tuple, col: tuple):
        self.top_left_x: int = rec[0]
        self.top_left_y: int = rec[1]
        self.width: int = rec[2]
        self.height: int = rec[3]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]

class ProEpilogue:
    '''ProEpilogue class'''
    def __init__(self, title: str):
        self.html_start: str = "<html>"
        self.body_start: str = "<body>"
        self.head_start: str = "<head>"
        self.title_start: str = "<title>"
        self.title: str = title
        self.title_end: str = "</title>"
        self.head_end: str = "</head>"
        self.body_end: str = "</body>"
        self.html_end: str = "</html>"
        
def writeHTMLcomment(f: IO[str], t: int, com: str):
    '''writeHTMLcomment method'''
    ts: str = "   " * t
    f.write(f'{ts}<!--{com}-->\n')
        
def drawCircleLine(f: IO[str], t: int, c: Circle):
    '''drawCircle method'''
    ts: str = "   " * t
    line: str = f'<circle cx="{c.cx}" cy="{c.cy}" r="{c.rad}" fill="rgb({c.red}, {c.green}, {c.blue})" fill-opacity="{c.op}"></circle>'
    f.write(f"{ts}{line}\n")

def drawRectangleLine(f: IO[str], t: int, rec: Rectangle):
    '''drawRectangle method'''
    ts: str = "   " * t
    line: str = f'<rect x="{rec.top_left_x}" y="{rec.top_left_y}" width="{rec.width}" height="{rec.height}" fill="rgb({rec.red}, {rec.green}, {rec.blue})" fill-opacity="{rec.op}"></rect>'
    f.write(f"{ts}{line}\n")

def genArt(f: IO[str], t: int):
    '''genART method'''
    drawCircleLine(f, t, Circle((50,50,50), (255,0,0,1.0)))
    drawCircleLine(f, t, Circle((150,50,50), (255,0,0,1.0)))
    drawCircleLine(f, t, Circle((250,50,50), (255,0,0,1.0)))
    drawCircleLine(f, t, Circle((350,50,50), (255,0,0,1.0)))
    drawCircleLine(f, t, Circle((450,50,50), (255,0,0,1.0)))
    drawCircleLine(f, t, Circle((50,250,50), (0,0,255,1.0)))
    drawCircleLine(f, t, Circle((150,250,50), (0,0,255,1.0)))
    drawCircleLine(f, t, Circle((250,250,50), (0,0,255,1.0)))
    drawCircleLine(f, t, Circle((350,250,50), (0,0,255,1.0)))
    drawCircleLine(f, t, Circle((450,250,50), (0,0,255,1.0)))
    drawRectangleLine(f, t, Rectangle((50,450,50,60), (255,0,0,1.0)))
    drawRectangleLine(f, t, Rectangle((150,450,50,60), (255,0,0,1.0)))
    drawRectangleLine(f, t, Rectangle((250,450,50,60), (255,0,0,1.0)))
    drawRectangleLine(f, t, Rectangle((350,450,50,60), (255,0,0,1.0)))
    drawRectangleLine(f, t, Rectangle((450,450,50,60), (255,0,0,1.0)))
    drawRectangleLine(f, t, Rectangle((50,650,50,60), (0,0,255,1.0)))
    drawRectangleLine(f, t, Rectangle((150,650,50,60), (0,0,255,1.0)))
    drawRectangleLine(f, t, Rectangle((250,650,50,60), (0,0,255,1.0)))
    drawRectangleLine(f, t, Rectangle((350,650,50,60), (0,0,255,1.0)))
    drawRectangleLine(f, t, Rectangle((450,650,50,60), (0,0,255,1.0)))
        
def openSVGcanvas(f: IO[str], t: int, canvas: tuple):
    '''openSVGcanvas method'''
    ts: str = "   " * t
    writeHTMLcomment(f, t, "Define SVG drawing box")
    f.write(f'{ts}<svg width="{canvas[0]}" height="{canvas[1]}">\n')

def closeSVGcanvas(f: IO[str], t: int, log: ProEpilogue):
    '''closeSVGcanvas method'''
    ts: str = "   " * t
    f.write(f'{ts}</svg>\n')
    f.write(f'{log.body_end}\n')
    f.write(f'{log.html_end}\n')

def writeHTMLline(f: IO[str], t: int, line: str):
    '''writeLineHTML method'''
    ts = "   " * t
    f.write(f"{ts}{line}\n")

def writeHTMLHeader(f: IO[str], log: ProEpilogue):
    '''writeHeadHTML method'''
    writeHTMLline(f, 0, log.html_start)
    writeHTMLline(f, 0, log.head_start)
    writeHTMLline(f, 1, f"{log.title_start}{log.title}{log.title_end}")
    writeHTMLline(f, 0, log.head_end)
    writeHTMLline(f, 0, log.body_start)

def writeHTMLfile():
    '''writeHTMLfile method'''
    fnam: str = "myPart1Art.html"
    winTitle: ProEpilogue = ProEpilogue("My Art")
    f: IO[str] = open(fnam, "w")
    writeHTMLHeader(f, winTitle)
    openSVGcanvas(f, 1, (800,1000))
    genArt(f, 2)
    closeSVGcanvas(f, 1, winTitle)
    f.close()

def main():
    '''main method'''
    writeHTMLfile()

main()                                                                                                                                                                                                                                                                                       