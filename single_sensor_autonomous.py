from sound_sensor import get_obstacle
from robot_motion import *
import RPi.GPIO as GPIO
import sys, time

set_min_distance = 30
set_number_of_turns = 3
set_time_for_reverse = 2
duration = 0.5
duration_left = 0.5
hold_time = 1

def left():
  print 'L'
  pivot_right(duration_left)
    
try:    
	x = 0
	while(True):
  	  distance = get_obstacle()
	  print distance
 	  if distance < set_min_distance :
		hold(hold_time)
    		left()
	  else:
	    forward(duration)
  	    print 'F'
except KeyboardInterrupt:
	GPIO.cleanup()
	sys.exit()
        


        
