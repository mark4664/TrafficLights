#!/usr/bin/python3

# Script name: TrafficLightFunction.py
# Uses the red, yellow and green LEDs to simulate a road traffic light
# 
# Mark Bradley
# 2019-12-05
# Code divided into functions.
# To exit the code use <ctrl> + c or click the stop button in Thonny

# Import additional libraries.
from gpiozero import LED          #Using gpiozero library, LED object used for each LED
from time import sleep            #Use sleep funtion for timing, time is in seconds

ns_grn=LED(21)       # Assign pin 21 to the green led.
ns_yel=LED(20)       # Assign pin 20 to the yellow led.
ns_red=LED(16)       # Assign pin 16 to the red led.

ew_grn=LED(5)        # Assign pin 5 to the green led.
ew_yel=LED(6)        # Assign pin 6 to the yellow led.
ew_red=LED(13)       # Assign pin 13 to the red led.

ns_red.on()          # Set both red LEDs on.
ew_red.on()

def traffic_light_ns():
    # Run through a single sequence of the North South traffic lights
    ns_red.on()       # Turn LED ON, set output pin 'on' this puts +3.3v on the IO pin.
    sleep(1)          # Wait 1 seconds
    ns_yel.on()       # Repeat for the other LEDs
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
    
def traffic_light_ew():
    # Run through a single sequence of East West traffic lights
    ew_red.on()       # Turn LED ON, set output pin 'on' this puts +3.3v on the IO pin.
    sleep(1)          # Wait 1 seconds
    ew_yel.on()       # Repeat for the other LEDs
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
    
def clean_exit():
    # On exit turn all the LEDs off.
    ns_grn.off()
    ns_yel.off()
    ns_red.off()

    ew_grn.off() 
    ew_yel.off() 
    ew_red.off()

#------ Start of the main block of code ------

print("Traffic Light simulation programme")

try:
    while True:    # Run utill <ctrl> C is pressed.
        traffic_light_ns()
        traffic_light_ew()
        
except (KeyboardInterrupt):   # Run util stopped by keyboard interrupt....Ctrl + C
    clean_exit()
    
print('All Done')
        
        
        
        

