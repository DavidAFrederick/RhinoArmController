from colorama import Fore, Back, Style
import os
import smbus
import time
import sys
import logging
from adafruit_I2C_lib import I2C

##  Dec 21, 2023 - Adding second arduino
"""
ToDo
) Figure why command 90 is not working
) Add joints D,E,F
) Determine which status items are really being used.

"""

#=( Defining global variables )=========================================

addressInterface1 = 0x08
addressInterface2 = 0x09

IF1bus = I2C(addressInterface1)
IF2bus = I2C(addressInterface2)

loop_for_status = True
error_string = "     "

IFA_status = "Unknown"
IFA_integer_status = 0
IFA_angle = 0              
IFA_count = 0

IFB_status = "Unknown"
IFB_integer_status = 0
IFB_angle = 0              
IFB_count = 0

IFC_status = "Unknown"
IFC_integer_status = 0
IFC_angle = 0              
IFC_count = 0

IFD_status = "Unknown"
IFD_integer_status = 0
IFD_angle = 0              
IFD_count = 0

IFE_status = "Unknown"
IFE_integer_status = 0
IFE_angle = 0              
IFE_count = 0

IFF_status = "Unknown"
IFF_integer_status = 0
IFF_angle = 0              
IFF_count = 0

#==========================================================================================
IF_A_one_second_count = 0
IF_B_one_second_count = 0
IF_C_one_second_count = 0
IF_D_one_second_count = 0
IF_E_one_second_count = 0
IF_F_one_second_count = 0


#==========================================================================================

def map_interface_status_integer_to_text():
    global IFA_integer_status, IFA_status
    global IFB_integer_status, IFB_status
    global IFC_integer_status, IFC_status
    global IFD_integer_status, IFD_status
    global IFE_integer_status, IFE_status
    global IFF_integer_status, IFF_status

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

#==========================================================================================
#  This function is no longer needed

def displayBasicMenu():
    os.system('clear')
    print ("                                   Status       Angle    Count")
    print ("Interface A [ Gripper Pinch  ] - [Not started] - [45] - [12345]") 
    print ("Interface B [ Wrist Rotation ] - [In Process ] - [00] - [12345]")
    print ("Interface C [ Wrist Flex     ] - [Complete   ] - [00] - [12345]")
    print ("Interface D [ Elbow          ] - [UnKnown    ] - [00] - [12345]")
    print ("Interface E [ Shoulder       ] - [UnKnown    ] - [00] - [12345]")
    print ("Interface F [ Waist          ] - [UnKnown    ] - [00] - [12345]")
    print (" ")
    print (F"{Style.BRIGHT}Commands:")
    print (F"{Style.NORMAL}Stop all - 1")
    print ("Home all  - 2")
    print ("Home One  - 10, 20, 30")
    print ("Set Angle - 11-xx, 21-xx, 31-xx")
    print ("Set Count - 12-xxxx, 22-xxxx, 33-xxxx")
    print (" ")
    print ("Exit - 0")
    print (error_string)

#==========================================================================================
def displaycoloredMenu():
    global IFA_integer_status, IFA_status
    global IFB_integer_status, IFB_status
    global IFC_integer_status, IFC_status
    global IFD_integer_status, IFD_status
    global IFE_integer_status, IFE_status
    global IFF_integer_status, IFF_status

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    IFX_status_display_In_Process = "In Process "
    IFX_status_display_Complete = " Complete  "
    IFX_status_display_Unknown = " Unknown   "

    # os.system('clear')   
    print ("================================================================")
    print ("|                                  Status       Angle    Count |")
    print ("================================================================")
    print ("Interface A [ Gripper Pinch  ] - [", end="")    
 
    IFA_status_display = ""
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
    print("]  [", end="")
    print ("%03d" % (IF_A_one_second_count), end="" )  
    print("]")

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    print ("Interface B [ Wrist Rotation ] - [", end="")    

    IFB_status_display = ""
    if (IFB_status == "Unknown"):   
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
    print("]  [", end="")
    print ("%03d" % (IF_B_one_second_count), end="" )  
    print("]")

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    print ("Interface C [ Wrist Flex     ] - [", end="")    

    IFC_status_display = ""
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
    print("]  [", end="")
    print ("%03d" % (IF_C_one_second_count), end="" )  
    print("]")

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    print ("Interface D [ Elbow          ] - [", end="")    

    IFD_status_display = ""
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
    print("]  [", end="")
    print ("%03d" % (IF_D_one_second_count), end="" )  
    print("]")

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    print ("Interface E [ Shoulder       ] - [", end="")    

    IFE_status_display = ""
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
    print("]  [", end="")
    print ("%03d" % (IF_E_one_second_count), end="" )  
    print("]")

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    print ("Interface F [ Waist          ] - [", end="")    

    IFF_status_display = ""
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
    print("]  [", end="")
    print ("%03d" % (IF_F_one_second_count), end="" )  
    print("]")

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    # print (" ")
    print (F"{Style.BRIGHT}Commands:")
    print (F"{Style.NORMAL}Stop all   - 1")
    print ("Home all   - 2")
    print ("                             Joint Commands")
    # print (" ")
    print ("              A        B        C        D        E        F     ")
    print ("Home One   - 10,      20,      30,      40,      50,      60     ")
    print ("Set Angle  - 11-xx,   21-xx,   31-xx,   41-xx,   51-xx,   61-xx  ")
    print ("Set Count  - 12-xxxx, 22-xxxx, 32-xxxx, 42-xxxx, 52-xxxx, 62-xxxx")
    print ("Find Home  - 15       25       35       45       55       65     ")
    print ("SelfTest   - 16       26       36       46       56       66     ")
    print ("Get 1 Sec  - 17       27       37       47       57       67     ")
    print ("Man-home   - 18       28       38       48       58       68     ")
    print ("Man-Out    - 19       29       39       49       59       69     ")
    print (" ")
    print ("Get Status - 90")
    print ("Get Counts - 91")
    # print (" ")
    print ("Exit - 0")

