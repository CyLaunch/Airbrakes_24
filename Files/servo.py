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

s = servo(18)


#25 is about 0
#s.move(25)
#sleep(2)
#s.move(180)
#s.move(60)

while True:
    # 0 is closed, 180 is open
    user_input = input("Please enter 'z' 'x' 'c' for 0, 60, 180; or 'i' for input, or 'q' to end the program: ")
    #s.move(user_input)
    if user_input == 'c':
        s.move(0)
    elif user_input == 'x':
        s.move(60)
    elif user_input == 'z':
        s.move(180)
    elif user_input == 'i':
        while True:
            int_input = int(input("Enter a num between 0 and 180: "))
            if int_input == 420:
                break
            else:
                s.move(int_input)
    elif user_input == 'q':
        s.__del__()
        quit()


#s.ChangeDutyCycle(5)
#s.ChangeDutyCycle(0)

sleep(1)

s.__del__()
