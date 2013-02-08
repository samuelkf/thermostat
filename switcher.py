#!/usr/bin/env python
import RPi.GPIO as GPIO
from sys import argv

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT)

if argv[1] == '1':
	GPIO.output(22, GPIO.HIGH)
else:
	GPIO.output(22, GPIO.LOW)
