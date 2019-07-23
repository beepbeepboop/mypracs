#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names:  Declan Molloy
Student Number: MLLDEC001
Prac: 1
Date:  04/08/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import itertools
import time

# Logic that you write
countValues =list(itertools.product([0,1],repeat=3))  #creates a list of increments in binary
counter = 0 #counter used for display updating

def main():
	#GPIO setup
	inputs = [16,18]
	outputs = [11,13,15]
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(outputs, GPIO.OUT) #selects the pins for output mode
	GPIO.setup(inputs,GPIO.IN, pull_up_down =GPIO.PUD_UP) #selects which pins are inputs
	#interupt detectors for buttons being pressed
	GPIO.add_event_detect(16, GPIO.FALLING, callback=increment, bouncetime=250)
	GPIO.add_event_detect(18, GPIO.FALLING, callback=decrement, bouncetime=250)

	#infinite loop
	while True:
		update()
		time.sleep(0.5)

#main function
def update():
	global counter
	#updates the 3 different digits of the counter
	GPIO.output(11, countValues[counter][0])
	GPIO.output(13, countValues[counter][1])
	GPIO.output(15, countValues[counter][2])

def increment(): #activates when the interupt for the increment button is pressed
	global counter
	counter=counter+1
	if counter >7: #resets counter when it reaches max
		counter =0
	print("wow you just incremented by 1!")

def decrement(): #activates when the interupt for the decrement button is pressed
	global counter
	counter = counter-1
	if counter <0:
		counter =7 #resets the counter when it reaches minimum
	print("wow you just decremented by 1!")


# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
	GPIO.setwarnings(False)
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
