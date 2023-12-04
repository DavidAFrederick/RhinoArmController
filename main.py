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
    print (" ")
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
def displaycoloredMenu():

    # IFA_status = "InProcess"
    # IFA_status = "Complete"
    IFA_status = "Unknown"
    IFA_angle = 0                #  2 characters width
    IFA_count = 11             #  6 characters width


    # IFB_status = "InProcess"
    IFB_status = "Complete"
    # IFB_status = "Unknown"
    IFB_angle = 2                #  2 characters width
    IFB_count = 22             #  6 characters width

    IFC_status = "InProcess"
    # IFC_status = "Complete"
    # IFC_status = "Unknown"
    IFC_angle = 94                #  2 characters width
    IFC_count = 0             #  6 characters width

    IFD_status = "InProcess"
    # IFD_status = "Complete"
    # IFD_status = "Unknown"
    IFD_angle = 96                #  2 characters width
    IFD_count = 33333             #  6 characters width

    # IFE_status = "InProcess"
    IFE_status = "Complete"
    # IFE_status = "Unknown"
    IFE_angle = 80                #  2 characters width
    IFE_count = 20348             #  6 characters width

    # IFF_status = "InProcess"
    IFF_status = "Complete"
    # IFF_status = "Unknown"
    IFF_angle = 70                #  2 characters width
    IFF_count = 10101             #  6 characters width

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    IFX_status_display_In_Process = "In Process "
    IFX_status_display_Complete = " Complete  "
    IFX_status_display_Unknown = " Unknown   "

    # os.system('clear')   
    print (" ")
    print ("Interface A [ Gripper Pinch  ] - [", end="")    

    if (IFA_status == "Unknown"):   
        print (Fore.RED, end="")
        IFA_status_display = IFX_status_display_Unknown
    
    if (IFA_status == "InProcess"): 
        print (Fore.CYAN, end="")
        IFA_status_display = IFX_status_display_In_Process

    if (IFA_status == "Complete"):  
        print (Fore.GREEN, end="")
        IFA_status_display = IFX_status_display_Complete

    print (IFA_status_display, end="")
    print (Fore.WHITE, end="")

    print("] - [",        end="")
    print ("%02d" % (IFA_angle), end="" )
    print("] - [",        end="")
    print ("%05d" % (IFA_count), end="" )
    print("]")

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    print ("Interface B [ Wrist Rotation ] - [", end="")    

    if (IFA_status == "Unknown"):   
        print (Fore.RED, end="")
        IFB_status_display = IFX_status_display_Unknown
    
    if (IFB_status == "InProcess"): 
        print (Fore.CYAN, end="")
        IFB_status_display = IFX_status_display_In_Process

    if (IFB_status == "Complete"):  
        print (Fore.GREEN, end="")
        IFB_status_display = IFX_status_display_Complete

    print (IFB_status_display, end="")
    print (Fore.WHITE, end="")

    print("] - [",        end="")
    print ("%02d" % (IFB_angle), end="" )
    print("] - [",        end="")
    print ("%05d" % (IFB_count), end="" )
    print("]")

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    print ("Interface C [ Wrist Flex     ] - [", end="")    

    if (IFC_status == "Unknown"):   
        print (Fore.RED, end="")
        IFC_status_display = IFX_status_display_Unknown
    
    if (IFC_status == "InProcess"): 
        print (Fore.CYAN, end="")
        IFC_status_display = IFX_status_display_In_Process

    if (IFC_status == "Complete"):  
        print (Fore.GREEN, end="")
        IFC_status_display = IFX_status_display_Complete

    print (IFC_status_display, end="")
    print (Fore.WHITE, end="")

    print("] - [",        end="")
    print ("%02d" % (IFC_angle), end="" )
    print("] - [",        end="")
    print ("%05d" % (IFC_count), end="" )
    print("]")

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    print ("Interface D [ Elbow          ] - [", end="")    

    if (IFD_status == "Unknown"):   
        print (Fore.RED, end="")
        IFD_status_display = IFX_status_display_Unknown
    
    if (IFD_status == "InProcess"): 
        print (Fore.CYAN, end="")
        IFD_status_display = IFX_status_display_In_Process

    if (IFD_status == "Complete"):  
        print (Fore.GREEN, end="")
        IFD_status_display = IFX_status_display_Complete

    print (IFD_status_display, end="")
    print (Fore.WHITE, end="")

    print("] - [",        end="")
    print ("%02d" % (IFD_angle), end="" )
    print("] - [",        end="")
    print ("%05d" % (IFD_count), end="" )
    print("]")

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    print ("Interface E [ Shoulder       ] - [", end="")    

    if (IFE_status == "Unknown"):   
        print (Fore.RED, end="")
        IFE_status_display = IFX_status_display_Unknown
    
    if (IFE_status == "InProcess"): 
        print (Fore.CYAN, end="")
        IFE_status_display = IFX_status_display_In_Process

    if (IFE_status == "Complete"):  
        print (Fore.GREEN, end="")
        IFE_status_display = IFX_status_display_Complete

    print (IFE_status_display, end="")
    print (Fore.WHITE, end="")

    print("] - [",        end="")
    print ("%02d" % (IFE_angle), end="" )
    print("] - [",        end="")
    print ("%05d" % (IFE_count), end="" )
    print("]")

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    print ("Interface F [ Waist          ] - [", end="")    

    if (IFF_status == "Unknown"):   
        print (Fore.RED, end="")
        IFF_status_display = IFX_status_display_Unknown
    
    if (IFF_status == "InProcess"): 
        print (Fore.CYAN, end="")
        IFF_status_display = IFX_status_display_In_Process

    if (IFF_status == "Complete"):  
        print (Fore.GREEN, end="")
        IFF_status_display = IFX_status_display_Complete

    print (IFF_status_display, end="")
    print (Fore.WHITE, end="")

    print("] - [",        end="")
    print ("%02d" % (IFF_angle), end="" )
    print("] - [",        end="")
    print ("%05d" % (IFF_count), end="" )
    print("]")

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    print (" ")
    print (F"{Style.BRIGHT}Commands:")
    print (F"{Style.NORMAL}Stop all - 1")
    print ("Home all - 2")
    print ("Home One - 10, 20, 30")
    print ("Set Angle - 11-xx, 21-xx, 31-xx")
    print ("Set Count - 12-xxxx, 22-xxxx, 33-xxxx")
    print ("Exit - 0")


