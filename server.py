import socket
import select

R_CURRENT = 0
G_CURRENT = 0
B_CURRENT = 0

from config import *
from ledFunctions import *
from effectThread import *
from effect_cops import *
from effect_fade import *
from ColorFader import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(31, GPIO.OUT)

led_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
led_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
led_socket.bind((SERVER_IP, SERVER_PORT))
led_socket.listen(5)

print "LED SERVER STARTED AT " + SERVER_IP + " ON PORT: " + str(SERVER_PORT)

oEffectThread = effect_cop(1)
oFadeThread = ColorFader(1,R_CURRENT,G_CURRENT,B_CURRENT,0,0,0)
oFadeThread.start()

read_list = [led_socket]
while True:
    readable, writable, errored = select.select(read_list, [], [])
    for s in readable:
        if s is led_socket:
            client_socket, address = led_socket.accept()
            read_list.append(client_socket)
        else:
            byteData = s.recv(24)
	    data = byteData.decode('utf-8')
            if len(data) > 0:
		if data == "OFF":
			oEffectThread.stopit()
			setRGB(0,0,0)
			print "rgb off"
  
                if data == "CLOFF":
                        GPIO.output(31,GPIO.HIGH)
                        print "CLOFF "
               
                if data == "CLON":
                        GPIO.output(31,GPIO.LOW)
                        print "CLON  "
                        
		if data == "STOP":
			oEffectThread.stopit()

		if data == "COPS":
			oEffectThread.stopit()
			oEffectThread = effect_cop(0.5)
			oEffectThread.start()

		if data == "FADE":
			oEffectThread.stopit()
			oEffectThread = effect_fade(0.03)
			oEffectThread.start()
              
			
                aRGB = data.split(',')
                if len(aRGB) == 3:
			oEffectThread.stopit()

                        r = int(aRGB[0])
                        g = int(aRGB[1])
                        b = int(aRGB[2])			

			if MODE is "fade":
				oFadeThread.stopit()
				oFadeThread = ColorFader(1000,R_CURRENT,G_CURRENT,B_CURRENT,r,g,b)
				oFadeThread.start()
				#BUFFER VALUES TO FADE FROM THERE NEXT TIME
				R_CURRENT = r
				G_CURRENT = g
				B_CURRENT = b
			else:
				setRGB(r,g,b)
            else:
                s.close()
                read_list.remove(s)


