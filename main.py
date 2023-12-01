from colorama import Fore, Back, Style
import os
import smbus
import time
import sys
import logging
from adafruit_I2C_lib import I2C


addressInterface1 = 0x08
IF1bus = I2C(addressInterface1)

#==========================================================================================
def displayBasicMenu():
    # os.system('clear')
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
    register = 0
    RPI2ARDcommand = 1
    RPI2ARDcommandList = [1]

    # Send the 1 byte command from the RPI to the Arduino
    # IF1bus.write8(register,RPI2ARDcommand)     #  Sending two bytes of data: Register (unused) and command
    IF1bus.writeList(register,RPI2ARDcommandList)
    # logging.debug('I2C: >> Wrote data 0x%02X',  RPI2ARDcommandList)

    # Request 1 byte response from the Arduino
    
    # logging.debug('I2C: >> Read data 0x%02X', ARD2RPIresponse)
    ARD2RPIresponse1 = IF1bus.readList(register, 20)

    # ARD2RPIresponse1 = IF1bus.readU8(register)
    # ARD2RPIresponse2 = IF1bus.readU8(register)
    # ARD2RPIresponse3 = IF1bus.readU8(register)
    print ("Received: ", ARD2RPIresponse1)
    # print ("Received: ", ARD2RPIresponse2)
    # print ("Received: ", ARD2RPIresponse3)




#==========================================================================================

#=(Main)===================================================================================

def main():
    logging.basicConfig(filename='python_app.log')

    done = False
    while not done:
        displayBasicMenu()
        userCommand = input(">>")
        if (userCommand == "0") or (userCommand == "q"):
            done = True

        if userCommand == "1":
            stopAllMotors()

if __name__ == '__main__':
    main()
#==========================================================================================


#==========================================================================================