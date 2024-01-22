import time
import board
import adafruit_icm20x
# Lets see if we can get this down to reading in around 0.1s
class accelerometer:

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