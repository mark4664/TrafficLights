#!/usr/bin/python3

# Mark Bradley
# 2019-12-08
# Simple buzzer script
# pin is the i/o pin the buzzer is connected to.
# duration is thetime to sound the buzzer forin seconds.
                                                                                                                                                           
from gpiozero import Buzzer
from time import sleep          

pin=12        # GPIO pin to connect buzzer to.
duration=5  # Time to sound buzzer in seconds

buzzer=Buzzer(pin)
    
buzzer.on()
sleep(duration)
buzzer.off()
                                                                                                                                                                                                                                                                                                                                                                                                                  
print("All done!")
