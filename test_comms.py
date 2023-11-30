'''
i2c_v1.py
Simple Python 3 script to test I2C by alternately
sending a 1 and 0 over I2C every second and reading
back the response from the Arduino
Tested on Raspberry Pi 4 B+ and Adafruit Feather M0+
'''
import smbus
import time
import sys
from adafruit_i2c_library import I2C

address = 0x08
buss = I2C(address)

# bus = smbus.SMBus(1)
# address = 0x08              # Arduino I2C Address

def main():
    i2cData = [1,12,45]
    i2cDataReceived = []
    while 1:
        # send data
#        i2cData = not i2cData
#        buss.writeList(address,0,i2cData)
        buss.writeList(address,i2cData)
#        i2cDataReceived = buss.readList(address,0,3)
      #  i2cDataReceived = buss.readList(address,3)
#        print (i2cDataReceived)
        
        # request data
#        print ("Arduino answer to RPi:", bus.read_byte(address))
        
        time.sleep(1)
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        gpio.cleanup()
        sys.exit(0)

