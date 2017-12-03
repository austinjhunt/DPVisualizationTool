from graphics import *
from math import *


# class to create window, background (table)
class Table:
    table1 = Circle(Point(250, 250), 130)
    table2 = Circle(Point(250, 250), 100)
    def __init__(self,center,win):
        self.table1.setFill(color_rgb(0, 0, 0))
        self.table2.setFill(color_rgb(50, 50, 50))
        self.table1.draw(win)
        self.table2.draw(win)


class ChopStick:
    datStick = None

    def __init__(self, width, r, g, b, p1, p2,win):
        self.datStick = Line(p1, p2)
        self.datStick.setWidth(width)
        self.datStick.setFill(color_rgb(r, g, b))
        self.datStick.draw(win)


class PhilosopherBoi:
    myHead = Circle(Point(0,0),0)
    RightArm = Line(Point(0,0),Point(0,0))
    LeftArm = Line(Point(1,0),Point(1,0))

    def __init__(self, r, g, b, x, y, win):
        self.myHead = Circle(Point(x, y), 50)
        self.myHead.setFill(color_rgb(r, g, b))
        self.myHead.setOutline(color_rgb(r, g, b))
        self.myHead.draw(win)

    def pickUpRight(self,philId, win):

        if philId == 0:
            self.RightArm = Line(Point(270, 398), Point(314, 321))
            #self.RightArm.__setattr__('self.RightArm.p1', Point(270,398))
            #self.RightArm.__setattr__('self.RightArm.p2', Point(314, 321))
            self.RightArm.setFill(color_rgb(255, 255, 255))
            self.RightArm.setWidth(7)
            self.RightArm.draw(win)
        if philId == 1:
            self.RightArm = Line(Point(113, 304), Point(205, 327))
            #self.RightArm.__setattr__('self.RightArm.p1', Point(113,304))
            #self.RightArm.__setattr__('self.RightArm.p2', Point(205,327))
            self.RightArm.setFill(color_rgb(255, 255, 255))
            self.RightArm.setWidth(7)
            self.RightArm.draw(win)
        if philId == 2:
            self.RightArm = Line(Point(173, 130), Point(170, 219))
            #self.RightArm.__setattr__('self.RightArm.p1', Point(173,130))
            #self.RightArm.__setattr__('self.RightArm.p2', Point(170,219))
            self.RightArm.setFill(color_rgb(255, 255, 255))
            self.RightArm.setWidth(7)
            self.RightArm.draw(win)
        if philId == 3:
            self.RightArm = Line(Point(344, 139), Point(253, 160))
            #self.RightArm.__setattr__('self.RightArm.p1', Point(344,139))
            #self.RightArm.__setattr__('self.RightArm.p2', Point(253,160))
            self.RightArm.setWidth(7)
            self.RightArm.setFill(color_rgb(255, 255, 255))
            self.RightArm.draw(win)
        if philId == 4:
            self.RightArm = Line(Point(390, 278), Point(335, 215))
            #self.RightArm.__setattr__('self.RightArm.p1', Point(390,278))
            #self.RightArm.__setattr__('self.RightArm.p2', Point(335,215))
            self.RightArm.setWidth(7)
            self.RightArm.setFill(color_rgb(255,255,255))
            self.RightArm.draw(win)

    def putDownLeft(self):
        self.LeftArm.undraw()
    def putDownRight(self):
        self.RightArm.undraw()


    def pickUpLeft(self,philId, win):
        if philId == 0:
            self.LeftArm = Line(Point(270, 398), Point(205, 327))
            #self.LeftArm.__setattr__('self.LeftArm.p1', Point(270,398))
            #self.LeftArm.__setattr__('self.LeftArm.p2', Point(205,327))
            self.LeftArm.setFill(color_rgb(255, 255, 255))
            self.LeftArm.setWidth(7)
            self.LeftArm.draw(win)
        if philId == 1:
            self.LeftArm = Line(Point(113, 304), Point(170, 219))
            #self.LeftArm.__setattr__('self.LeftArm.p1', Point(113,304))
            #self.LeftArm.__setattr__('self.LeftArm.p2', Point(170,219))
            self.LeftArm.setFill(color_rgb(255, 255, 255))
            self.LeftArm.setWidth(7)
            self.LeftArm.draw(win)
        if philId == 2:
            self.LeftArm = Line(Point(173, 130), Point(253,160))
            #self.LeftArm.__setattr__('self.LeftArm.p1', Point(173,130))
           # self.LeftArm.__setattr__('self.LeftArm.p2', Point(253,160))
            self.LeftArm.setFill(color_rgb(255, 255, 255))
            self.LeftArm.setWidth(7)
            self.LeftArm.draw(win)
        if philId == 3:
            self.LeftArm = Line(Point(344, 139), Point(335,215))

            #self.LeftArm.__setattr__('self.LeftArm.p1', Point(344,139))
            #self.LeftArm.__setattr__('self.LeftArm.p2', Point(335,215))
            self.LeftArm.setWidth(7)
            self.LeftArm.setFill(color_rgb(255, 255, 255))
            self.LeftArm.draw(win)
        if philId == 4:
            self.LeftArm = Line(Point(390,278),Point(314,321))
            #self.LeftArm.__setattr__('self.LeftArm.p1', Point(390, 278))
            #self.LeftArm.__setattr__('self.LeftArm.p2', Point(314, 321))
            self.LeftArm.setWidth(7)
            self.LeftArm.setFill(color_rgb(255,255,255))
            self.LeftArm.draw(win)
