import os, sys
filename = 'robo_commands.txt'
target = open(filename, 'w')
x = 0
while x != chr(27): # ESC
    x=sys.stdin.read(1)[0]
    target.write(x)
    target.flush()
target.close()
