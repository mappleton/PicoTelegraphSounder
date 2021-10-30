'''
Raspberry pi pico project to convert text file to morse and
tap it out on a vintage telegraph repeater
Author: Michael Appleton
Date: October 29, 2021
'''
from machine import Pin
from time import sleep
led = Pin(15, Pin.OUT)
led.off()
button = Pin(14, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(13, Pin.IN, Pin.PULL_DOWN)

text_file = open("gettysburg.txt", "r")
text = text_file.read()
message = text.upper()
text_file.close()




morse = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

'''
Farnsworth timing rules:
The length of a dit is 1 time unit.
A dah is 3 time units.
The space between symbols (dits and dahs) of the same letter is 1 time unit.
The space between letters is 3 time units.
The space between words is 7 time units.


'''

unit = .093 #sets speed/wpm @ 93ms ~13wpm

def to_morse(message):
    for char in message:
        if button2.value():
            break
        else:
            print(char)
            if char in morse:
                if char != ' ':
                    m = morse[char]
                    for i in m:
                        if i == '.':
                            led.on()
                            sleep(1*unit)
                            led.off()
                        elif i == '-':
                            led.on()
                            sleep(3*unit)
                            led.off()
                        sleep(1*unit) #time between dit & dah      
                elif char == ' ':
                    sleep(7*unit) #time between words
                sleep(3*unit) #time between characters


while True:
    if button.value():
        to_morse(message)

