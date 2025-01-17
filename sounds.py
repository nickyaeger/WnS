import time
import RPi.GPIO as GPIO

def playWhackamole():
    GPIO.setmode(GPIO.BCM)
    trigger_pin = 23
    GPIO.setup(trigger_pin, GPIO.OUT)
    GPIO.output(trigger_pin, GPIO.LOW)
    time.sleep(0.1)  # Trigger for 100ms
    GPIO.output(trigger_pin, GPIO.HIGH)
    GPIO.cleanup(trigger_pin)

def playMemory():
    GPIO.setmode(GPIO.BCM)
    trigger_pin = 27
    GPIO.setup(trigger_pin, GPIO.OUT)
    GPIO.output(trigger_pin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(trigger_pin, GPIO.HIGH)
    GPIO.cleanup(trigger_pin)

def playShake():
    GPIO.setmode(GPIO.BCM)
    trigger_pin = 21
    GPIO.setup(trigger_pin, GPIO.OUT)
    GPIO.output(trigger_pin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(trigger_pin, GPIO.HIGH)
    GPIO.cleanup(trigger_pin)

def playJacks():
    GPIO.setmode(GPIO.BCM)
    trigger_pin = 19
    GPIO.setup(trigger_pin, GPIO.OUT)
    GPIO.output(trigger_pin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(trigger_pin, GPIO.HIGH)
    GPIO.cleanup(trigger_pin)

def playMenu():
    GPIO.setmode(GPIO.BCM)
    trigger_pin = 15
    GPIO.setup(trigger_pin, GPIO.OUT)
    GPIO.output(trigger_pin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(trigger_pin, GPIO.HIGH)
    GPIO.cleanup(trigger_pin)