#----------------------------------------------------
# Accelerometer object for the ICM20649
# @Author Cam or Marcus?
# CyLaunch 2023-24
#----------------------------------------------------

import time
import board
import adafruit_icm20x

class accelerometer:

    def __init__(self):
        self.i2c = board.I2C()  
        self.icm = adafruit_icm20x.ICM20649(self.i2c)

        self.iterations = 500

        self.icm.accelerometer_data_rate_divisor = 20
        self.icm.gyro_data_rate_divisor = 0

        self.accelRate = self.icm.accelerometer_data_rate
        self.gyroRate = self.icm.gyro_data_rate
        
        self.gyroRange = self.icm.gyro_range
        self.accelRange = self.icm.accelerometer_range

    def gyro(self):
        return self.icm.gyro
        
    # Returns a touple of the x, y, & z accelerations
    def accel(self):
        return self.icm.acceleration

    # Returns the maginitude of the X, Y, & Z
    # Accelerations in meters
    def accel_magnitude(self):
        data = self.accel()
        cnt = 0
        accel_sum = 0
        for x in data:
            cnt = cnt + 1
            accel_sum = accel_sum + x

        return (accel_sum / cnt)

        
    
         

## Example
# a = accelerometer()

# for i in range(a.iterations):
#     print("Gyro value is:", a.gyro())
#     print("Accelerometer value is:", a.accel())
#     time.sleep(1)