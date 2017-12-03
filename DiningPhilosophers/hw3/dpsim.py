# Need to translate dpsim.c to python here

from threading import *
import copy
import time

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


def mainThreadAction():
    for i in range(0, NUM_CHOPSTICKS):
        chopsticks.append(-1)
    print("Chopsticks initialized!")

    for j in range(0, NUM_PHILOSOPHERS):
        currPhilosopherThread = Thread(target=philosopherAction, args=[j])
        philosopherThreads.append(currPhilosopherThread)

        currPhilosopherThread.start()

    print("Thread created for each philosopher!")

    #initialize array of mutex locks

    for m in range(0, NUM_PHILOSOPHERS):

        mutexArray.append(Lock())
        print("APPENDING LOCK")
    p0Eating=False
    p1Eating=False
    p2Eating=False
    p3Eating=False
    p4Eating=False
    while True:
        chopsticksCopy = copy.copy(chopsticks)

        if chopsticksCopy[0] == 0 and chopsticksCopy[1] == 0:
            p0Eating = True
        else:
            p0Eating = False

        if chopsticksCopy[1] == 1 and chopsticksCopy[2] == 1:
            p1Eating = True
        else:
            p1Eating = False

        if chopsticksCopy[2] == 2 and chopsticksCopy[3] == 2:
            p2Eating = True
        else:
            p2Eating = False

        if chopsticksCopy[3] == 3 and chopsticksCopy[4] == 3:
            p3Eating = True
        else:
            p3Eating = False

        if chopsticksCopy[4] == 4 and chopsticksCopy[0] == 4:
            p4Eating = True
        else:
            p4Eating = False

        # WHich ones are eating?

        print("\nPhilosopher(s) ")
        if p0Eating:
            print("0")
        if p1Eating:
            print("1")
        if p2Eating:
            print("")
        if p3Eating:
            print("3")
        if p4Eating:
            print("4")
        print(" are eating.\n")

        # Deadlock
        if chopsticksCopy[0] == 0 and chopsticksCopy[1] == 1 and chopsticksCopy[2] == 2 \
                and chopsticksCopy[3] == 3 and chopsticksCopy[4] == 4:
            print("Deadlock condition (0,1,2,3,4) ... terminating.")
            break

        time.sleep(.1)

    for k in range(0, NUM_PHILOSOPHERS):
        philosopherThreads[k].stop()

    return


# philosopher thread
def philosopherAction(philId):
    while True:
        time.sleep(.01)
        eat(philId)


def eat(phil_id):

    with mutexArray[phil_id]:
        chopsticks[phil_id] = phil_id

        with mutexArray[(phil_id + 1) % NUM_CHOPSTICKS]:
            chopsticks[(phil_id + 1) % NUM_CHOPSTICKS] = phil_id
            time.sleep(4)  # eating 3 seconds



def main():

    mainThread = Thread(target=mainThreadAction())

    mainThread.join()


main()
