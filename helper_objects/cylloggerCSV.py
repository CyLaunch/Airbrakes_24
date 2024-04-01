#----------------------------------------------------
# CyLogger object, simplifies timestamping and 
# writing to logs. Creates a timestamped logfile .csv excel file with
# timestamped entries. Closes the logger upon removal.
# @Authors Marcus Miller
# CyLaunch 2023-24
#----------------------------------------------------

from datetime import datetime
import os
#import csv
LOGS_DIR = "/home/cylaunch/logs/"
class cylloggerCSV:
    def __init__(self, name):
        self.filePath = LOGS_DIR + name + datetime.now().strftime("--%Y-%m-%d--%H-%M-%S") + ".csv", "w"
        try:    
            self.logfile = os.open(self.filePath | os.O_NONBLOCK) 
            #self.writer = csv.writer(self.logfile)  
        except:
            os.mkdir(LOGS_DIR)
            self.logfile = os.open(LOGS_DIR + name + datetime.now().strftime("--%Y-%m-%d--%H-%M-%S") + ".csv", "w")
    
    def writeTo(self, message): 
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        arr = [current_time, message]
        self.writer.writerow(arr)
    
    def writeToCSV(self, message)
        now = datetime,now()
        current_time = now.strftime("%H:%M:%S")
        arr = [current_time, message]
        for i in message:
            string = string + ", " + i
            os.write(self.logfile,  str.encode("[" + current_time + "] " + str(string) + "\n"))
    
    def __del__(self):
        self.logfile.close()