#==========================================================================================
#==========================================================================================
def stopAllMotors():    ##  two bytes command and one byte Reponse
    # All transfers to the Arduino include:  [the command],[Data (optional)], [Expected response size]
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 1                                                    # This command
    RPI2ARDexpected_response_count = 1                                    # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    IF2bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF2bus.readList(register, RPI2ARDexpected_response_count)

    # print ("COMMAND: stopAllMotors ")

#==========================================================================================
def homeAll():          ##  two byte command and one byte Reponse
    # All transfers to the Arduino include:  [the command],[Data (optional)], [Expected response size]
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 2      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    IF2bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse2 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    # print ("COMMAND: homeAll ")

#==========================================================================================
def homeIFA():          ##  Two byte command and one byte Reponse
    # All transfers to the Arduino include:  [the command],[Data (optional)], [Expected response size]
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 10      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    # print ("COMMAND: homeIFA ")

#==========================================================================================
def homeIFB():          ##  Two byte command and one byte Reponse
    # All transfers to the Arduino include:  [the command],[Data (optional)], [Expected response size]
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 20      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    # print ("COMMAND:  homeIFB")

#==========================================================================================
def homeIFC():          ##  Two byte command and one byte Reponse
    # All transfers to the Arduino include:  [the command],[Data (optional)], [Expected response size]
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 30      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    # print ("COMMAND: homeIFC ")

#==========================================================================================
def homeIFD():          ##  Two byte command and one byte Reponse
    global ARD2RPIresponse1
    # All transfers to the Arduino include:  [the command],[Data (optional)], [Expected response size]
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 40  # This command goes to Arduino #2
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF2bus.writeList(register,RPI2ARDcommandList)  # Arduino #2
    ARD2RPIresponse1 = IF2bus.readList(register, RPI2ARDexpected_response_count)

#==========================================================================================
def homeIFE():          ##  Two byte command and one byte Reponse
    # All transfers to the Arduino include:  [the command],[Data (optional)], [Expected response size]
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 50  # This command goes to Arduino #2
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF2bus.writeList(register,RPI2ARDcommandList) # Arduino #2
    ARD2RPIresponse1 = IF2bus.readList(register, RPI2ARDexpected_response_count)

    # print ("COMMAND: homeIFE ")

#==========================================================================================
def homeIFF():          ##  Two byte command and one byte Reponse
    # All transfers to the Arduino include:  [the command],[Data (optional)], [Expected response size]
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 60 # This command goes to Arduino #2
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF2bus.writeList(register,RPI2ARDcommandList) # Arduino #2
    ARD2RPIresponse1 = IF2bus.readList(register, RPI2ARDexpected_response_count)

    # print ("COMMAND: homeIFF ")

#==========================================================================================
def IFAsetAngle(angle):          ##  Three byte command and one byte Reponse
        # Transfers to the Arduino include:  [ command],[angle], [Expected response size]  || [status]

    global IFA_integer_status, IFA_status
    global error_string

    if (angle < 0) or (angle > 90):
        error_string = "Angle outside of 0 to 90, setting to 2, angle is: " + str(angle)
        angle = 0

    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 11      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand, angle, RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    # print ("11 - RESPONSE:   length of list: ", len(ARD2RPIresponse1), "   List:", ARD2RPIresponse1 )

    if (ARD2RPIresponse1[0] >= 0) and (ARD2RPIresponse1[0] <= 2):
        IFA_integer_status = ARD2RPIresponse1[0]

