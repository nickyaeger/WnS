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
    alarm = pygame.mixer.Sound('/home/wns/WnS/audio/alarm.wav')
    alarm.play()
    time.sleep(alarm.get_length())

def playPushup():
    pushup = pygame.mixer.Sound('/home/wns/WnS/audio/pushup.wav')
    pushup.play()
    time.sleep(pushup.get_length())