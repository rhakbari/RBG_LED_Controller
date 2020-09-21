from config import *


def setLights(pin, brightness):
        realBrightness = int(int(brightness) * (float(MAX_BRIGHTNESS) / 255.0))
        pi.set_PWM_dutycycle(pin, realBrightness)

def setRGB(r,g,b):
	if r > 255:
		r = 255
	if g > 255:
		g = 255
	if b > 255:
		b = 255

	if r < 0:
		r = 0
	if g < 0:
		g = 0
	if b < 0:
		b = 0
	
        setLights(RED_PIN, r)
        setLights(GREEN_PIN, g)
        setLights(BLUE_PIN,b)
        
