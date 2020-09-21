#!/bin/bash 
SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

#STOP POSSIBLE RUNNING PIGPIOD
sudo killall pigpiod
#START PIGPIOD
sudo pigpiod
#START LED-SERVER
sudo python $SCRIPTPATH/server.py
