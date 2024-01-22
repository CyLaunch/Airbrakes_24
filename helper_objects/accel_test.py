import time
from accelerometer import accelerometer

sensor = accelerometer()
start_time = time.time()
data = sensor.accel()
end_time = time.time()
print(data)
print(str(end_time-start_time))