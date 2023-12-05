from colorama import Fore, Back, Style
import os
import smbus
import time
import sys
import logging
from adafruit_I2C_lib import I2C


def define_global_variables():
    global addressInterface1;   addressInterface1 = 0x08
    global IF1bus;              IF1bus = I2C(addressInterface1)

    global IFA_status;          IFA_status = "Unknown"
    global IFA_integer_status;  IFA_integer_status = 0
    global IFA_angle;           IFA_angle = 0              
    global IFA_count;           IFA_count = 0

    print ("IFA_integer_status start of IFASetANgle: ", IFA_integer_status)


    global IFB_status;          IFB_status = "Unknown"
    global IFB_integer_status;  IFB_integer_status = 0
    global IFB_angle;           IFB_angle = 0              
    global IFB_count;           IFB_count = 0

    global IFC_status;          IFC_status = "Unknown"
    global IFC_integer_status;  IFC_integer_status = 0
    global IFC_angle;           IFC_angle = 0              
    global IFC_count;           IFC_count = 0

    global IFD_status;          IFD_status = "Unknown"
    global IFD_integer_status;  IFD_integer_status = 0
    global IFD_angle;           IFD_angle = 0              
    global IFD_count;           IFD_count = 0

    global IFE_status;          IFE_status = "Unknown"
    global IFE_integer_status;  IFE_integer_status = 0
    global IFE_angle;           IFE_angle = 0              
    global IFE_count;           IFE_count = 0

    global IFF_status;          IFF_status = "Unknown"
    global IFF_integer_status;  IFF_integer_status = 0
    global IFF_angle;           IFF_angle = 0              
    global IFF_count;           IFF_count = 0

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

    # # IFA_status = "InProcess"
    # # IFA_status = "Complete"
    # IFA_status = "Unknown"
    # IFA_angle = 0                #  2 characters width
    # IFA_count = 11             #  6 characters width

    IFA_integer_status = 2


    # # IFB_status = "InProcess"
    # IFB_status = "Complete"
    # # IFB_status = "Unknown"
    # IFB_angle = 2                #  2 characters width
    # IFB_count = 22             #  6 characters width

    # IFC_status = "InProcess"
    # # IFC_status = "Complete"
    # # IFC_status = "Unknown"
    # IFC_angle = 94                #  2 characters width
    # IFC_count = 0             #  6 characters width

    # IFD_status = "InProcess"
    # # IFD_status = "Complete"
    # # IFD_status = "Unknown"
    # IFD_angle = 96                #  2 characters width
    # IFD_count = 33333             #  6 characters width

    # # IFE_status = "InProcess"
    # IFE_status = "Complete"
    # # IFE_status = "Unknown"
    # IFE_angle = 80                #  2 characters width
    # IFE_count = 20348             #  6 characters width

    # # IFF_status = "InProcess"
    # IFF_status = "Complete"
    # # IFF_status = "Unknown"
    # IFF_angle = 70                #  2 characters width
    # IFF_count = 10101             #  6 characters width

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

# All transfers to the Arduino include:  [the command],[Data (optional)], [Expected response size]

#==========================================================================================
def stopAllMotors():    ##  two bytes command and one byte Reponse
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 1                                                    # This command
    RPI2ARDexpected_response_count = 1                                    # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    print ("COMMAND: stopAllMotors ")

#==========================================================================================
def homeAll():          ##  two byte command and one byte Reponse
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 2      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    print ("COMMAND: homeAll ")

#==========================================================================================
def homeIFA():          ##  Two byte command and one byte Reponse
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 10      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    print ("COMMAND: homeIFA ")

#==========================================================================================
def homeIFB():          ##  Two byte command and one byte Reponse
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 20      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    print ("COMMAND:  homeIFB")

#==========================================================================================
def homeIFC():          ##  Two byte command and one byte Reponse
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 30      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    print ("COMMAND: homeIFC ")

