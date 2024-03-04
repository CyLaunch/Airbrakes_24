# Command: pytest calculations_test.py
# Add the -s flag if you want the print statements to come out
# from main import Calculations
import numpy as np

data = [
    # Velocity  Altitude    Expected Prediction
    (   0.0,    5000,       5000),    
    (   0.0,    2500,       2500)
    ]

# calcs = Calculations()
pred_alt = 0

def predicted_alt(alt,velocity): #Maybe read in density too?
        m=33.0693 #lbs 
        Cd=0.61 #CHANGE for each rocket!! 
        A= 0.2411 # ft^2 TODO Brenner check that this seems right
        rho=0.069607176 #lbs/ft^3 at 2000ft 
        g=32.16789 #ft/s^2 
        Xc=(m/(rho*Cd*A)*np.log10((m*g+0.5*rho*Cd*A*velocity**2)/(m*g)))+alt
        return Xc

def test_calculations():
    # Runs each velocity/altitude combo
    for vel, alt, ex_pred_alt in data:
        pred_alt = predicted_alt(alt, vel)
        print("Velocity: {} Altitude: {} predicted Alt: {}".format(vel, alt, pred_alt))
        assert pred_alt == ex_pred_alt

if __name__ == "__main__":
    test_calculations()