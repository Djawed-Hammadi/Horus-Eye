#!/bin/python3 
#Coded By Djawed Hammadi
#Copyright@2020
import sys
import time
def Slowprint(banner):
    time.sleep(3)	
    for dido in banner + '\n' :
        sys.stdout.write(dido)
        sys.stdout.flush()
        time.sleep(10./ 100)
Slowprint("\n\033[0;36mIP INFO : \033[1;37m0% ║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║ 100%\n\n\033[0;31mRESULT:")
