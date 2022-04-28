2019 / Python 3
# Moves ObjectDock to the correct screen

Using a python script, I solved a problem with ObjectDock starting up on the wrong screen. The script searches and changes in the settings file
for ObjectDock and restarts ObjectDock so that it starts on the correct screen.

What is ObjectDock ?
ObjectDock is a program from Stardock that creates a menu where you can have your shortcuts (instead of on the desktop).
The menu appears when you press the mouse arrow to the edge of the screen.

The problem I had was that sometimes ObjectDock started on the wrong screen and instead of having to go into a bunch of settings each time, I wrote a script that solved the problem with one click.

First I found out where the save information was and what it looked like.
After some testing, I was able to identify which setting was changing the screen.
Created search variables and replacement variables (for the different screens).
The first thing the script does is turn off ObjectDock 
Replaces the setting in the settings file.
And then starts up ObjectDock.
Then it was just to add an icon (shortcut) to the script on ObjectDock (to click on).

# How to use it:

1) install Python 3.x
2) copy the text and save it in a file and name the file Switch_Monitor.py
3) make a shortcut and put it on the Dock (or where you ever like)

now when you run it, it will terminate ObjectDock, change the settings file, start up ObjectDock agian.

if it not working or you get error:
check that variables SettingsFile, CloseObjectDock, RunObjectDock have the right search path
