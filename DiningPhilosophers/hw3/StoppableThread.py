from threading import *
import logging
import sys

class StoppableThread(Thread):

    # Implements a thread that can be stopped.

    def __init__(self, name, target, args=()):
        super(StoppableThread, self).__init__(name=name, target=target, args=args)
        self._status = 'running'

    def stop_me(self):
        if (self._status == 'running'):
            self._status = 'stopping'

    def stopped(self):
        self._status = 'stopped'

    def is_running(self):
        return (self._status == 'running')

    def is_stopping(self):
        return (self._status == 'stopping')

    def is_stopped(self):
        return (self._status == 'stopped')