#==========================================================================================
def IFBsetAngle(angle):           ##  Two byte command and one byte Reponse
    # Transfers to the Arduino include:  [ command],[angle], [Expected response size]  || [status]
    global IFB_integer_status, IFB_status
    global error_string

    if (angle < 0) or (angle > 90):
        error_string = "Angle outside of 0 to 90, setting to 2, angle is: " + str(angle)
        angle = 0

    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 21      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)
    
    if (ARD2RPIresponse1[0] >= 0) and (ARD2RPIresponse1[0] <= 2):
        IFB_integer_status = ARD2RPIresponse1[0]

#==========================================================================================
def IFCsetAngle(angle):         ##  Two byte command and one byte Reponse
    # Transfers to the Arduino include:  [ command],[angle], [Expected response size]  || [status]
    global IFC_integer_status, IFC_status
    global error_string

    if (angle < 0) or (angle > 90):
        error_string = "Angle outside of 0 to 90, setting to 2, angle is: " + str(angle)
        angle = 0

    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 31      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    if (ARD2RPIresponse1[0] >= 0) and (ARD2RPIresponse1[0] <= 2):
        IFC_integer_status = ARD2RPIresponse1[0]

#==========================================================================================
#==========================================================================================
def IFDsetAngle(angle):          ##  Three byte command and one byte Reponse
        # Transfers to the Arduino include:  [ command],[angle], [Expected response size]  || [status]

    global IFD_integer_status, IFD_status
    global error_string

    if (angle < 0) or (angle > 90):
        error_string = "Angle outside of 0 to 90, setting to 2, angle is: " + str(angle)
        angle = 0

    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 41      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand, angle, RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF2bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF2bus.readList(register, RPI2ARDexpected_response_count)

    # print ("11 - RESPONSE:   length of list: ", len(ARD2RPIresponse1), "   List:", ARD2RPIresponse1 )

    if (ARD2RPIresponse1[0] >= 0) and (ARD2RPIresponse1[0] <= 2):
        IFD_integer_status = ARD2RPIresponse1[0]

#==========================================================================================
def IFEsetAngle(angle):           ##  Two byte command and one byte Reponse
    # Transfers to the Arduino include:  [ command],[angle], [Expected response size]  || [status]
    global IFE_integer_status, IFE_status
    global error_string

    if (angle < 0) or (angle > 90):
        error_string = "Angle outside of 0 to 90, setting to 2, angle is: " + str(angle)
        angle = 0

    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 51      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF2bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF2bus.readList(register, RPI2ARDexpected_response_count)
    
    if (ARD2RPIresponse1[0] >= 0) and (ARD2RPIresponse1[0] <= 2):
        IFE_integer_status = ARD2RPIresponse1[0]

#==========================================================================================
def IFFsetAngle(angle):         ##  Two byte command and one byte Reponse
    # Transfers to the Arduino include:  [ command],[angle], [Expected response size]  || [status]
    global IFF_integer_status, IFF_status
    global error_string

    if (angle < 0) or (angle > 90):
        error_string = "Angle outside of 0 to 90, setting to 2, angle is: " + str(angle)
        angle = 0

    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 61      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF2bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF2bus.readList(register, RPI2ARDexpected_response_count)

    if (ARD2RPIresponse1[0] >= 0) and (ARD2RPIresponse1[0] <= 2):
        IFF_integer_status = ARD2RPIresponse1[0]

#==========================================================================================
#==========================================================================================
def IFAsetCount(target_count):         ##  Three byte command and one byte Reponse
    global IFA_integer_status, IFA_status

                           #   [0][CMD# 12][High Byte][Low Byte][Size of Response]
    # Transfers to the Arduino include:  [ command],[angle], [Expected response size]
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 12      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response

    target_count_high_byte = (target_count >> 8) & 0xff
    target_count_low_byte = target_count % 256;   

    RPI2ARDcommandList = [RPI2ARDcommand, target_count_high_byte, target_count_low_byte, 
                          RPI2ARDexpected_response_count]  #  Data sent to arduino
    
    # print ("target_count: ", target_count, "   High byte: ", target_count_high_byte, "  Low byte: ", target_count_low_byte)
    # print ("RPI to Ard List: ", RPI2ARDcommandList)

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    if (ARD2RPIresponse1[0] >= 0) and (ARD2RPIresponse1[0] <= 2):
        IFA_integer_status = ARD2RPIresponse1[0]

