"""
Challenge :1
Create a Game in which there would be cards for Logos of Car brands 
and the Car Models would be displayed randomly on screen, user 
needs to place the correct Logo card for the Car displayed.

Brands And Codes 

1.Hyundai =       1 0 0
2.Maruti Suzuki = 0 1 1
3.Ford =          0 0 1

Pin A3 = Object Sensor 1
Pin A4 = Object Sensor 2
Pin A5 = Object Sensor 3 
"""

# Importing Libraries
from Phygital_v0 import Phygital_v0 as pyro
import pygame 
import random

#Pin Intialition 
pyro.pinMode('A3','dInput')
pyro.pinMode('A4','dInput')
pyro.pinMode('A5','dInput')

# #Communication Initialization
pyro.init('COM10')


#Setting up the pygame window
Width = 558
Height = 418

screen = pygame.display.set_mode((Width,Height))

#Loading Images

ScreenImage = pygame.image.load("Images/Background Image.png")
Hyundai_Car_1 = pygame.image.load("Images/Verna.png")
Maruti_Suzuki_Car_2 = pygame.image.load("Images/Swift.png")
Ford_Car_3 = pygame.image.load("Images/Ecosport.png")
screen.blit(ScreenImage,(0,0))

#Variables
num = random.randint(1,3)
data_OBJ_S_1 = pyro.dRead('A3')
data_OBJ_S_2 = pyro.dRead('A4')
data_OBJ_S_3 = pyro.dRead('A5')
print(num)
ASK = input("CAN WE START :")
if ASK == 'YES':
    if num == 1 :
        screen.blit(Hyundai_Car_1,(0,0))
        
    if num == 2:
        screen.blit(Maruti_Suzuki_Car_2,(0,0))
        
    if num == 3:
        screen.blit(Ford_Car_3,(0,0))
        
    NUMBER_ASK = int(input("ENTER THE NUMBER YOU HAVE GOT INN THE CONSOLE:"))
    if NUMBER_ASK == 1:
        print("PUT THE CARD OF A BRAND ON THE PYRO BOARD ")
        if data_OBJ_S_1 == 1 and data_OBJ_S_2 == 0 and data_OBJ_S_3 == 0:
            print("YOU HAVE CHOSSEN COREECT BRAND")
        elif data_OBJ_S_1 == 0 and data_OBJ_S_2 == 1 and data_OBJ_S_3 == 1:
            print("WRONG CARD")
        elif data_OBJ_S_1 == 0 and data_OBJ_S_2 == 0 and data_OBJ_S_3 == 1: 
            print("WRONG CARD")
            
    if NUMBER_ASK == 2:
        print("PUT THE CARD OF A BRAND ON THE PYRO BOARD ")
        if data_OBJ_S_1 == 1 and data_OBJ_S_2 == 0 and data_OBJ_S_3 == 0:
            print("YOU HAVE CHOSSEN COREECT BRAND")
        elif data_OBJ_S_1 == 1 and data_OBJ_S_2 == 0 and data_OBJ_S_3 == 0:
            print("WRONG CARD!!")
        elif data_OBJ_S_1 == 0 and data_OBJ_S_2 == 0 and data_OBJ_S_3 == 1: 
            print("WRONG CARD")        
            
    if NUMBER_ASK == 3:
        print("PUT THE CARD OF A BRAND ON THE PYRO BOARD ")
        if data_OBJ_S_1 == 0 and data_OBJ_S_2 == 0 and data_OBJ_S_3 == 1:
            print("YOU HAVE CHOSSEN COREECT BRAND")
        elif data_OBJ_S_1 == 1 and data_OBJ_S_2 == 0 and data_OBJ_S_3 == 0:
            print("WRONG CARD!!")
        elif data_OBJ_S_1 == 0 and data_OBJ_S_2 == 1 and data_OBJ_S_3 == 1: 
            print("WRONG CARD")        

