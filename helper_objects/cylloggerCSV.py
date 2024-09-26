#----------------------------------------------------
# CyLogger object, simplifies timestamping and 
# writing to logs. Creates a timestamped logfile .csv file with
# timestamped entries. Closes the logger upon removal.
# @Authors Marcus Miller
# CyLaunch 2023-24
#----------------------------------------------------

from datetime import datetime
import os

LOGS_DIR = "/home/cylaunch/logs/"
class cylloggerCSV:
    def __init__(self, name):
        self.filePath = LOGS_DIR + name + datetime.now().strftime("--%Y-%m-%d--%H-%M-%S") + ".csv"
        try:    
            self.logfile = os.open(self.filePath, os.O_CREAT | os.O_RDWR | os.O_NONBLOCK) 
        except:
            os.mkdir(LOGS_DIR)
            self.logfile = os.open(self.filePath, os.O_CREAT | os.O_RDWR | os.O_NONBLOCK)
    
    def writeToCSV(self, message):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S.%f")[:-3]
        os.write(self.logfile,  str.encode("[" + current_time + "]" + ", " + str(message) + "\n"))
    
    def __del__(self):
        os.close(self.logfile)