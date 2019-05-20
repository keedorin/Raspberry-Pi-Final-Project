from Tkinter import *
import Tkinter
import time
import speech_recognition as sr
import os
from socket import *
from Cheese import *
host = "138.47.139.129" # IP Address of server
port = 2041
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
x = 0
GPIO.setwarnings(False)
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    'a':'.-','b':'-...', 'c':'-.-.',
                    'd':'-..','e':'.', 'f':'..-.',
                    'g':'--.','h':'....', 'i':'..',
                    'j':'.---','k':'-.-', 'l':'.-..',
                    'm':'--','n':'-.', 'o':'---',
                    'p':'.--.','q':'--.-', 'r':'.-.',
                    's':'...','t':'-', 'u':'..-',
                    'v':'...-','w':'.--', 'x':'-..-',
                    'y':'-.--','zq1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', '-':' '}
 
def do_something():
    global speech
    global data
    global addr
    data = "Sorry could not recognize what you said"
    r = sr.Recognizer()
    r.energy_threshold=4000
    label.update()
    if x == 1:
        print "Sending..."
        with sr.Microphone(chunk_size = 512) as source:
            audio = r.listen(source)
            try:
                print "Starting..."
                speech = r.recognize_google(audio)
                data = speech
                label.configure(text="You said : {}".format(speech))
                print "Done"
                print "You said " + data
                print " "
                UDPSock.sendto(data, addr)
            except:
                label.configure(text="Sorry could not recognize what you said")

    else:
        print "Receiving"
        (data, addr) = UDPSock.recvfrom(buf)
        label.configure(text="Receiving".format(speech))
        speech = data
        print "Received " + speech
        label.configure(text="Received: {}".format(speech))
        print " "

def encrypt(message):
    global cipher
    cipher = ''
    for letter in message: 
        if letter != ' ': 
            cipher += MORSE_CODE_DICT[letter] + ' '
        else: 
            cipher += ' '
    return cipher

def bop():
    global label
    global x 
    root = Tk()
    root.attributes("-topmost", True)

    if x ==0:
        label = Label(root, wraplength = 700, height=7,  width=25, text="Receiving...", bg="white", fg="black", font=("TexGyreAdventor", 35))
        label.pack(fill=BOTH, expand = 1)
    if x ==1:
        label = Label(root, wraplength = 700, height=7,  width=25, text="Speak Anything...", bg="white", fg="black", font=("TexGyreAdventor", 35))
        label.pack(fill=BOTH, expand = 1)
        
    do_something()
    GPIO.setmode(GPIO.BCM)
    led = 6
    GPIO.setup(led, GPIO.OUT)
    cipher = encrypt(speech)
    
    if x ==0:
        sound(cipher)
        GPIO.cleanup()
        
    boom = Label(root, wraplength = 700, text="{}".format(cipher), bg="white", fg="black", font=("TexGyreAdventor", 35))
    boom.pack(fill=BOTH, expand = 1)
    soap()

def soap():
    root = Tk()
    b1 = Tkinter.Button(root, text="Send Message", command=send, height = 17, width = 30, font=("TexGyreAdventor", 15))
    b2 = Tkinter.Button(root, text="Receive Message", command=receive, height = 17, width = 30, font=("TexGyreAdventor", 15))
    b1.pack(side=LEFT)
    b2.pack(side=RIGHT)
    root.mainloop()

def send():
    global x
    x = 1
    bop()

def receive():
    global x
    x = 0
    bop()
soap()



