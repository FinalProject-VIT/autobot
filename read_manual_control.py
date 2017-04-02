import RPi.GPIO as GPIO
import sys
from robot_motion import *
filename = 'robo_commands.txt'
x = 0
direction = 'F'
duration = 1.5

def change_direction(last_line):
  global direction
  if last_line == 'R':
    print 'R'
    direction = 'R'
    pivot_left(duration)
  elif last_line == 'L':
    print 'L'
    direction = 'L'
    pivot_right(duration)
  elif last_line == 'F':
    print 'F'
    direction = 'F'
    forward(duration)
  elif last_line == 'B':
    print 'B'
    direction = 'B'
    reverse(duration)
  elif last_line == 'H':
    print 'H'
    direction = 'H'
    hold(duration)

with open(filename, 'r') as f:
    lines = f.read().splitlines()
    last_line = lines[-1]
    initial = last_line



while(True):
   try: 
  	with open(filename, 'r') as f:
    		lines = f.read().splitlines()
    		last_line = lines[-1]
    	if last_line != initial:
      		initial = last_line
      		change_direction(last_line)
    	else: 
      		print direction
      		change_direction(last_line)
   except KeyboardInterrupt:
   	 GPIO.cleanup()
	 sys.exit()
	
