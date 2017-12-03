# need to translate hw3.c to python in this file

from threading import *
from DiningPhilosophers.hw3 import dpsim
from DiningPhilosophers.hw3.dpsim import *


def main():
    mainThread = dpsim.Thread(target=mainThreadAction())
    mainThread.join()


main()
