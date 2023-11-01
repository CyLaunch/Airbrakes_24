import numpy as np
from scipy import signal
from gpiozero import Barometer,Accelerometer
from signal import pause
import time
import math

altitude = Barometer()#Pin
accelerometer = Accelerometer()#Pin

class Controllers:
    def __init__(self):
        # Initialize your hardware interface here (e.g., GPIO pins, servos, etc.)
        pass

    def deploy(self):
        # Code to deploy the airbrakes
        pass

    def retract(self):
        # Code to retract the airbrakes
        pass
    
    def state(self):
        #determine what the state of airbrakes is 
        #return state
        pass

class Sensors:
    def altitude(self):
        #Read in barometer? 
        #return alt
        pass

    def acceleration(self):
        #Filter
        #Return acceleration in Z direction
        pass

class Calculations:
    def current_speed(self):
        alt_s1 = Sensors.altitude()
        acc_s1 = Sensors.acceleration()
        time.sleep(0.01)
        alt_s2 = Sensors.altitude()
        acc_s2 = Sensors.acceleration()
        altSpeed = (alt_s2-alt_s1)/0.01
        accSpeed = (acc_s2-acc_s1)*0.01
        if accSpeed > 100: #This can change so it makes sense
            return altSpeed
        else:
            return accSpeed

    def desired_speed(alt):
        deltaAlt = alt - Sensors.altitude()
        speed = math.sqrt(2(Sensors.acceleration()*deltaAlt))
        return speed
    

class ControlLogic:
    def launch(self):
        #0 not launched
        #1 is launched
        if Sensors.acceleration() >= 15: #
            return 1 
        else:
            return 0

    def deployment(alt): 
        if Calc.current_speed() > Calc.desired_speed(alt):
            Rocket.deploy()
        
        elif Rocket.state() == 1:
            Rocket.retract()


if __name__ == "__main__":
    Rocket = Controllers()
    Calc = Calculations()
    DesiredAltitude = 5000

    #Launch Phase
    launchState = ControlLogic.launch()
    while launchState == 0:
        launchState = ControlLogic.launch()

    #Motor Burn
    time.sleep(5)

    #Apogee
    currSpeed = Calculations.current_speed()
    while currSpeed >= 0:
        ControlLogic.deployment(DesiredAltitude)
