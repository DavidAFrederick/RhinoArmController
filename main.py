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
    print ("Home One - 10, 20, 30")
    print ("Set Angle - 11-xx, 21-xx, 31-xx")
    print ("Set Count - 12-xxxx, 22-xxxx, 33-xxxx")
    print ("Exit - 0")

#==========================================================================================
def stopAllMotors():
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 1      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    # print ("Command / Response : ", RPI2ARDcommand, "  ", ARD2RPIresponse1)

#==========================================================================================
def homeAll():
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 2      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    # print ("Command / Response : ", RPI2ARDcommand, "  ", ARD2RPIresponse1)

#==========================================================================================
def homeIFA():
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 10      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    # print ("Command / Response : ", RPI2ARDcommand, "  ", ARD2RPIresponse1)

#==========================================================================================
def homeIFB():
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 20      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    # print ("Command / Response : ", RPI2ARDcommand, "  ", ARD2RPIresponse1)

#==========================================================================================
def homeIFC():
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 30      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    # print ("Command / Response : ", RPI2ARDcommand, "  ", ARD2RPIresponse1)

#==========================================================================================
def IFAsetAngle():
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 11      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    # print ("Command / Response : ", RPI2ARDcommand, "  ", ARD2RPIresponse1)

#==========================================================================================
def IFBsetAngle():
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 21      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    # print ("Command / Response : ", RPI2ARDcommand, "  ", ARD2RPIresponse1)

#==========================================================================================
def IFCsetAngle():
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 31      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    # print ("Command / Response : ", RPI2ARDcommand, "  ", ARD2RPIresponse1)

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

        if userCommand == "2":
            homeAll()

        if userCommand == "10":
            homeIFA()

        if userCommand == "20":
            homeIFB()

        if userCommand == "30":
            homeIFC()

        if userCommand == "11":
            IFAsetAngle()

        if userCommand == "21":
            IFBsetAngle()

        if userCommand == "31":
            IFCsetAngle()

if __name__ == '__main__':
    main()
#==========================================================================================


#==========================================================================================