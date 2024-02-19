import numpy as np
from helper_objects import cyllogger
import time
import math
from airbrake import airbrake
from helper_objects.cyllogger import cyllogger

# LAUNCH PARAMS
# ----------------------------------------------------------------------
TRGT_ALT_FT = 5000.0 #TODO up to date?
ALT_MAX_SPEED = 100.0 #TODO Change please, and what unit is this in?
# ----------------------------------------------------------------------

# Airbrakes
ab = airbrake()

# Logger
main_log = cyllogger("main")

def main():
    Calc = Calculations()
    currSpeed = 0.0

    #Launch Phase
    launch_State = False
    while launch_State == False:
        launch_State = ab.detect_launch()
        time.sleep(0.25) 
        launch_State = True

    # Motor Burn
    time.sleep(1.1)
    
    # Apogee
    timeout = time.time() + 10 #Change this 6 to change time of airbrake logic
    while timeout >= time.time(): #In total 11 seconds after launch
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
        # timeout += time.time() - This doesn't make sense as time.time() is total seconds since the epoch,
        # Therefore adding this will make the loop last forever

    ab.retract_airbrakes()

class Calculations:
    def current_speed():
        #This reads in barometer and accelerometer and decides velocity
        #THIS NEEDS TO CHANGE BASED ON SENSOR TIMING
        alt_s1 = ab.get_altitude()
        alt_s2 = ab.get_altitude()
        #print("alt_s1, alt_s2 " + str(alt_s1) + " " + str(alt_s2))
        accSpeed = 0.0
        altSpeed = (alt_s2-alt_s1)/0.02
        if altSpeed > ALT_MAX_SPEED: #This can change so it makes sense just if its outside of bounds
            print("else taken")
            ab.retract_airbrakes()
            acc_s1 = ab.get_acceleration()
            acc_s2 = ab.get_acceleration()
            accSpeed += (acc_s2-acc_s1)*0.02
            return accSpeed
        else:
            return altSpeed
    
    def predicted_alt(alt,velocity): #Maybe read in density too?
        m=33.0693 #lbs 
        Cd=0.61 #CHANGE for each rocket!! 
        A= 0.2411 # ft^2 TODO Brenner check that this seems right
        rho=0.069607176 #lbs/ft^3 at 2000ft 
        g=32.16789 #ft/s^2 
        Xc=(m/(rho*Cd*A)*math.log((m*g+0.5*rho*Cd*A*velocity**2)/(m*g)))+alt
        return Xc

if __name__ == "__main__":
    main()