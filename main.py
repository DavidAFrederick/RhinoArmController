from colorama import Fore, Back, Style
import os
import smbus
import time
import sys
from adafruit_I2C_lib import I2C

#==========================================================================================
def displayBasicMenu():
    os.system('clear')
    print ("Interface A [ Gripper Pinch  ] - [Not started] - [45] - [12345]") 
    print ("Interface B [ Wrist Rotation ] - [In Process ] - [00] - [12345]")
    print ("Interface C [ Wrist Flex     ] - [Complete   ] - [00] - [12345]")
    print ("Interface D [ Elbow          ] - [UnKnown    ] - [00] - [12345]")
    print ("Interface E [ Shoulder       ] - [UnKnown    ] - [00] - [12345]")
    print ("Interface F [ Waist          ] - [UnKnown    ] - [00] - [12345]")
    print (" ")
    print (F"{Style.BRIGHT}Commands:")
    print (F"{Style.NORMAL}Stop all - 1")
    print ("Home all - 2")
    print ("Set Angle - 11-xx, 21-xx, 31-xx")
    print ("Set Count - 12-xxxx, 22-xxxx, 33-xxxx")
    print ("Exit - 0")

#==========================================================================================
def stopAllMotors():
    RPI2ARDcommand = 1

    # Send the 1 byte command from the RPI to the Arduino
    bus.write8(address,RPI2ARDcommand)

    # Request 1 byte response from the Arduino
    ARD2RPIresponse = bus.readU8(address)
    print ("ARD2RPIresponse: |", ARD2RPIresponse, "|")



#==========================================================================================

#=(Main)===================================================================================

address = 0x08
bus = I2C(address)


done = False
while not done:
    displayBasicMenu()
    userCommand = input(">>")
    if (userCommand == "0") or (userCommand == "q"):
        done = True

    if userCommand == "1":
        stopAllMotors()



#==========================================================================================