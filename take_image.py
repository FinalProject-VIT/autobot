import os
import sys
os.system('rm ./images/*.jpg')
os.system('raspistill -o ./images/clicked.jpg')

path_remove_pass = './images/'
try:
	while True:
		message = 'not done'
		for file in os.listdir(path_remove_pass):
			if file == 'remove_pass.jpg':
				os.system('rm ./images/*.jpg')
				message = 'done'
				break
		if message == 'done':
			break
except KeyboardInterrupt:
	os.system('rm ./images/*.jpg')
	sys.exit()
