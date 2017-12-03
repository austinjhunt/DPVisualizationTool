from graphics import *
from math import *

#class to create window, background (table) 
class Table:
    table1 = Circle(Point(250,250),130)
    table1.setFill(color_rgb(0,0,0))
    table2 = Circle(Point(250,250),100)
    table2.setFill(color_rgb(50,50,50))

class LChopStick:
    datStick = None
    def __init__(self, width, r, g, b):
        self.datStick = Line(Point(30,60), Point(60,100))
        self.datStick.setWidth(width)
        self.datStick.setFill(color_rgb(r, g, b))
class PhilosopherBoi:

    myHead = None



    def __init__(self, r, g, b, x, y):
        self.myHead = Circle(Point(x, y), 50)
        self.myHead.setFill(color_rgb(r, g, b))
        self.myHead.setOutline(color_rgb(r, g, b))

    # def pickUpRight(philId):
    #     if philId = 0:
    #         #create arm in necesssary position for THIS philosopher
    #         #draw that arm
    #
    #     if philId = 1:
    #         ##
    #     if philId = 2:
    #
    #     if philId = 3:
    #
    #     if philId = 4:

    #def pickUpRight(PhilosopherId):
     #   return 1

#    def pickUpLeft(PhilosopherId):
 #       return 2
        
    

def main():
    degreeInterval = 72
    point1x = cos(degreeInterval)
    point1y = sin(degreeInterval)
    point2x = cos(degreeInterval*2)
    point2y = sin(degreeInterval*2)
    point3x = cos(degreeInterval*3)
    point3y = sin(degreeInterval*3)
    point4x = cos(degreeInterval*4)
    point4y = sin(degreeInterval*4)
    point5x = cos(degreeInterval*5)
    point5y = sin(degreeInterval*5)



    win = GraphWin('Dining Philosophers', 500, 500)
    table = Table()
    table.table1.draw(win)
    table.table2.draw(win)
    philosoph = PhilosopherBoi(0,255,0,250 -(point1x * 200), 250 -(point1y * 200))
    philosoph.myHead.draw(win)
    philosoph2 = PhilosopherBoi(0, 255, 0, 250 - (point2x * 200), 250 - (point2y * 200))
    philosoph2.myHead.draw(win)
    philosoph3 = PhilosopherBoi(0, 255, 0, 250 - (point3x * 200), 250 - (point3y * 200))
    philosoph3.myHead.draw(win)
    leftChop1 = LChopStick(20,255, 255, 0)
    leftChop1.datStick.draw(win)
    #create philosopher
    #boi1 = PhilosopherBoi(255, 255, 0, point1x * 100, point1y * 100)
    #philosopherCircle = boi1.makePhilosopher()

    #philosopherCircle.draw(win)

    win.getMouse()
    win.close()

    

main()
