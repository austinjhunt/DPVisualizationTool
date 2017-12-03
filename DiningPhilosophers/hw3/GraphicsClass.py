from graphics import *
from math import *

#class to create window, background (table) 
class Table:
    table1 = Circle(Point(250,250),130)
    table1.setFill(color_rgb(0,0,0))
    table2 = Circle(Point(250,250),100)
    table2.setFill(color_rgb(50,50,50))


class PhilosopherBoi:

    myHead = None



    def __init__(self, r, g, b, x, y):
        self.myHead = Circle()
        self.myHead.setFill(color_rgb(r, g, b))
        self.myHead.setOutline(color_rgb(r, g, b))

    def pickUpRight(philId):
        if philId = 0:
            #create arm in necesssary position for THIS philosopher
            #draw that arm
            
        if philId = 1:
            ##
        if philId = 2:

        if philId = 3:

        if philId = 4:

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
    philosoph = PhilosopherBoi(255,255,0,point1x * 100, point1y * 100)
    philosoph.myFuckingHead.draw(win)
    #create philosopher
    #boi1 = PhilosopherBoi(255, 255, 0, point1x * 100, point1y * 100)
    #philosopherCircle = boi1.makePhilosopher()

    #philosopherCircle.draw(win)

    win.getMouse()
    win.close()

    

main()
