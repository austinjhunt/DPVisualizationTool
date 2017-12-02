from graphics import *

#class to create window, background (table) 
class Table:
    table1 = Circle(Point(250,250),130)
    table1.setFill(color_rgb(0,0,0))
    table2 = Circle(Point(250,250),100)
    table2.setFill(color_rgb(50,50,50))


#class PhilosopherBoi():
   # def __init__(self):
        
        
   # def pickUpRight(PhilosopherId):

   # def pickUpLeft(PhilosopherId):
        
        
    

def main():
    win = GraphWin('Dining Philosophers', 500, 500)
    table = Table()
    table.table1.draw(win)
    table.table2.draw(win)
    win.getMouse()
    win.close()

    

main()
