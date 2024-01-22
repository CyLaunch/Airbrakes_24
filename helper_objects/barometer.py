import time
from time import sleep
import board
import adafruit_mpl3115a2

class barometer:
    def __init__(self):
        #Create sensor object
        i2c = board.I2C()

        #Initialize the sensor
        self.sensor = adafruit_mpl3115a2.MPL3115A2(i2c)

        # You can configure the pressure at sealevel to get better altitude estimates.
        # This value has to be looked up from your local weather forecast or meteorological
        # reports.  It will change day by day and even hour by hour with weather
        # changes.  Remember altitude estimation from barometric pressure is not exact!

        # Set this to a value in hectopascals:
        self.sensor.sealevel_pressure = 1012.0 # Set to current pressure 11/8/23 by Cam

    def readPressure(self):
        pressure = self.sensor.pressure

        # Returns pressure in hectopascal
        return pressure

    def readAltitude(self, mode):
        # Reads the altitude in meters
        altitudeM = self.sensor.altitude

        if mode == 1: # if mode 1, return meters
            return altitudeM
        elif mode == 2: # if mode 2, return feet
            return altitudeM * 3.281
    
    def readTemp(self, mode):
        # Reads the temp in c
        tempC = self.sensor.temperature

        if mode == 1: # if mode 1, return c
            return tempC
        elif mode == 2: # if mode 2, return f
            return (tempC * 9/5) + 32

# Example Code

# b = barometer()

# while True:
#     print("--Start--")

#     print("Pressure: {0:0.3f} hectopascals".format(b.readPressure()))
    
#     print("Altitude: {0:0.3f} meters".format(b.readAltitude(1)))
#     print("Altitude: {0:0.3f} feet".format(b.readAltitude(2)))

#     print("Temperature: {0:0.3f} Celsius".format(b.readTemp(1)))
#     print("Temperature: {0:0.3f} Fahrenheit".format(b.readTemp(2)))

#     print("--End--")

#     time.sleep(0.1)
