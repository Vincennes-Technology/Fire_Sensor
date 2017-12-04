#!/usr/bin/env python
# Joel Oliphant
# Fire Sensor
# Code Credit
# https://www.sunfounder.com/learn/sensor-kit-v2-0-for-raspberry-pi-b-plus/lesson-21-flame-sensor-sensor-kit-v2-0-for-b-plus.html
# I have modified small parts of the code.

import socket
import RPi.GPIO as GPIO
import time
import Adafruit_CharLCD as LCD

SERVERIP = '10.0.0.22'

lcd = LCD.Adafruit_CharLCDPlate()

DO = 17

n = 0

GPIO.setmode(GPIO.BCM)

def setup():

    GPIO.setup(DO, GPIO.IN)

def xprint(x):
    if x == 1:
        lcd.clear()
        lcd.message("Dude Cold!!!")
        print "Dude Cold!!!"
    if x == 0:
        global n
        lcd.clear()
        lcd.message("Dude Fire!!!")
        print "Dude Fire!!!"
        n = n +1
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((SERVERIP, 8881))
        print "%d : Connected to server" % n,
        data = "Joel is on fire!!!"
        sock.sendall(data)
        print"Sent:", data
        sock.close( )

def loop():
    status = 1
    while True:
        tmp = GPIO.input(DO)
        if tmp != status:
            xprint(tmp)
            status = tmp
            
        time.sleep(0.2)

if __name__ == '__main__':
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        pass
