#!/usr/bin/python3

# Script name: TrafficLightClass.py
# Use 2 sets the red, yellow and green LEDs to simulate traffic lights at a cross roads
# 
# Mark Bradley
# 01/12/19
# Traffic signal class used twice to create a pair of lights to control a junction.
# Stop and Go methods to set the lights as required.

# Import additional libraries.
from gpiozero import LED     #Using gpiozero library, LED object used for each LED
from time import sleep       #Use sleep funtion for timing, time is in seconds
        
class traffic_signal:
    def __init__(self,grn,yel,red): # Parameters grn yel & red contain IO pins for LED
        self.grn_led=LED(grn)       # Assign pin grn to the green led (grn_led) etc.
        self.yel_led=LED(yel)       
        self.red_led=LED(red)
        self.red_led.on()           #Set the traffic signal to Red
        
    def terminate(self):
        self.grn_led.off()
        self.red_led.off()
        self.yel_led.off()
        
    def go(self):      # Change traffic signal from Red to Green
        self.yel_led.on()       
        sleep(1)
        self.red_led.off()
        self.yel_led.off()
        self.grn_led.on()
                    
    def stop(self):    # Change traffic signal from Green to Red
        self.grn_led.off()
        self.yel_led.on()
        sleep(1.5)
        self.yel_led.off()
        self.red_led.on()
        
#Initalise 2 traffic light objects tl_ns North South and tl_ew East West
 
tl_ns=traffic_signal(21,20,16)   # Configure traffic lights for cross roads, the parameters are the I/O pin numbers.
tl_ew=traffic_signal(5,6,13)   # North-South (ns) East-West (ew) junction

#------ Start of the main block of code ------

print("Traffic Light simulation programme - Class Version")

try:
    while True:    # Run utill <ctrl> C is pressed
       tl_ns.go()
       sleep(4)
       tl_ns.stop()
       sleep(1)
       tl_ew.go()
       sleep(4)
       tl_ew.stop()
       sleep(1)
        
except (KeyboardInterrupt):   # Run util stopped by keyboard interrupt....Ctrl + C
    pass
  
tl_ns.terminate()  # Turn all the LEDs off
tl_ew.terminate()

print('All done!')