#==========================================================================================
def IFBsetCount(target_count):         ##  Three byte command and one byte Reponse
    global IFB_integer_status, IFB_status
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 22      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response

    target_count_high_byte = (target_count >> 8) & 0xff
    target_count_low_byte = target_count % 256;   

    RPI2ARDcommandList = [RPI2ARDcommand, target_count_high_byte, target_count_low_byte, 
                          RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    if (ARD2RPIresponse1[0] >= 0) and (ARD2RPIresponse1[0] <= 2):
        IFB_integer_status = ARD2RPIresponse1[0]

#==========================================================================================
def IFCsetCount(target_count):         ##  Three byte command and one byte Reponse
    global IFC_integer_status, IFC_status
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 32      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response

    target_count_high_byte = (target_count >> 8) & 0xff
    target_count_low_byte = target_count % 256;   

    RPI2ARDcommandList = [RPI2ARDcommand, target_count_high_byte, target_count_low_byte, 
                          RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)

    if (ARD2RPIresponse1[0] >= 0) and (ARD2RPIresponse1[0] <= 2):
        IFC_integer_status = ARD2RPIresponse1[0]

#==========================================================================================

#==========================================================================================
def IFDsetCount(target_count):         ##  Three byte command and one byte Reponse
    global IFD_integer_status, IFD_status

                           #   [0][CMD# 12][High Byte][Low Byte][Size of Response]
    # Transfers to the Arduino include:  [ command],[angle], [Expected response size]
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 42      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response

    target_count_high_byte = (target_count >> 8) & 0xff
    target_count_low_byte = target_count % 256;   

    RPI2ARDcommandList = [RPI2ARDcommand, target_count_high_byte, target_count_low_byte, 
                          RPI2ARDexpected_response_count]  #  Data sent to arduino
    
    # print ("target_count: ", target_count, "   High byte: ", target_count_high_byte, "  Low byte: ", target_count_low_byte)
    # print ("RPI to Ard List: ", RPI2ARDcommandList)

    IF2bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF2bus.readList(register, RPI2ARDexpected_response_count)

    if (ARD2RPIresponse1[0] >= 0) and (ARD2RPIresponse1[0] <= 2):
        IFD_integer_status = ARD2RPIresponse1[0]

#==========================================================================================
def IFEsetCount(target_count):         ##  Three byte command and one byte Reponse
    global IFE_integer_status, IFE_status
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 52      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response

    target_count_high_byte = (target_count >> 8) & 0xff
    target_count_low_byte = target_count % 256;   

    RPI2ARDcommandList = [RPI2ARDcommand, target_count_high_byte, target_count_low_byte, 
                          RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF2bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF2bus.readList(register, RPI2ARDexpected_response_count)

    if (ARD2RPIresponse1[0] >= 0) and (ARD2RPIresponse1[0] <= 2):
        IFE_integer_status = ARD2RPIresponse1[0]

#==========================================================================================
def IFFsetCount(target_count):         ##  Three byte command and one byte Reponse
    global IFF_integer_status, IFF_status
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 62      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response

    target_count_high_byte = (target_count >> 8) & 0xff
    target_count_low_byte = target_count % 256;   


    # print ("COMMAND:62 ")
    RPI2ARDcommandList = [RPI2ARDcommand, target_count_high_byte, target_count_low_byte, 
                          RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF2bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF2bus.readList(register, RPI2ARDexpected_response_count)

    if (ARD2RPIresponse1[0] >= 0) and (ARD2RPIresponse1[0] <= 2):
        IFF_integer_status = ARD2RPIresponse1[0]

#==========================================================================================


#==========================================================================================

# Command - Provide status of command  = Command, command // 
# Response for spec command: [ Not started || In Process || Complete ]
# >>	CTR = 2  => SL = 1 		Command = [90] [XX] // [Status IF-A][Status IF-B][Status IF-C]

def request_all_interface_status():  ##  two bytes command and three byte Reponse
    global IFA_integer_status, IFA_status
    global IFB_integer_status, IFB_status
    global IFC_integer_status, IFC_status
    global IFD_integer_status, IFD_status
    global IFE_integer_status, IFE_status
    global IFF_integer_status, IFF_status

    # print ("request_all_interface_status()")

    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 90      # This command
    RPI2ARDexpected_response_count = 3  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)
    IFA_integer_status = ARD2RPIresponse1[0]
    IFB_integer_status = ARD2RPIresponse1[1]
    IFC_integer_status = ARD2RPIresponse1[2]

    #### print ("90 ABC - ARD2RPIresponse1:  ",ARD2RPIresponse1, "  Length: ", len(ARD2RPIresponse1))

    time.sleep(0.2)

    IF2bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse2 = IF2bus.readList(register, RPI2ARDexpected_response_count)
    IFD_integer_status = ARD2RPIresponse2[0]
    IFE_integer_status = ARD2RPIresponse2[1]
    IFF_integer_status = ARD2RPIresponse2[2]

    #### print ("90 DEF - ARD2RPIresponse2:  ",ARD2RPIresponse2, "  Length: ", len(ARD2RPIresponse2))

    # print ("ARD2RPIresponse1 stat ",ARD2RPIresponse1 )
    # print ("IFA_stat: ", IFA_integer_status, "IFB_stat: ", IFB_integer_status, "IFC_stat: ",IFC_integer_status)
    # time.sleep(1)

#==========================================================================================

# Command - Request current counts  //   ##  one byte command and six byte Reponse
# InterfaceA Count [high] [low],InterfaceB Count [high] [low], InterfaceC Count [high] [low]
# >>	CTR = 1  => SL = 6 		Command = [50]   // [A-High] [A-Low][B-High] [B-Low][C-High] [C-Low] 

def request_all_interface_counts():
    global IFA_count, IFB_count, IFC_count, IFD_count, IFE_count, IFF_count
    #### print ("91 - request_all_interface_counts()")

    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 91      # This command
    RPI2ARDexpected_response_count = 6  # count of bytes to be in the response (1 greater than number of bytes returned)
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)
    # print ("91 - ARD2RPIresponse1:  ",ARD2RPIresponse1, "  Length: ", len(ARD2RPIresponse1))

    IFA_count = ARD2RPIresponse1[0] * 256 + ARD2RPIresponse1[1]
    IFB_count = ARD2RPIresponse1[2] * 256 + ARD2RPIresponse1[3]
    IFC_count = ARD2RPIresponse1[4] * 256 + ARD2RPIresponse1[5]

    #### print ("91 ABC - ARD2RPIresponse1:  ",ARD2RPIresponse1, "  Length: ", len(ARD2RPIresponse1))

    time.sleep(0.2)

    IF2bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse2 = IF2bus.readList(register, RPI2ARDexpected_response_count)
    #### print ("91 DEF - ARD2RPIresponse2:  ",ARD2RPIresponse2, "  Length: ", len(ARD2RPIresponse2))
    # print ("Waiting 10")
    # time.sleep(10)

    IFD_count = ARD2RPIresponse2[0] * 256 + ARD2RPIresponse2[1]
    IFE_count = ARD2RPIresponse2[2] * 256 + ARD2RPIresponse2[3]
    IFF_count = ARD2RPIresponse2[4] * 256 + ARD2RPIresponse2[5]

    # print ("50 - IFA_count: ", IFA_count, "   IFB_count: ", IFB_count, "     IFC_count: ", IFC_count, )
    # time.sleep(2.5)
#==(15)=====================================================================================

#==========================================================================================
##  Move the Joint A away from home for 1 second
def IFA_move_slowly_to_home():
    
    # All transfers to the Arduino include:  [the command],[Expected response size]
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 15      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino
    IF1bus.writeList(register,RPI2ARDcommandList)
    time.sleep(1.5)

    # print ("COMMAND: 15 - IF-A - Long way to home ")

#==========================================================================================
##  Move the Joint B away from home for 1 second
def IFB_move_slowly_to_home():
    
    # All transfers to the Arduino include:  [the command],[Expected response size]
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 25      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino
    IF1bus.writeList(register,RPI2ARDcommandList)
    time.sleep(1.5)

    # print ("COMMAND: 25 - IF-B - Long way to home ")

#==========================================================================================
##  Move the Joint C away from home for 1 second
def IFC_move_slowly_to_home():
    
    # All transfers to the Arduino include:  [the command],[Expected response size]
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 35      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino
    IF1bus.writeList(register,RPI2ARDcommandList)
    time.sleep(1.5)

    # print ("COMMAND: 35 - IF-C - Long way to home ")


#==========================================================================================
##  Move the Joint D away from home for 1 second
def IFD_move_slowly_to_home():
    
    # All transfers to the Arduino include:  [the command],[Expected response size]
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 45      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino
    IF2bus.writeList(register,RPI2ARDcommandList)
    time.sleep(1.5)

    # print ("COMMAND: 45 - IF-D - Long way to home ")

#==========================================================================================
##  Move the Joint E away from home for 1 second
def IFE_move_slowly_to_home():
    
    # All transfers to the Arduino include:  [the command],[Expected response size]
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 55      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino
    IF2bus.writeList(register,RPI2ARDcommandList)
    time.sleep(1.5)

    # print ("COMMAND: 55 - IF-E - Long way to home ")

#==========================================================================================
##  Move the Joint F away from home for 1 second
def IFF_move_slowly_to_home():
    
    # All transfers to the Arduino include:  [the command],[Expected response size]
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 65      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino
    IF2bus.writeList(register,RPI2ARDcommandList)
    time.sleep(1.5)

    # print ("COMMAND: 65 - IF-F - Long way to home ")

#==========================================================================================


#==========================================================================================
##  Move the Joint A away from home for 1 second
def IFA_move_toward_home_for_1_second():
    
    # All transfers to the Arduino include:  [the command],[Expected response size]
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 18      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino
    IF1bus.writeList(register,RPI2ARDcommandList)
    time.sleep(1.5)

    # print ("COMMAND: 18 - IF-A - Move toward home ")

#==========================================================================================
##  Move the Joint B away from home for 1 second
def IFB_move_toward_home_for_1_second():
    
    # All transfers to the Arduino include:  [the command],[Expected response size]
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 28      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino
    IF1bus.writeList(register,RPI2ARDcommandList)
    time.sleep(1.5)

    # print ("COMMAND: 28 - IF-B - Move toward home ")

#==========================================================================================
##  Move the Joint C away from home for 1 second
def IFC_move_toward_home_for_1_second():
    
    # All transfers to the Arduino include:  [the command],[Expected response size]
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 38      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino
    IF1bus.writeList(register,RPI2ARDcommandList)
    time.sleep(1.5)

    # print ("COMMAND: 38 - IF-C - Move toward home ")


#==========================================================================================
##  Move the Joint D away from home for 1 second
def IFD_move_toward_home_for_1_second():
    
    # All transfers to the Arduino include:  [the command],[Expected response size]
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 48      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino
    IF2bus.writeList(register,RPI2ARDcommandList)
    time.sleep(1.5)

    # print ("COMMAND: 48 - IF-D - Move toward home ")

#==========================================================================================
##  Move the Joint E away from home for 1 second
def IFE_move_toward_home_for_1_second():
    
    # All transfers to the Arduino include:  [the command],[Expected response size]
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 58      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino
    IF2bus.writeList(register,RPI2ARDcommandList)
    time.sleep(1.5)

    # print ("COMMAND: 58 - IF-E - Move toward home ")

#==========================================================================================
##  Move the Joint F away from home for 1 second
def IFF_move_toward_home_for_1_second():
    
    # All transfers to the Arduino include:  [the command],[Expected response size]
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 68      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino
    IF2bus.writeList(register,RPI2ARDcommandList)
    time.sleep(1.5)

    # print ("COMMAND: 68 - IF-F - Move toward home ")

#==========================================================================================
##  Move the Joint A away from home for 1 second
def IFA_move_away_from_home_for_1_second():
    
    # All transfers to the Arduino include:  [the command],[Expected response size]
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 19      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino
    IF1bus.writeList(register,RPI2ARDcommandList)
    time.sleep(1.5)

    # print ("COMMAND: 19 - IF-A - Move away from home ")

#==========================================================================================
##  Move the Joint B away from home for 1 second
def IFB_move_away_from_home_for_1_second():
    
    # All transfers to the Arduino include:  [the command],[Expected response size]
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 29      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino
    IF1bus.writeList(register,RPI2ARDcommandList)
    time.sleep(1.5)

    # print ("COMMAND: 29 - IF-B - Move away from home ")

#==========================================================================================
##  Move the Joint C away from home for 1 second
def IFC_move_away_from_home_for_1_second():
    
    # All transfers to the Arduino include:  [the command],[Expected response size]
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 39      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino
    IF1bus.writeList(register,RPI2ARDcommandList)
    time.sleep(1.5)

    # print ("COMMAND: 39 - IF-C - Move away from home ")

#==========================================================================================
##  Move the Joint D away from home for 1 second
def IFD_move_away_from_home_for_1_second():
    
    # All transfers to the Arduino include:  [the command],[Expected response size]
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 49      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino
    IF2bus.writeList(register,RPI2ARDcommandList)
    time.sleep(1.5)

    # print ("COMMAND: 49 - IF-D - Move away from home ")

#==========================================================================================
##  Move the Joint E away from home for 1 second
def IFE_move_away_from_home_for_1_second():
    
    # All transfers to the Arduino include:  [the command],[Expected response size]
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 59      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino
    IF2bus.writeList(register,RPI2ARDcommandList)
    time.sleep(1.5)

    # print ("COMMAND: 59 - IF-E - Move away from home ")

#==========================================================================================
##  Move the Joint F away from home for 1 second
def IFF_move_away_from_home_for_1_second():
    
    # All transfers to the Arduino include:  [the command],[Expected response size]
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 69      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino
    IF2bus.writeList(register,RPI2ARDcommandList)
    time.sleep(1.5)

    # print ("COMMAND: 69 - IF-F - Move away from home ")

#==========================================================================================
def IFA_pull_counts_after_one_second_of_movement():

    global IF_A_one_second_count
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 17      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)
    # print ("17 DEF - ARD2RPIresponse1:  ",ARD2RPIresponse1, "  Length: ", len(ARD2RPIresponse1))
    IF_A_one_second_count = ARD2RPIresponse1[0]
    time.sleep(0.5)

