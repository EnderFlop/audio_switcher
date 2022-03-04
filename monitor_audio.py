import screeninfo
import os

if len(screeninfo.get_monitors()) < 3: #if it is 3, all monitors are on. If it is less, the tall monitor is off and 'unplugged'.
  os.system("nircmd.exe setdefaultsounddevice \"Headset\" 1") 
  #using nircmd, change the windows sound device to headset. 1 means multimedia, not communication
  #must use double quotes lol