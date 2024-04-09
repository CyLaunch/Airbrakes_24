import time
from airbrake import airbrake

NS_TO_S = 0.000000001
ALT_MAX_SPEED_FT_S = 700.0

ab = airbrake()
def current_speed():
        alt_s1 = ab.get_altitude()
        before_time_ns = time.time_ns()

        alt_s2 = ab.get_altitude()
        after_time_ns = time.time_ns()

        time_delta_s = (after_time_ns - before_time_ns) * NS_TO_S

        altSpeed = (alt_s2-alt_s1)/time_delta_s

        if altSpeed > ALT_MAX_SPEED_FT_S: #This can change so it makes sense just if its outside of bounds
            return 1.0

        elif altSpeed <= 0:
            return 2.0
        else:
            return altSpeed

while True:
        # stime.sleep(.2)
        print(str(current_speed()) + "\r")