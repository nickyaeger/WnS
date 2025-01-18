import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

def playWhackamole():
    trigger_pin = 23
    GPIO.setup(trigger_pin, GPIO.OUT, initial=GPIO.HIGH)  # Set initial state to HIGH
    GPIO.output(trigger_pin, GPIO.LOW)  # Trigger active low
    time.sleep(0.1)  # Trigger for 100ms
    GPIO.output(trigger_pin, GPIO.HIGH)  # Reset to inactive
    GPIO.cleanup(trigger_pin)  # Clean up after use

def playMemory():
    trigger_pin = 27
    GPIO.setup(trigger_pin, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.output(trigger_pin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(trigger_pin, GPIO.HIGH)
    GPIO.cleanup(trigger_pin)

def playShake():
    trigger_pin = 21
    GPIO.setup(trigger_pin, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.output(trigger_pin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(trigger_pin, GPIO.HIGH)
    GPIO.cleanup(trigger_pin)

def playJacks():
    trigger_pin = 19
    GPIO.setup(trigger_pin, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.output(trigger_pin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(trigger_pin, GPIO.HIGH)
    GPIO.cleanup(trigger_pin)

def playMenu():
    trigger_pin = 15
    GPIO.setup(trigger_pin, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.output(trigger_pin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(trigger_pin, GPIO.HIGH)
    GPIO.cleanup(trigger_pin)
