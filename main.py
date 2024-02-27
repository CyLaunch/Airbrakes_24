import numpy as np
from helper_objects import cyllogger
import time
import math
from airbrake import airbrake
from helper_objects.cyllogger import cyllogger

# LAUNCH PARAMS
# ----------------------------------------------------------------------
TRGT_ALT_FT = 5000.0 #TODO up to date?
ALT_MAX_SPEED = 670 #TODO Change please, and what unit is this in?
MOTOR_BURN_TIME_S = 3.0
AB_ACTUATION_TIME_S = 10.0
# ----------------------------------------------------------------------

# Airbrakes
ab = airbrake()

# Logger
main_log = cyllogger("main")

def main():
    currSpeed = 0.0

    main_log.writeTo("Entering Detect launch Loop.")
    #Launch Phase
    while ab.detect_launch() == False:
        time.sleep(0.25) 
        main_log.writeTo("Launch Not Detected.")
    main_log.writeTo("Launch Detected! Exiting Loop.")

    # Motor Burn
    main_log.writeTo("Entering motor burn sleep of {} Seconds".format(MOTOR_BURN_TIME_S))
    time.sleep(MOTOR_BURN_TIME_S)
    main_log.writeTo("Exiting motor burn sleep.")
    
    # Apogee
    main_log.writeTo("Entering Aibrake actuation loop. Will timeout in {} seconds".format(AB_ACTUATION_TIME_S))
    timeout = time.time() + AB_ACTUATION_TIME_S
    while timeout >= time.time(): # In total 13 seconds after launch
        currSpeed = Calculations.current_speed()
        total_alt = Calculations.predicted_alt(ab.get_altitude(),currSpeed)
        main_log.writeTo("Predicted Alt: {}ft.".format(total_alt))
        if total_alt >= TRGT_ALT_FT:
            main_log.writeTo("Target altitude exceeded! Deploying airbrakes.")
            ab.deploy_airbrakes()
            main_log.writeTo("Airbrakes deployed.")
        else: 
            ab.retract_airbrakes()
            main_log.writeTo("Airbrakes are retracted.")
    ab.retract_airbrakes()
    main_log.writeTo("Final Time Occured, Retracting airbrakes and exiting loop")

class Calculations:
    def current_speed():
        alt_s1 = ab.get_altitude()
        alt_s2 = ab.get_altitude()
        accSpeed = 0.0
        altSpeed = (alt_s2-alt_s1)/0.02
        if altSpeed > ALT_MAX_SPEED: #This can change so it makes sense just if its outside of bounds
            ab.retract_airbrakes()
            return 1.0
        else:
            return altSpeed
    
    def predicted_alt(alt,velocity): 
        m=30.25 #lbs 
        Cd=0.61 #CHANGE for each rocket!! 
        A= 0.2413 # ft^2 
        rho=0.062 #lbs/ft^3 at 2000ft 
        g=32.16789 #ft/s^2 
        Xc=(m/(rho*Cd*A)*math.log((m*g+0.5*rho*Cd*A*velocity**2)/(m*g)))+alt
        return Xc

if __name__ == "__main__":
    main()
