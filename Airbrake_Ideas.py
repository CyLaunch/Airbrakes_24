import numpy as np
from helper_objects import cyllogger
import time
import math
from airbrake import airbrake

#THIS IS IN IMPERIAL UNITS!!!!!
ab = airbrake()
accSpeed = 0.0

#Loggers
#ab_log = cyllogger("Airbrake")
#alt_predict_log = cyllogger("Prediction_Alt")
#vel_log = cyllogger("Velocity")
#launch_log = cyllogger("Launch")
class Calculations:
    def current_speed(self):
        #This reads in barometer and accelerometer and decides velocity
        #THIS NEEDS TO CHANGE BASED ON SENSOR TIMING
        alt_s1 = ab.get_altitude()
        alt_s2 = ab.get_altitude()
        altSpeed = (alt_s2-alt_s1)/0.02
        if altSpeed > 1000: #This can change so it makes sense just if its outside of bounds
            return altSpeed
        else:
            ab.retract_airbrakes()
            acc_s1 = ab.get_acceleration()
            acc_s2 = ab.get_acceleration()
            accSpeed += (acc_s2-acc_s1)*0.02
            return accSpeed
    
    def predicted_alt(alt,velocity): #Maybe read in density too?
        m=33.0693 #lbs 
        Cd=0.61 #CHANGE for each rocket!! 
        A=0.0224 #Area without airbrakes (m^2)
        rho=0.069607176 #lbs/ft^3 at 2000ft 
        g=32.16789 #ft/s^2 
        print(velocity)
        Xc=(m/(rho*Cd*A)*np.log10((m*g+0.5*rho*Cd*A*velocity**2)/(m*g)))+alt
        #alt_predict_log.writeto(Xc)
        #print(Xc)
        return Xc

if __name__ == "__main__":
    Calc = Calculations()
    DesiredAltitude = 5000.0 #Altitude in Feet
    currSpeed = 0.0

    #Launch Phase
    launch_State = False
    while launch_State == False:
        launch_State = ab.detect_launch()
        time.sleep(0.25) 

    #Motor Burn
    time.sleep(1.1)

    #Apogee
    timeout = time.time() + 10 #Change this 6 to change time of airbrake logic
    while timeout >= time.time(): #In total 11 seconds after launch
        currSpeed = Calculations.current_speed()
        total_alt = Calculations.predicted_alt(ab.get_altitude(),currSpeed) 
        if total_alt >= DesiredAltitude: #This is in meters! 
            ab.deploy_airbrakes()
        else: 
            ab.retract_airbrakes()
            #print('Closing')
        timeout += time.time()

    ab.retract_airbrakes()
