import socket
import select
from config import *
from ledFunctions import *
from effectThread import *
from effect_cops import *
from effect_fade import *

class ColorFader(StoppableThread):
	import time

	iInterval = 1
	iDuration = 1000

	rCurrent = 0
	gCurrent = 0
	bCurrent = 0

	rFinal = 0
	gFinal = 0
	bFinal = 0

	rSpeed = 0
	gSpeed = 0
	bSpeed = 0

	def fadeColor(self):
		self.rCurrent += self.rSpeed
		self.gCurrent += self.gSpeed
		self.bCurrent += self.bSpeed
		#CHECK IT ITS READY
		self.check()
		#SET CALCULATED COLOR
		setRGB(self.rCurrent, self.gCurrent, self.bCurrent)

	def check(self):
		rEnd = False
		gEnd = False
		bEnd = False

		#RED
		if self.rSpeed <= 0 and self.rCurrent <= self.rFinal:
			rEnd = True
			self.rCurrent = self.rFinal

		if self.rSpeed > 0 and self.rCurrent >= self.rFinal:
			rEnd = True
			self.rCurrent = self.rFinal

		#GREEN
		if self.gSpeed <= 0 and self.gCurrent <= self.gFinal:
			gEnd = True
			self.gCurrent = self.gFinal

		if self.gSpeed > 0 and self.gCurrent >= self.gFinal:
			gEnd = True
			self.gCurrent = self.gFinal

		#BLUE
		if self.bSpeed <= 0 and self.bCurrent <= self.bFinal:
			bEnd = True
			self.bCurrent = self.bFinal

		if self.bSpeed > 0 and self.bCurrent >= self.bFinal:
			bEnd = True
			self.bCurrent = self.bFinal

		#CHECK IF ITS READY
		if rEnd and gEnd and bEnd:
			self.stopit()
		


	def __init__(self, iDuration, rStart,gStart,bStart,rFinal,gFinal,bFinal):
		self.iDuration = iDuration
		self.iInterval = 1 / iDuration  
		StoppableThread.__init__(self)

		self.rCurrent = rStart
		self.gCurrent = gStart
		self.bCurrent = bStart

		self.rFinal = rFinal
		self.gFinal = gFinal
		self.bFinal = bFinal
		
		#RED
		rDifference = self.rFinal - self.rCurrent
		self.rSpeed = rDifference / self.iDuration
		if not rDifference is 0 and self.rSpeed is 0:
			self.rSpeed = 1
		 

		#GREEN
		gDifference = self.gFinal - self.gCurrent
		self.gSpeed = gDifference / self.iDuration
		if not gDifference is 0 and self.gSpeed is 0:
			self.gSpeed = 1

		#BLUE
		bDifference = self.bFinal - self.bCurrent
		self.bSpeed = bDifference / self.iDuration
		if not bDifference is 0 and self.bSpeed is 0:
			self.bSpeed = 1
		

	def run(self):
		while not self.stopped():
			self.fadeColor()
			time.sleep(self.iInterval)

#oEffectThread = ColorFader(1000,255,0,0,0,255,0)
#oEffectThread.start()