#==========================================================================================
def IFAsetAngle(angle):          ##  Three byte command and one byte Reponse

    # Transfers to the Arduino include:  [ command],[angle], [Expected response size]
    print ("IFA_integer_status start of IFASetANgle: ", IFA_integer_status)

    if (angle < 0) or (angle > 90):
        print ("Angle outside of 0 to 90, setting to 2, angle is:  ",angle )
        angle = 2

    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 11      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand, angle, RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    print ("11 - RESPONSE:   length of list: ", len(ARD2RPIresponse1), "   List:", ARD2RPIresponse1 )

    if (ARD2RPIresponse1[0] >= 0) and (ARD2RPIresponse1[0] <= 2):
        IFA_integer_status = ARD2RPIresponse1[0]

    print ("COMMAND: IFAsetAngle ")
    print ("IFA_integer_status in IFBSetAngle: ", IFA_integer_status)
    print ("IFA_status: in IFBSetAngle ", IFA_status)
#==========================================================================================
def IFBsetAngle():           ##  Two byte command and one byte Reponse
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 21      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)
    
    print ("COMMAND: IFBsetAngle ")

#==========================================================================================
def IFCsetAngle():         ##  Two byte command and one byte Reponse
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 31      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    print ("COMMAND: IFCsetAngle ")
    print ("IFA_status: in main end ", IFA_status)

#==========================================================================================
#==========================================================================================
def IFAsetCount():         ##  Three byte command and one byte Reponse
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 12      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    print ("COMMAND: IFAsetCount ")

#==========================================================================================
def IFBsetCount():         ##  Three byte command and one byte Reponse
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 22      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    print ("COMMAND: IFBsetCount ")

#==========================================================================================
def IFCsetCount():         ##  Three byte command and one byte Reponse
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 32      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    print ("COMMAND: IFCsetCount ")

#==========================================================================================

# Command - Provide status of command  = Command, command // 
# Response for spec command: [ Not started || In Process || Complete ]
# >>	CTR = 2  => SL = 1 		Command = [40] [XX] // [Status IF-A][Status IF-B][Status IF-C]

def request_all_interface_status():  ##  two bytes command and three byte Reponse
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 40      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)


#==========================================================================================

# Command - Request current counts  //   ##  one byte command and six byte Reponse
# InterfaceA Count [high] [low],InterfaceB Count [high] [low], InterfaceC Count [high] [low]
# >>	CTR = 1  => SL = 6 		Command = [50]   // [A-High] [A-Low][B-High] [B-Low][C-High] [C-Low] 

def request_all_interface_counts():
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 50      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

#==========================================================================================

def map_interface_status_integer_to_text():
    print ("IFA_integer_status in Map start: ", IFA_integer_status)
    print ("IFA_status: in map start ", IFA_status)


    if (IFA_integer_status == 0): IFA_status = "Unknown"
    if (IFA_integer_status == 1): IFA_status = "InProcess"
    if (IFA_integer_status == 2): IFA_status = "Complete"

    if (IFB_integer_status == 0): IFB_status = "Unknown"
    if (IFB_integer_status == 1): IFB_status = "InProcess"
    if (IFB_integer_status == 2): IFB_status = "Complete"

    if (IFC_integer_status == 0): IFC_status = "Unknown"
    if (IFC_integer_status == 1): IFC_status = "InProcess"
    if (IFC_integer_status == 2): IFC_status = "Complete"

    if (IFD_integer_status == 0): IFD_status = "Unknown"
    if (IFD_integer_status == 1): IFD_status = "InProcess"
    if (IFD_integer_status == 2): IFD_status = "Complete"

    if (IFE_integer_status == 0): IFE_status = "Unknown"
    if (IFE_integer_status == 1): IFE_status = "InProcess"
    if (IFE_integer_status == 2): IFE_status = "Complete"

    if (IFF_integer_status == 0): IFF_status = "Unknown"
    if (IFF_integer_status == 1): IFF_status = "InProcess"
    if (IFF_integer_status == 2): IFF_status = "Complete"

    print ("IFA_integer_status in Map out: ", IFA_integer_status)
    print ("IFA_status: in map end ", IFA_status)

#=(Main)===================================================================================

def main():
    logging.basicConfig(filename='python_app.log')

    define_global_variables()


    parameter = 99

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
            IFAsetAngle(int(parameter))

        print ("IFA_integer_status in main: ", IFA_integer_status)
        print ("IFA_status: in main mid ", IFA_status)

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

    map_interface_status_integer_to_text()
    print ("IFA_integer_status end main: ", IFA_integer_status)
    print ("IFA_status: in main end ", IFA_status)

if __name__ == '__main__':
    main()
#==========================================================================================


#==========================================================================================