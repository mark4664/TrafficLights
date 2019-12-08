#!/usr/bin/python3

# Script name: TrafficLightSimple.py
# Uses 2 sets of red yellow and green LEDs to simulate a set of road trafficlights at a cross roads
# Light designated North South - ns and East West - ew
# Mark Bradley
# 2019-12-05
# ns LEDs on I/O pins 21,20,16
# ew LEDs on I/O pins 5,6,13
# Simple sequential version. No functions or classes.

from gpiozero import LED, Button    #Using gpiozero library
from time import sleep              #Use sleep funtion for timing, time is in seconds

ns_grn=LED(21)       # Assign pin 21 to the green led.
ns_yel=LED(20)       # Assign pin 20 to the yellow led.
ns_red=LED(16)       # Assign pin 16 to the red led.

ew_grn=LED(5)        # Assign pin 5 to the green led.
ew_yel=LED(6)        # Assign pin 6 to the yellow led.
ew_red=LED(13)       # Assign pin 13 to the red led.

ns_red.on()          # Set both red LEDs on.
ew_red.on()

print("Traffic Light simulation programme")

try:
    while True:            # Run util stopped by keyboard interrupt....Ctrl + C
        ns_red.on()        # Turn LED ON, set output pin to +3.3v
        sleep(1)           # Wait 1 second
        ns_yel.on()        # Repeat for the other the entire sequence.
        sleep(1)
        ns_red.off()
        ns_yel.off()
        ns_grn.on()
        sleep(4)
        ns_grn.off()
        ns_yel.on()
        sleep(1.5)
        ns_yel.off()
        ns_red.on()
        sleep(1)        
        ew_yel.on()     
        sleep(1)
        ew_red.off()
        ew_yel.off()
        ew_grn.on()
        sleep(4)
        ew_grn.off()
        ew_yel.on()
        sleep(1.5)
        ew_yel.off()
        ew_red.on()
        sleep(1)

except (KeyboardInterrupt):   # Run util stopped by keyboard interrupt....Ctrl + C
    pass

ns_grn.off()   # Tidy up and turn all the LEDs off.
ns_yel.off()
ns_red.off()

ew_grn.off() 
ew_yel.off() 
ew_red.off() 

print("All done!")
