import numpy as np
import time
import math

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
        #This reads in barometer and accelerometer and decides velocity
        #THIS NEEDS TO CHANGE BASED ON SENSOR TIMING
        alt_s1 = Sensors.altitude()
        acc_s1 = Sensors.acceleration()
        time.sleep(0.01)
        alt_s2 = Sensors.altitude()
        acc_s2 = Sensors.acceleration()
        altSpeed = (alt_s2-alt_s1)/0.01
        accSpeed = (acc_s2-acc_s1)*0.01
        if altSpeed > 100: #This can change so it makes sense just if its outside of bounds
            return accSpeed
        else:
            return altSpeed
    
    def predicted_alt(alt,velocity): #Maybe read in density too?
        m=15 #kg
        Cd=0.43 #CHANGE HUHHH???
        A=0.0224 #Area without airbrakes (m^2)
        rho=1.056 #Can we read this in with barometer?
        g=9.81 #duh m/s^2) 
        Xc=(m/(rho*Cd*A)*log((m*g+0.5*rho*Cd*A*velocity^2)/(m*g)))+alt;
        return Xc

if __name__ == "__main__":
    Rocket = Controllers()
    Calc = Calculations()
    Sensor = Sensors()
    DesiredAltitude = 5000
    currSpeed = 0

    #Launch Phase
    launch_State = 0
    while launch_State == 0:
        #0 not launched
        #1 is launched
        if Sensors.acceleration() >= 15: #This doesnt really mean anything
            launch_State = 1
        else:
            launch_State = 0

    #Motor Burn
    t_end = time.time() + 5
    while time.time() < t_end:
        currSpeed += Calculations.current_speed() #This just reads the data

    #Apogee
    while currSpeed >= 0:
        currSpeed += Calculations.current_speed()
        total_alt = Calculations.predicted_alt(Sensors.altitude(),currSpeed) #Need to read in alt 
        if total_alt >= 1524: #This is in meters! 
            Controllers.deploy()
        else: #WE might need logic in here that decides if they are not out what should happen
            Controllers.retract()

    Controllers.retract()