def IFB_pull_counts_after_one_second_of_movement():
    global IF_B_one_second_count
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 27      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)
    # print ("27 DEF - ARD2RPIresponse1:  ",ARD2RPIresponse1, "  Length: ", len(ARD2RPIresponse1))
    IF_B_one_second_count = ARD2RPIresponse1[0]
    time.sleep(0.5)

def IFC_pull_counts_after_one_second_of_movement():
    global IF_C_one_second_count
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 37      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)
    # print ("37 DEF - ARD2RPIresponse1:  ",ARD2RPIresponse1, "  Length: ", len(ARD2RPIresponse1))
    IF_C_one_second_count = ARD2RPIresponse1[0]
    time.sleep(0.5)

def IFD_pull_counts_after_one_second_of_movement():

    global IF_D_one_second_count
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 47      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF2bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse2 = IF2bus.readList(register, RPI2ARDexpected_response_count)
    # print ("47 DEF - ARD2RPIresponse2:  ",ARD2RPIresponse2, "  Length: ", len(ARD2RPIresponse2))
    IF_D_one_second_count = ARD2RPIresponse2[0]
    time.sleep(0.5)

def IFE_pull_counts_after_one_second_of_movement():
    global IF_E_one_second_count
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 57      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF2bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse2 = IF2bus.readList(register, RPI2ARDexpected_response_count)
    # print ("57 DEF - ARD2RPIresponse2:  ",ARD2RPIresponse2, "  Length: ", len(ARD2RPIresponse2))
    IF_E_one_second_count = ARD2RPIresponse2[0]
    time.sleep(0.5)