#==========================================================================================

#==========================================================================================
def stopAllMotors():
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 1                                                    # This command
    RPI2ARDexpected_response_count = 1                                    # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    print ("COMMAND: stopAllMotors ")

#==========================================================================================
def homeAll():
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 2      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    print ("COMMAND: homeAll ")

#==========================================================================================
def homeIFA():
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 10      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    print ("COMMAND: homeIFA ")

#==========================================================================================
def homeIFB():
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 20      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    print ("COMMAND:  homeIFB")

#==========================================================================================
def homeIFC():
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 30      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    print ("COMMAND: homeIFC ")

#==========================================================================================
def IFAsetAngle():
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 11      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    print ("COMMAND: IFAsetAngle ")

#==========================================================================================
def IFBsetAngle():
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 21      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    print ("COMMAND: IFBsetAngle ")

#==========================================================================================
def IFCsetAngle():
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 31      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    print ("COMMAND: IFCsetAngle ")

#==========================================================================================
#==========================================================================================
def IFAsetCount():
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 12      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    print ("COMMAND: IFAsetCount ")

#==========================================================================================
def IFBsetCount():
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 22      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    print ("COMMAND: IFBsetCount ")

#==========================================================================================
def IFCsetCount():
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 32      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    print ("COMMAND: IFCsetCount ")

#=(Main)===================================================================================

def main():
    logging.basicConfig(filename='python_app.log')

    done = False
    while not done:
        # displayBasicMenu()
        displaycoloredMenu()
        userCommand = input(">>>>")
        shortUserCommand = 99

        if (len(userCommand) >= 2):
            shortUserCommand = userCommand[0:2]

            if (len(userCommand) >= 4):
                position_of_dash = userCommand.find("-")
                parameter = userCommand[(position_of_dash+1):]
                print ("ShortUserCommand: |",shortUserCommand ,"|  Parameter:  |", int(parameter),"|")
                print ("x2 |",int(parameter)*2,"|")

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

        if shortUserCommand == "11":
            IFAsetAngle()

        if shortUserCommand == "21":
            IFBsetAngle()

        if shortUserCommand == "31":
            IFCsetAngle()

        if shortUserCommand == "12":
            IFAsetCount()

        if shortUserCommand == "22":
            IFBsetCount()

        if shortUserCommand == "32":
            IFCsetCount()

if __name__ == '__main__':
    main()
#==========================================================================================


#==========================================================================================