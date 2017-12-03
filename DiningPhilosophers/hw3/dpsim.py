# Need to translate dpsim.c to python here

import copy
from time import sleep
from DiningPhilosophers.hw3.GraphicsClass import *
from DiningPhilosophers.hw3.StoppableThread import *

win = GraphWin('Dining Philosophers', 500, 500)

# draw table and philosophers and chopsticks, ready to eat
table = Table(Point(250,250),win)


philosoph0 = PhilosopherBoi(0, 220, 0, 270, 398, win)
philosoph1 = PhilosopherBoi(0, 220, 0, 113, 304, win)
philosoph2 = PhilosopherBoi(0, 220, 0, 173, 130, win)
philosoph3 = PhilosopherBoi(0, 220, 0, 344, 139, win)
philosoph4 = PhilosopherBoi(0, 220, 0, 390, 278, win)

# Chopsticks
chopstick0 = ChopStick(10, 255, 255, 0, Point(205, 327), Point(228, 295), win)

chopstick1 = ChopStick(10, 255, 255, 0, Point(170, 219), Point(200, 229), win)

chopstick2 = ChopStick(10, 255, 255, 0, Point(251, 160), Point(253, 185), win)

chopstick3 = ChopStick(10, 255, 255, 0, Point(335, 215), Point(304, 223), win)

chopstick4 = ChopStick(10, 255, 255, 0, Point(314, 321), Point(290, 295), win)

# wait for click to start
win.getMouse()

# Define constants
NUM_PHILOSOPHERS = 5
NUM_CHOPSTICKS = 5

# Define static vars

# array of chopsticks
chopsticks = []  # capacity of 5
# array of mutexes
mutexArray = []  # will have 5 locks
philosopherThreads = []  # will have 5 threads
philosopherObjects = []  # will have 5 objects
philosopherObjects.append(philosoph0)
philosopherObjects.append(philosoph1)
philosopherObjects.append(philosoph2)
philosopherObjects.append(philosoph3)
philosopherObjects.append(philosoph4)


def mainThreadAction():
    for i in range(0, NUM_CHOPSTICKS):
        chopsticks.append(-1)
    print("Chopsticks initialized!")

    for j in range(0, NUM_PHILOSOPHERS):
        id = "phil"+j.__str__()
        currPhilosopherThread = StoppableThread(name=id,target=philosopherAction, args=[j])
        philosopherThreads.append(currPhilosopherThread)

        currPhilosopherThread.start()

    print("Thread created for each philosopher!")

    # initialize array of mutex locks

    for m in range(0, NUM_PHILOSOPHERS):
        mutexArray.append(Lock())

    p0Eating = False
    p1Eating = False
    p2Eating = False
    p3Eating = False
    p4Eating = False
    while True:

        chopsticksCopy = copy.copy(chopsticks)

        if chopsticksCopy[0] == 0:
            philosoph0.pickUpRight(0, win)
            if chopsticksCopy[1] == 0:
                philosoph0.pickUpLeft(0, win)
                p0Eating = True
            else:
                p0Eating = False
        else:
            p0Eating = False

        if chopsticksCopy[1] == 1:
            philosoph1.pickUpRight(1, win)
            if chopsticksCopy[2] == 1:
                philosoph1.pickUpLeft(1, win)
                p1Eating = True
            else:
                p1Eating = False
        else:
            p1Eating = False

        if chopsticksCopy[2] == 2:
            philosoph2.pickUpRight(2, win)
            if chopsticksCopy[3] == 2:
                philosoph2.pickUpLeft(2, win)
                p2Eating = True
            else:
                p2Eating = False
        else:
            p2Eating = False

        if chopsticksCopy[3] == 3:
            philosoph3.pickUpRight(3, win)
            if chopsticksCopy[4] == 3:
                philosoph3.pickUpLeft(3, win)
                p3Eating = True
            else:
                p3Eating = False
        else:
            p3Eating = False

        if chopsticksCopy[4] == 4:
            philosoph4.pickUpRight(4, win)
            if chopsticksCopy[0] == 4:
                philosoph4.pickUpLeft(4, win)
                p4Eating = True
        else:
            p4Eating = False

        # WHich ones are eating?

        print("\nPhilosopher(s) ",end="")
        if p0Eating:
            print("0",end=" ")
        if p1Eating:
            print("1",end=" ")
        if p2Eating:
            print("", end= " ")
        if p3Eating:
            print("3",end= " ")
        if p4Eating:
            print("4",end= " ")
        print(" are eating.\n")

        # Deadlock
        if chopsticksCopy[0] == 0 and chopsticksCopy[1] == 1 and chopsticksCopy[2] == 2 \
                and chopsticksCopy[3] == 3 and chopsticksCopy[4] == 4:
            print("Deadlock condition (0,1,2,3,4) ... terminating.")
            break

        time.sleep(.01)
        #win.getMouse()
        philosoph0.putDownLeft()
        philosoph0.putDownRight()

        philosoph1.putDownLeft()
        philosoph1.putDownRight()

        philosoph2.putDownLeft()
        philosoph2.putDownRight()

        philosoph3.putDownLeft()
        philosoph3.putDownRight()

        philosoph4.putDownLeft()
        philosoph4.putDownRight()

    for k in range(0, NUM_PHILOSOPHERS):
        philosopherThreads[k].stop_me()


    win.getMouse()
    undrawAllArms()

    win.close()

def undrawAllArms():
    philosoph4.RightArm.undraw()
    philosoph4.LeftArm.undraw()
    philosoph3.RightArm.undraw()
    philosoph3.LeftArm.undraw()
    philosoph2.RightArm.undraw()
    philosoph2.LeftArm.undraw()
    philosoph1.RightArm.undraw()
    philosoph1.LeftArm.undraw()
    philosoph0.RightArm.undraw()
    philosoph4.LeftArm.undraw()



    # philosopher thread
def philosopherAction(philId):
    while True:
        time.sleep(1)
        eat(philId)


def eat(phil_id):
    with mutexArray[phil_id]:
        chopsticks[phil_id] = phil_id

        with mutexArray[(phil_id + 1) % NUM_CHOPSTICKS]:
            chopsticks[(phil_id + 1) % NUM_CHOPSTICKS] = phil_id
            time.sleep(1)  # eating 1 seconds
            chopsticks[(phil_id + 1) % NUM_CHOPSTICKS] = -1 #set down left

        time.sleep(.01) #hold left for very little time
        chopsticks[phil_id] = -1


