from effectThread import *
from ledFunctions import *

class effect_cop(StoppableThread):
    import time

    iInterval = 1

    BUFFER_EFFECT_COPS = 1
    def effect_cops(self):
        if self.BUFFER_EFFECT_COPS == 1:
                setRGB(255,0,0)
                self.BUFFER_EFFECT_COPS = 0
        else:
                setRGB(0,0,255)
                self.BUFFER_EFFECT_COPS = 1


    def __init__(self, iInterval):
      self.iInterval = iInterval
      StoppableThread.__init__(self)

    def run(self):
        while not self.stopped():
                self.effect_cops()
                time.sleep(self.iInterval)
