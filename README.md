This is a tool written in Python to visualize the Dining Philosophers problem; the timings are set to create eventual deadlock, but decreasing or removing the time of holding the second chopstick will greatly reduce likelihood of deadlock.

#How to Use
Open terminal. 
Clone the repository. 
Open the DiningPhilosophers project in an IDE of your choice (I use PyCharm)
In the IDE, run backendThreads.py.
to adjust when deadlock occurs, increase or decrease the time.sleep() function used in the second mutex lock of the eat() function. 




