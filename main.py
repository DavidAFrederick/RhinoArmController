from colorama import Fore, Back, Style
import os
import smbus
import time
import sys
import logging
from adafruit_I2C_lib import I2C

##  Dec 11, 2023 - Interface A working
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

    os.system('clear')   
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
    print("]")

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    print (" ")
    print (F"{Style.BRIGHT}Commands:")
    print (F"{Style.NORMAL}Stop all   - 1")
    print ("Home all   - 2")
    print ("                             Joint Commands")
    print (" ")
    print ("              A        B        C        D        E        F   ")
    print ("Home One   - 10,      20,      30,      40,      50,      60")
    print ("Set Angle  - 11-xx,   21-xx,   31-xx,   41-xx,   51-xx,   61-xx")
    print ("Set Count  - 12-xxxx, 22-xxxx, 32-xxxx, 42-xxxx, 52-xxxx, 62-xxxx")
    print (" ")
    print ("Get Status - 40")
    print ("Set Count  - 50")
    print (" ")
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

# Command - Provide status of command  = Command, command // 
# Response for spec command: [ Not started || In Process || Complete ]
# >>	CTR = 2  => SL = 1 		Command = [40] [XX] // [Status IF-A][Status IF-B][Status IF-C]

def request_all_interface_status():  ##  two bytes command and three byte Reponse
    global IFA_integer_status, IFA_status
    global IFB_integer_status, IFB_status
    global IFC_integer_status, IFC_status
    global IFD_integer_status, IFD_status
    global IFE_integer_status, IFE_status
    global IFF_integer_status, IFF_status

    # print ("request_all_interface_status()")

    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 40      # This command
    RPI2ARDexpected_response_count = 3  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)
    IFA_integer_status = ARD2RPIresponse1[0]
    IFB_integer_status = ARD2RPIresponse1[1]
    IFC_integer_status = ARD2RPIresponse1[2]

    # print ("ARD2RPIresponse1 stat ",ARD2RPIresponse1 )
    # print ("IFA_stat: ", IFA_integer_status, "IFB_stat: ", IFB_integer_status, "IFC_stat: ",IFC_integer_status)
    # time.sleep(1)

#==========================================================================================

# Command - Request current counts  //   ##  one byte command and six byte Reponse
# InterfaceA Count [high] [low],InterfaceB Count [high] [low], InterfaceC Count [high] [low]
# >>	CTR = 1  => SL = 6 		Command = [50]   // [A-High] [A-Low][B-High] [B-Low][C-High] [C-Low] 

def request_all_interface_counts():
    global IFA_count, IFB_count, IFC_count
    # print ("50 - request_all_interface_counts()")

    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 50      # This command
    RPI2ARDexpected_response_count = 6  # count of bytes to be in the response (1 greater than number of bytes returned)
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino

    IF1bus.writeList(register,RPI2ARDcommandList)
    ARD2RPIresponse1 = IF1bus.readList(register, RPI2ARDexpected_response_count)
    # print ("50 - ARD2RPIresponse1:  ",ARD2RPIresponse1, "  Length: ", len(ARD2RPIresponse1))

    IFA_count = ARD2RPIresponse1[0] * 256 + ARD2RPIresponse1[1]
    IFB_count = ARD2RPIresponse1[2] * 256 + ARD2RPIresponse1[3]
    IFC_count = ARD2RPIresponse1[4] * 256 + ARD2RPIresponse1[5]

    # print ("50 - IFA_count: ", IFA_count, "   IFB_count: ", IFB_count, "     IFC_count: ", IFC_count, )
    # time.sleep(2.5)


#==========================================================================================
##  Move the Joint A away from home for 1 second
def IFA_move_from_below_home_for_1_second():
    
    # All transfers to the Arduino include:  [the command],[Expected response size]
    register = 0            # Not used just setting to zero
    RPI2ARDcommand = 19      # This command
    RPI2ARDexpected_response_count = 1  # count of bytes to be in the response
    RPI2ARDcommandList = [RPI2ARDcommand,RPI2ARDexpected_response_count]  #  Data sent to arduino
    IF1bus.writeList(register,RPI2ARDcommandList)

    # print ("COMMAND: 19 - IFA - Move away from home ")


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

        if (loop_for_status):
            userCommand = "90"
            shortUserCommand = "90"
            loop_for_status = True
            print (">>> LOOPING <<<")

            IFB_integer_status = 2
            IFC_integer_status = 2
            
            if (IFA_integer_status == 2) and (IFB_integer_status == 2) and (IFC_integer_status == 2):
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
            homeAll()

        if userCommand == "10":
            homeIFA()

        if userCommand == "20":
            homeIFB()

        if userCommand == "30":
            homeIFC()

        if shortUserCommand == "11":
            IFAsetAngle(int(parameter))

        if shortUserCommand == "21":
            IFBsetAngle(int(parameter))

        if shortUserCommand == "31":
            IFCsetAngle(int(parameter))

        if shortUserCommand == "12":
            IFAsetCount(int(parameter))
            loop_for_status = True

        if shortUserCommand == "22":
            IFBsetCount(int(parameter))
            loop_for_status = True

        if shortUserCommand == "32":
            IFCsetCount(int(parameter))
            loop_for_status = True

        if shortUserCommand == "19":
            IFA_move_from_below_home_for_1_second()

        if shortUserCommand == "40":
            request_all_interface_status()

        if shortUserCommand == "50":
            request_all_interface_counts()

        # if userCommand == "90":
        #     request_all_interface_counts()
        #     time.sleep(0.2)
        #     request_all_interface_status()

if __name__ == '__main__':
    main()
#==========================================================================================


#==========================================================================================