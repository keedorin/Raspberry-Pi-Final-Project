import RPi.GPIO as GPIO
import time
import pygame
    # to use Raspberry Pi board pin numbers
Rate = 0.090
pygame.init()


GPIO.setmode(GPIO.BCM)
led = 6


GPIO.setup(led,GPIO.OUT)

def morse_line():
    sounds2.play()
    GPIO.output(6, True)
    time.sleep(3*Rate)
    GPIO.output(6,False)
    time.sleep(Rate)


def morse_dot():
    sounds.play()
    GPIO.output(6, True)
    time.sleep(Rate)
    GPIO.output(6,False)
    time.sleep(Rate)

def sound(a):
    text = a
    for i in range(len(text)):
        if (text[i]== '-'):
            morse_line()
        elif (text[i]== '.'):
            morse_dot()
        elif (text[i]== ' '):
            time.sleep(7*Rate)
        else:
            Writeline("invalid char")

sounds = pygame.mixer.Sound("dot.wav")
sounds2 = pygame.mixer.Sound("dash.wav")
            
        

GPIO.cleanup()

