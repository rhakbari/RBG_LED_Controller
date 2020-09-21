import sys
import threading
import time

class StoppableThread(threading.Thread):
    
    def __init__(self):
        super(StoppableThread, self).__init__()
        self._stopper = threading.Event()

    def stopit(self):
	try:
        	self._stopper.set()
	except Error:
		print "NOTHING TO STOP"

    def stopped(self):
        return self._stopper.is_set()
