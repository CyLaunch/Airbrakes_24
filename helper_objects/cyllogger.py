#----------------------------------------------------
# CyLogger object, simplifies timestamping and 
# writing to logs. Creates a timestamped logfile with
# timestamped entries. Closes the logger upon removal
# @Author bdpope
# CyLaunch 2023-24
#----------------------------------------------------

from datetime import datetime
import os

class cyllogger:
    def __init__(self, name):
        try:
            self.logfile = open("logs/" + name + datetime.now().strftime("--%Y-%m-%d--%H-%M-%S") + ".txt", "w")
        except:
            os.mkdir("logs")
            self.logfile = open("logs/" + name + datetime.now().strftime("--%Y-%m-%d--%H-%M-%S") + ".txt", "w")
    
    def writeTo(self, message):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.logfile.write("[" + current_time + "] " + message + "\n")
    
    def __del__(self):
        self.logfile.close()