from graphics import *
from math import *


# class to create window, background (table)
class Table:
    table1 = Circle(Point(250, 250), 130)
    table1.setFill(color_rgb(0, 0, 0))
    table2 = Circle(Point(250, 250), 100)
    table2.setFill(color_rgb(50, 50, 50))


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
    LeftArm = Line(Point(0,0),Point(0,0))

    def __init__(self, r, g, b, x, y, win):
        self.myHead = Circle(Point(x, y), 50)
        self.myHead.setFill(color_rgb(r, g, b))
        self.myHead.setOutline(color_rgb(r, g, b))
        self.myHead.draw(win)

    def pickUpRight(self,philId, win):
        if philId == 0:
            RightArm = Line(Point(270, 398), Point(314, 321))
            RightArm.setFill(color_rgb(255, 255, 255))
            RightArm.setWidth(7)
            RightArm.draw(win)
        if philId == 1:
            RightArm = Line(Point(113, 304), Point(205, 327))
            RightArm.setFill(color_rgb(255, 255, 255))
            RightArm.setWidth(7)
            RightArm.draw(win)
        if philId == 2:
            RightArm = Line(Point(173, 130), Point(170, 219))
            RightArm.setFill(color_rgb(255, 255, 255))
            RightArm.setWidth(7)
            RightArm.draw(win)
        if philId == 3:
            RightArm = Line(Point(344, 139), Point(253, 160))
            RightArm.setWidth(7)
            RightArm.setFill(color_rgb(255, 255, 255))
            RightArm.draw(win)
        if philId == 4:
            RightArm = Line(Point(390, 278), Point(335, 215))
            RightArm.setWidth(7)
            RightArm.setFill(color_rgb(255,255,255))
            RightArm.draw(win)

    def putDownLeft(self):
        self.LeftArm.undraw()
    def putDownRight(self):
        self.RightArm.undraw()


    def pickUpLeft(self,philId, win):
        if philId == 0:
            LeftArm = Line(Point(270, 398), Point(205, 327))
            LeftArm.setFill(color_rgb(255, 255, 255))
            LeftArm.setWidth(7)
            LeftArm.draw(win)
        if philId == 1:
            LeftArm = Line(Point(113, 304), Point(170, 219))
            LeftArm.setFill(color_rgb(255, 255, 255))
            LeftArm.setWidth(7)
            LeftArm.draw(win)
        if philId == 2:
            LeftArm = Line(Point(173, 130), Point(253,160))
            LeftArm.setFill(color_rgb(255, 255, 255))
            LeftArm.setWidth(7)
            LeftArm.draw(win)
        if philId == 3:
            LeftArm = Line(Point(344, 139), Point(335,215))
            LeftArm.setWidth(7)
            LeftArm.setFill(color_rgb(255, 255, 255))
            LeftArm.draw(win)
        if philId == 4:
            LeftArm = Line(Point(390, 278), Point(314, 321))
            LeftArm.setWidth(7)
            LeftArm.setFill(color_rgb(255,255,255))
            LeftArm.draw(win)