def IFF_pull_counts_after_one_second_of_movement():
    global IF_F_one_second_count
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 67      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF2bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse2 = IF2bus.readList(register, RPI2ARDexpected_response_count)
    # print ("67 DEF - ARD2RPIresponse2:  ",ARD2RPIresponse2, "  Length: ", len(ARD2RPIresponse2))
    IF_F_one_second_count = ARD2RPIresponse2[0]
    time.sleep(0.5)

#=(Main)===================================================================================

def main():
    global IFA_integer_status, IFB_integer_status, IFC_integer_status
    global IFD_integer_status, IFE_integer_status, IFF_integer_status
    global loop_for_status
    logging.basicConfig(filename='python_app.log')

    done = False
    loop_for_status = False   #  Need to get to main menu so we can command to home.

    # print ("Start of While Loop")

    while not done:
        request_all_interface_status()
        request_all_interface_counts()
        map_interface_status_integer_to_text()
        displaycoloredMenu()

        loop_for_status = False
        if (loop_for_status):
            userCommand = "98"
            shortUserCommand = "98"
            loop_for_status = True
            print (">>> LOOPING <<<")
           
            if (IFA_integer_status == 2) and (IFB_integer_status == 2) and (IFC_integer_status == 2) \
            and (IFD_integer_status == 2) and (IFE_integer_status == 2) and (IFF_integer_status == 2):
                # print ("Stat  ",IFA_integer_status, "  ", IFB_integer_status,"  ",  IFC_integer_status)
                loop_for_status = False
            else:
                loop_for_status = True
        else:
            userCommand = input(">>")
            shortUserCommand = "99"    

            if (len(userCommand) >= 2):
                shortUserCommand = userCommand[0:2]

            if (len(userCommand) >= 4):
                position_of_dash = userCommand.find("-")
                parameter = userCommand[(position_of_dash+1):]

        if (userCommand == "0") or (userCommand == "q"):
            done = True

        if userCommand == "1":
            stopAllMotors()

        if userCommand == "2":
            # homeAll()
            homeIFA()
            homeIFB()
            homeIFC()
            homeIFD()
            homeIFE()
            homeIFF()

