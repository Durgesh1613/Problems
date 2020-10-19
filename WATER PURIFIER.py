"""
WATER PURIFIER
"""
 
from Phygital_v0 import Phygital_v0 as pyro
import time
pyro.pinMode("A0","dOutput")
pyro.pinMode("A1","dOutput")
pyro.pinMode("A2","dOutput")
pyro.pinMode("A3","dOutput")
pyro.pinMode("A4","dOutput")
pyro.pinMode("A5","dOutput")

pyro.init("COM10")

START = input("TO START THE PURIFIER PRESS O:")

if START == "O":
    print("WATER PURIFIER HAS BEEN STARTED")
    print(" ")
    print("PROBLEM FOUND!!")
    print(" ")
    print("1.OUTLET PIPE CHOCKED")
    print(" ")
    print("2.POWER OFF")
    print(" ")
    print("3.WATER TANK EMPTY")
    print(" ")
    print("4.PIPE BROKEN")
    print(" ")
    print("5.PURIFIER RODS ARE EXHAUSTED")
    print(" ")
    print("6.THERE IS NO WATER SOURCE")
    PROBLEM = int(input("PLEASE ENTER THE NUMBER OF THE PROBLEM :"))    

    

while True:        
    try:
        if PROBLEM == 1:
            pyro.dWrite('A0',1)
            time.sleep(10)
            pyro.dWrite('A0',0)
            
        if PROBLEM == 2:
            pyro.dWrite('A1',1)
            time.sleep(10)
            pyro.dWrite('A0',0)
            
        if PROBLEM == 3:
            pyro.dWrite('A2',1)
            time.sleep(10)
            pyro.dWrite('A0',0)
            
        if PROBLEM == 4:
            pyro.dWrite('A3',1)
            time.sleep(1)
            pyro.dWrite('A3',0)
            
        if PROBLEM == 5:
            pyro.dWrite('A4',1)
            time.sleep(10)
            pyro.dWrite('A0',0)
            
        if PROBLEM == 6:
            pyro.dWrite('A5',1)    
            time.sleep(10)
            pyro.dWrite('A0',0)
            
        
    except:
         if KeyboardInterrupt:
            pyro.close()
            break
        
print("Closed the Connection!!")
        
        
        
        

