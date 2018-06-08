import sys
sys.path.append('/home/pi/SAKS-SDK')
from sakshat import SAKSHAT
import RPi.GPIO as GPIO
import time
SAKS = SAKSHAT()

GPIO.setmode(GPIO.BCM)

DS = 6
SHCP = 19
STCP = 13

def init():
    GPIO.setup(DS, GPIO.OUT)
    GPIO.setup(SHCP, GPIO.OUT)
    GPIO.setup(STCP, GPIO.OUT)

    GPIO.output(DS, GPIO.LOW)
    GPIO.output(SHCP, GPIO.LOW)
    GPIO.output(STCP, GPIO.LOW)

def writeBit(data):
    GPIO.output(DS, data)
    GPIO.output(SHCP, GPIO.LOW)
    GPIO.output(SHCP, GPIO.LOW)

def writeByte(data):
    for i in range(0, 8):
        writeBit((data >> i) & 0x01)
    GPIO.output(STCP, GPIO.LOW)
    GPIO.output(STCP, GPIO.HIGH)


# Turn off the lights
init()
writeByte(0x00)

while True:
    t = time.strftime("%H.%M", time.localtime())
    SAKS.digital_display.show(t)
    time.sleep(1)
