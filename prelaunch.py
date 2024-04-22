#----------------------------------------------------
# Simple script to nuke old logs >:)
# 
# @Author bdpope
# CyLaunch 2023-24
#----------------------------------------------------

import os

def main():
    input("You are about to nuke EVERYTHING in the logs folder, that good? Press enter to proceed. Press CTRL + C to exit")
    os.system("rm /home/cylaunch/logs/* ")

if __name__ == "main":
    main()