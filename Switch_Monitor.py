import sys
import os
import time
import subprocess

SettingsFile = 'C:\\Users\\GoaXeoN\\AppData\\Local\\Stardock\\ObjectDockPlus\\CurrentTheme.ini'
CloseObjectDock = '"C:\\Program Files (x86)\\Stardock\\ObjectDock\\CloseObjectDock.exe"'
RunObjectDock = '"C:\\Program Files (x86)\\Stardock\\ObjectDock\\ObjectDock.exe"'

SearchData1 = 'LastMonitor=\\\\.\\DISPLAY1'
SearchData2 = 'LastMonitor=\\\\.\\DISPLAY2'

DETACHED_PROCESS = 0x00000008

# read in all the setting file
try:
    with open(SettingsFile, encoding='UTF-16', mode='r') as File1:
        File2 = File1.read()
except:
    sys.exit()

# replace parts of the text
if File2.find(SearchData1) > -1:
    File2 = File2.replace(SearchData1, SearchData2)
elif File2.find(SearchData2) > -1:
    File2 = File2.replace(SearchData2, SearchData1)

# close objectdock
subprocess.Popen(CloseObjectDock, shell=False, stdin=None, stdout=None, stderr=None)
time.sleep(10)

# over write with new text
try:
    with open(SettingsFile, encoding='UTF-16', mode='w') as File1:
        File1.write(File2)
except:
    sys.exit()
time.sleep(1)

# Startup ObjectDock
subprocess.Popen(RunObjectDock, shell=False, stdin=None, stdout=None, stderr=None, creationflags=DETACHED_PROCESS)
