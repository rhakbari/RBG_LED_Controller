from effectThread import *
from ledFunctions import *

class effect_fade(StoppableThread):
        import time
        iInterval = 1

        rCurrent = 240
        gCurrent = 80
        bCurrent = 160

        iSpeedR = 1
	iSpeedG = 1
	iSpeedB = 1

	rMin = 50
	gMin = 50
	bMin = 50

	rMax = 255
	gMax = 255
	bMax = 255

	def __init__(self, iInterval):
      		self.iInterval = iInterval
      		StoppableThread.__init__(self)

 	def run(self):
		while not self.stopped():
	        	self.effect_fade()
		        time.sleep(self.iInterval)

        def effect_fade(self):
		# CALCULATE NEW RGB
		self.rCurrent += self.iSpeedR
		self.gCurrent += self.iSpeedG
		self.bCurrent += self.iSpeedB

		#RED UP
		if self.rCurrent >= self.rMax:
			self.rCurrent = self.rMax
			self.iSpeedR *= -1

		#GREEN UP
		if self.gCurrent >= self.gMax:
			self.gCurrent = self.gMax
			self.iSpeedG *= -1

		#BLUE UP
		if self.bCurrent >= self.bMax:
			self.bCurrent = self.bMax
			self.iSpeedB *= -1
		
		#RED DOWN
		if self.rCurrent <= self.rMin:
			self.rCurrent = self.rMin
			self.iSpeedR *= -1

		#GREEN DOWN
		if self.gCurrent <= self.gMin:
			self.gCurrent = self.gMin
			self.iSpeedG *= -1

		#BLUE DOWN
		if self.bCurrent <= self.bMin:
			self.bCurrent = self.bMin
			self.iSpeedB *= -1

		#SET COLOR
		setRGB(self.rCurrent,self.gCurrent,self.bCurrent)


               
