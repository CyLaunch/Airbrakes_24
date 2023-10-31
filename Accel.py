import time
import board
import adafruit_icm20x

class accelerometer():

    def __init__(self):

        self.i2c = board.I2C()  
        self.icm = adafruit_icm20x.ICM20649(self.i2c)

        self.iterations = 500

        self.icm.accelerometer_data_rate_divisor = 0
        self.icm.gyro_data_rate_divisor = 0

        self.accelRate = self.icm.accelerometer_data_rate
        self.gyroRate = self.icm.gyro_data_rate
        
        self.gyroRange = self.icm.gyro_range
        self.accelRange = self.icm.accelerometer_range

    def gyro(self):
        return self.icm.gyro
        
    
    def accel(self):
        return self.icm.acceleration


a = accelerometer()

for i in range(a.iterations):
    print("Gyro value is:", a.gyro())
    print("Accelerometer value is:", a.accel())
    time.sleep(1)