# - - (Home) - - -

        if userCommand == "10":
            homeIFA()

        if userCommand == "20":
            homeIFB()

        if userCommand == "30":
            homeIFC()

        if userCommand == "40":
            homeIFD()

        if userCommand == "50":
            homeIFE()

        if userCommand == "60":
            homeIFF()
# - - (Set Angle) - - -

        if shortUserCommand == "11":
            IFAsetAngle(int(parameter))

        if shortUserCommand == "21":
            IFBsetAngle(int(parameter))

        if shortUserCommand == "31":
            IFCsetAngle(int(parameter))

        if shortUserCommand == "41":
            IFDsetAngle(int(parameter))

        if shortUserCommand == "51":
            IFEsetAngle(int(parameter))

        if shortUserCommand == "61":
            IFFsetAngle(int(parameter))


# - - (Set Count) - - -

        if shortUserCommand == "12":
            IFAsetCount(int(parameter))
            loop_for_status = True

        if shortUserCommand == "22":
            IFBsetCount(int(parameter))
            loop_for_status = True

        if shortUserCommand == "32":
            IFCsetCount(int(parameter))
            loop_for_status = True

        if shortUserCommand == "42":
            IFDsetCount(int(parameter))
            loop_for_status = True

        if shortUserCommand == "52":
            IFEsetCount(int(parameter))
            loop_for_status = True

        if shortUserCommand == "62":
            IFFsetCount(int(parameter))
            loop_for_status = True

