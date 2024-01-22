import time
from barometer import barometer

sensor = barometer()
start_time = time.time()
data = sensor.readPressure()
end_time = time.time()
print(data)
print(str(end_time-start_time))