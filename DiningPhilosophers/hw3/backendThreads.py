# need to translate hw3.c to python in this file


from DiningPhilosophers.hw3.dpsim import *
from DiningPhilosophers.hw3.StoppableThread import *


def main():
    mainThread = StoppableThread(name=1, target=mainThreadAction(), args=())
    mainThread.start()
    mainThread.join()


main()