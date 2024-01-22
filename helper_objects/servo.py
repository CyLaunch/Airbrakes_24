import RPi.GPIO as GPIO
from time import sleep
freq_hz = 50

class servo:
    def __init__(self, pin_num):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin_num, GPIO.OUT)
        GPIO.setwarnings(False)
        self.p = GPIO.PWM(pin_num, 50) 
        self.p.start(0)

    def move(self, angle):
        newDC = 2.5 + (angle / 18.95)
        self.p.ChangeDutyCycle(newDC)
        sleep(1)

    def __del__(self):
        GPIO.cleanup()