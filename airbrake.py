#----------------------------------------------------
# Airbrakes object for reading from airbrake sensors
# and actuating the airbrake servo.
# 
# @Author bdpope
# CyLaunch 2023-24
#----------------------------------------------------
from helper_objects.barometer import barometer
from helper_objects.accelerometer import accelerometer
from helper_objects.cyllogger import cyllogger
from helper_objects.servo import servo
from helper_objects.cylloggerCSV import cylloggerCSV

#----------------------------------------------------
# Constants
#----------------------------------------------------
airbrake_deployment_angle = 170
launch_detection_magnitude = 30

class airbrake:
    def __init__(self):
        self.logger = cyllogger("airbrakes")
        self.loggerCSV = cylloggerCSV("airbrakes")
        self.accelerometer = accelerometer()
        self.barometer = barometer()
        self.servo = servo(18) # Servo is on pin 18
        self.airbrake_tare_value = 0
        self.tare_barometer() # zeros the baro to local altitude
        

    def deploy_airbrakes(self):
        self.servo.move(airbrake_deployment_angle)
    
    def retract_airbrakes(self):
        self.servo.move(0)

    #TODO Confirm the launch detection magnitude
    def detect_launch(self):
        avg = 0.0
        for i in range(2):
            avg += self.accelerometer.accel_magnitude()
        avg = avg / 3

        if(avg > launch_detection_magnitude):
            return True
        else:
            return False

    def get_accel_mag(self):
        return self.accelerometer.accel_magnitude()

    def get_altitude(self):
        print("AB tare value: " + str(self.airbrake_tare_value))
        b = (self.barometer.get_altitude() - self.airbrake_tare_value)
        self.loggerCSV.writeTo(b)
        return b    

    def get_acceleration(self):
        return self.accelerometer.accel()
    
    def tare_barometer(self):
        sum = 0.0
        for x in range(5): # Runs 5 times
            sum += self.get_altitude()
        avg = sum / 5.0
        print("Barometer tare set to {}".format(avg))
        self.airbrake_tare_value = avg
        self.logger.writeTo("Barometer zero value set to {}".format(self.airbrake_tare_value))
        