import time

import pygame
pygame.init()

def playWhackamole():
    whackamole = pygame.mixer.Sound('/home/wns/WnS/audio/whackamole.wav')
    whackamole.play()
    time.sleep(whackamole.get_length())

def playMemory():
    memory = pygame.mixer.Sound('/home/wns/WnS/audio/memory.wav')
    memory.play()
    time.sleep(memory.get_length())

def playShake():
    shake = pygame.mixer.Sound('/home/wns/WnS/audio/shake.wav')
    shake.play()
    time.sleep(shake.get_length())

def playJump():
    jump = pygame.mixer.Sound('/home/wns/WnS/audio/jump.wav')
    jump.play()
    time.sleep(jump.get_length())

def playMenu():
    menu = pygame.mixer.Sound('/home/wns/WnS/audio/menu.wav')
    menu.play()
    time.sleep(menu.get_length())

def playAlarm():
    alarm = pygame.mixer.Sound('/home/wns/WnS/audio/repeat.wav')
    alarm.play()
    time.sleep(alarm.get_length())

def playPushup():
    pushup = pygame.mixer.Sound('/home/wns/WnS/audio/pushup.wav')
    pushup.play()
    time.sleep(pushup.get_length())

def playOne():
    one = pygame.mixer.Sound('/home/wns/WnS/audio/one.wav')
    one.play()
    time.sleep(one.get_length())

def playTwo():
    two = pygame.mixer.Sound('/home/wns/WnS/audio/two.wav')
    two.play()
    time.sleep(two.get_length())

def playThree():
    three = pygame.mixer.Sound('/home/wns/WnS/audio/three.wav')
    three.play()
    time.sleep(three.get_length())

def playFour():
    four = pygame.mixer.Sound('/home/wns/WnS/audio/four.wav')
    four.play()
    time.sleep(four.get_length())

def playFive():
    five = pygame.mixer.Sound('/home/wns/WnS/audio/five.wav')
    five.play()
    time.sleep(five.get_length())

def playSix():
    six = pygame.mixer.Sound('/home/wns/WnS/audio/six.wav')
    six.play()
    time.sleep(six.get_length())

def playSeven():
    seven = pygame.mixer.Sound('/home/wns/WnS/audio/seven.wav')
    seven.play()
    time.sleep(seven.get_length())

def playEight():
    eight = pygame.mixer.Sound('/home/wns/WnS/audio/eight.wav')
    eight.play()
    time.sleep(eight.get_length())

def playNine():
    nine = pygame.mixer.Sound('/home/wns/WnS/audio/nine.wav')
    nine.play()
    time.sleep(nine.get_length())

def playTen():
    ten = pygame.mixer.Sound('/home/wns/WnS/audio/ten.wav')
    ten.play()
    time.sleep(ten.get_length())