# - - (Find home long way) - - -
        if shortUserCommand == "15":
            IFA_move_slowly_to_home()

        if shortUserCommand == "25":
            IFB_move_slowly_to_home()

        if shortUserCommand == "35":
            IFC_move_slowly_to_home()

        if shortUserCommand == "45":
            IFD_move_slowly_to_home()

        if shortUserCommand == "55":
            IFE_move_slowly_to_home()

        if shortUserCommand == "65":
            IFF_move_slowly_to_home()



# - - (Self Test) - - -

        if userCommand == "6":
            IFA_move_toward_home_for_1_second()
            IFA_move_away_from_home_for_1_second()
            IFA_pull_counts_after_one_second_of_movement()

            IFB_move_toward_home_for_1_second()
            IFB_move_away_from_home_for_1_second()
            IFB_pull_counts_after_one_second_of_movement()

            IFC_move_toward_home_for_1_second()
            IFC_move_away_from_home_for_1_second()
            IFC_pull_counts_after_one_second_of_movement()

            IFD_move_toward_home_for_1_second()
            IFD_move_away_from_home_for_1_second()
            IFD_pull_counts_after_one_second_of_movement()

            IFE_move_toward_home_for_1_second()
            IFE_move_away_from_home_for_1_second()
            IFE_pull_counts_after_one_second_of_movement()

            IFF_move_toward_home_for_1_second()
            IFF_move_away_from_home_for_1_second()
            IFF_pull_counts_after_one_second_of_movement()


        if shortUserCommand == "16":
            IFA_move_toward_home_for_1_second()
            IFA_move_away_from_home_for_1_second()
            IFA_pull_counts_after_one_second_of_movement()

        if shortUserCommand == "26":
            IFB_move_toward_home_for_1_second()
            IFB_move_away_from_home_for_1_second()
            IFB_pull_counts_after_one_second_of_movement()

        if shortUserCommand == "36":
            IFC_move_toward_home_for_1_second()
            IFC_move_away_from_home_for_1_second()
            IFC_pull_counts_after_one_second_of_movement()

        if shortUserCommand == "46":
            IFD_move_toward_home_for_1_second()
            IFD_move_away_from_home_for_1_second()
            IFD_pull_counts_after_one_second_of_movement()

        if shortUserCommand == "56":
            IFE_move_toward_home_for_1_second()
            IFE_move_away_from_home_for_1_second()
            IFE_pull_counts_after_one_second_of_movement()

        if shortUserCommand == "66":
            IFF_move_toward_home_for_1_second()
            IFF_move_away_from_home_for_1_second()
            IFF_pull_counts_after_one_second_of_movement()


# - - (Request Counts after 1 second of movement) - - -

        if shortUserCommand == "17":
            IFA_pull_counts_after_one_second_of_movement()

        if shortUserCommand == "27":
            IFB_pull_counts_after_one_second_of_movement()

        if shortUserCommand == "37":
            IFC_pull_counts_after_one_second_of_movement()

        if shortUserCommand == "47":
            IFD_pull_counts_after_one_second_of_movement()

        if shortUserCommand == "57":
            IFE_pull_counts_after_one_second_of_movement()

        if shortUserCommand == "67":
            IFF_pull_counts_after_one_second_of_movement()

# - - (Forced movement) - - -

        if shortUserCommand == "18":
            IFA_move_toward_home_for_1_second()

        if shortUserCommand == "28":
            IFB_move_toward_home_for_1_second()

        if shortUserCommand == "38":
            IFC_move_toward_home_for_1_second()

        if shortUserCommand == "48":
            IFD_move_toward_home_for_1_second()

        if shortUserCommand == "58":
            IFE_move_toward_home_for_1_second()

        if shortUserCommand == "68":
            IFF_move_toward_home_for_1_second()

# - - (Forced movement) - - -

        if shortUserCommand == "19":
            IFA_move_away_from_home_for_1_second()

        if shortUserCommand == "29":
            IFB_move_away_from_home_for_1_second()

        if shortUserCommand == "39":
            IFC_move_away_from_home_for_1_second()

        if shortUserCommand == "49":
            IFD_move_away_from_home_for_1_second()

        if shortUserCommand == "59":
            IFE_move_away_from_home_for_1_second()

        if shortUserCommand == "69":
            IFF_move_away_from_home_for_1_second()


# - - (Request status) - - -

        if shortUserCommand == "90":     # was 40
            request_all_interface_status()

        if shortUserCommand == "91":     # was 50
            request_all_interface_counts()

        if userCommand == "98":
            request_all_interface_counts()
            time.sleep(0.2)
            request_all_interface_status()

if __name__ == '__main__':
    main()
#==========================================================================================


#==========================================================================================