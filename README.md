#LED-Server

This Script can be used on a Raspberry Pi to Control a RGB-Led Strip connected to its GPIO-Pins.
The Script creates a Socket and waits for Commands to set the Color of your LED-Strip.

An Android App to Control the LED-Strip via Wifi can be found here: [Android LED-Controller App](https://github.com/simondankelmann/LED_Controller)

In Order to use it you will need the PIGPIOD Library installed on your Raspberry Pi, have a look at it here:
http://abyz.co.uk/rpi/pigpio/

Before you start the script (after installing PIGPIOD) you need to run:

`sudo pigpiod`

to start it as a daemon.
Set the IP-Address and Port in the Script to your local Settings.



#Update 02. Aug. 2016



##Autostart as systemd service: 
You can also setup a systemd service on your Raspberry Pi in order to autorun PIGPIOD and the LED-server at startup. Just follow [this guide](http://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/). Before step 2 you need to create a shell script that starts PIGPIOD and the Led-Server. Create the file /home/pi/Desktop/rgbservice.sh (or any other location) with the following content:

`sudo pigpiod`

`sudo /usr/bin/python /LOCATION/TO/server.py`

Then in step 2, change the line starting with ExecStart to the following:

`ExecStart=/bin/bash /home/pi/Desktop/rgbservice.sh`

Apart from that, just follow all steps of the guide.

##Autostart with rc.local:
Just copy the following lines into /etc/rc.local (before the line `exit 0`):

`/DIRECTORY/TO/pigpiod`
`/usr/bin/python /DIRECTORY/TO/server.py &`

After that just reboot:
`sudo reboot`

#Setup
Here's how to wire it, in my case i used **STP16NF06L Mosfets** (The RGB-Led in this Picture can be replaced by a RGB-Led Strip):

![](https://github.com/simondankelmann/LED-Server/blob/master/Server-Setup.png)
