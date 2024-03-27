import time
from airbrake import airbrake

ab = airbrake()
def speed():
        alt_s1a = ab.get_altitude()
        alt_s1b = ab.get_altitude()
        alt_s1 = (alt_s1a + alt_s1b)/2
        before_time_ns = time.time_ns()

        alt_s2a = ab.get_altitude()
        alt_s2b = ab.get_altitude()
        alt_s2 = (alt_s2a + alt_s2b)/2
        after_time_ns = time.time_ns()

        time_delta_s = (after_time_ns - before_time_ns) * NS_TO_S
        altSpeed = (alt_s2-alt_s1)/time_delta_s
        return altSpeed

while True:
    print(str(speed()) + "\r")