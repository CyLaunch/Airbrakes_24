from airbrake import airbrake

ab = airbrake()

while(ab.detect_launch() != True):
    print("HAH \n")

print("All done.")