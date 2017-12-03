#need to translate hw3.c to python in this file

from threading import *
from .dpsim import *


def main():

    mainThread = Thread(target=mainThreadAction)

    print("Error creating main thead!")
    exit(1)

    try:
        mainThread.join()
    except:
        print("Error joining!")
        exit(2)

    return 0;






