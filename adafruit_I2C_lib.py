############################################################################################
#
#  Adafruit i2c interface plus bug fix
# https://learn.adafruit.com/working-with-i2c-devices
# https://arduino.stackexchange.com/questions/81245/reading-i2c-registers-as-slave-device
# https://docs.python.org/2/tutorial/errors.html#user-defined-exceptions
#
############################################################################################
# import smbus
import time
import logging



class I2C:

    # counter = 0

    # def __init__(self, address):
    #     self.address = address
        
    # def writeList (reg, tbd, in_list):
    #     pass
    
    # def readList(reg, tbd, out_list):
        
    #     list1 = [0,0,0,4,5,6,7,8]  
    #     counter = input("Enter Counter value: ")
    #     if (counter == "1"): list1 = [1,1,1,4,5,6,7,8]  
    #     if (counter == "2"): list1 = [2,2,2,4,5,6,7,8]  
    #     if (counter == "3"): list1 = [1,2,2,4,5,6,7,8]  
        
    #     print (list1)
    #     return list1

        #                   IF1bus.writeList (register,RPI2ARDcommandList)
        # ARD2RPIresponse1 = IF1bus.readList (register, RPI2ARDexpected_response_count)


    logging.basicConfig(filename='/tmp/python_app2.log', level=logging.DEBUG)

    def __init__(self, address, bus=smbus.SMBus(1)):
        self.address = address
        self.bus = bus

    def reverseByteOrder(self, data):
        #'''Reverses the byte order of an int (16-bit) or long (32-bit) value'''
        # Courtesy Vishal Sapre
        dstr = hex(data)[2:].replace('L','')
        byteCount = len(dstr[::2])
        val = 0
        for i, n in enumerate(range(byteCount)):
            d = data & 0xFF
            val |= (d << (8 * (byteCount - i - 1)))
            data >>= 8
        return val

    def write8(self, reg, value):
        "Writes an 8-bit value to the specified register/address"
        while True:
            try:
                self.bus.write_byte_data(self.address, reg, value)
                #logger.debug('I2C: Wrote 0x%02X to register 0x%02X', value, reg)
                # logging.debug('I2C: Wrote 0x%02X to register 0x%02X', value, reg)
                # print('I2C: Wrote 0x%02X to register 0x%02X', value, reg)
                break
#			except IOError, err:
            except IOError:
                # print('Error %d, %s accessing 0x%02X: Check your I2C address'% (err.errno, err.strerror, self.address))
                time.sleep(0.001)

    def writeList(self, reg, list):
        "Writes an array of bytes using I2C format"
        while True:
            try:
                self.bus.write_i2c_block_data(self.address, reg, list)
                break
            except IOError:
#			except IOError, err:
#				logger.exception('Error %d, %s accessing 0x%02X: Check your I2C address', err.errno, err.strerror, self.address)
                # print('Error %d, %s accessing 0x%02X: Check your I2C address'%(err.errno, err.strerror, self.address))
                time.sleep(0.001)

    def readU8(self, reg):
        "Read an unsigned byte from the I2C device"
        while True:
            try:
                result = self.bus.read_byte_data(self.address, reg)
                # logging.debug('I2C: Device 0x%02X returned 0x%02X from reg 0x%02X', self.address, result & 0xFF, reg)
                # print('I2C: Device 0x%02X returned 0x%02X from reg 0x%02X', self.address, result & 0xFF, reg)
                return result
            except IOError:
#			except IOError, err:
#				logger.exception('Error %d, %s accessing 0x%02X: Check your I2C address', err.errno, err.strerror, self.address)
                # print('Error %d, %s accessing 0x%02X: Check your I2C address'%(err.errno, err.strerror, self.address))
                time.sleep(0.001)

    def readS8(self, reg):
        "Reads a signed byte from the I2C device"
        while True:
            try:
                result = self.bus.read_byte_data(self.address, reg)
#				logger.debug('I2C: Device 0x%02X returned 0x%02X from reg 0x%02X', self.address, result & 0xFF, reg)
                print('I2C: Device 0x%02X returned 0x%02X from reg 0x%02X'% (self.address, result & 0xFF, reg))
                if (result > 127):
                    return result - 256
                else:
                    return result
            except IOError:
#			except IOError, err:
#				logger.exception('Error %d, %s accessing 0x%02X: Check your I2C address', err.errno, err.strerror, self.address)
                # print('Error %d, %s accessing 0x%02X: Check your I2C address'% (err.errno, err.strerror, self.address))
                time.sleep(0.001)

    def readU16(self, reg):
        "Reads an unsigned 16-bit value from the I2C device"
        while True:
            try:
                hibyte = self.bus.read_byte_data(self.address, reg)
                result = (hibyte << 8) + self.bus.read_byte_data(self.address, reg+1)
#				# logger.debug('I2C: Device 0x%02X returned 0x%04X from reg 0x%02X', self.address, result & 0xFFFF, reg)
                print('I2C: Device 0x%02X returned 0x%04X from reg 0x%02X'%( self.address, result & 0xFFFF, reg))
                if result == 0x7FFF or result == 0x8000:
                    print('I2C read max value')
                    time.sleep(0.001)
                else:
                    return result
            except IOError:
#			except IOError, err:
#				logger.exception('Error %d, %s accessing 0x%02X: Check your I2C address', err.errno, err.strerror, self.address)
                # print('Error %d, %s accessing 0x%02X: Check your I2C address' % ( err.errno, err.strerror, self.address))
                time.sleep(0.001)

    def readS16(self, reg):
        "Reads a signed 16-bit value from the I2C device"
        while True:
            try:
                hibyte = self.bus.read_byte_data(self.address, reg)
                if (hibyte > 127):
                    hibyte -= 256
                result = (hibyte << 8) + self.bus.read_byte_data(self.address, reg+1)
                print('I2C: Device 0x%02X returned 0x%04X from reg 0x%02X', self.address, result & 0xFFFF, reg)
                if result == 0x7FFF or result == 0x8000:
                    print('I2C read max value')
                    time.sleep(0.001)
                else:
                    return result
            except IOError:
#			except IOError, err:
#				logger.exception('Error %d, %s accessing 0x%02X: Check your I2C address', err.errno, err.strerror, self.address)
                # print('Error %d, %s accessing 0x%02X: Check your I2C address' %(err.errno, err.strerror, self.address))
                time.sleep(0.001)
                
    def readList(self, reg, length):
        "Reads a a byte array value from the I2C device"
        while True:
            try:
                result = self.bus.read_i2c_block_data(self.address, reg, length)                
                # result = self.bus.read_block_data(self.address, reg)                
                # result = self.bus.read_block_data(self.address, reg)
                # print ("result")
                
#				logging.debug('I2C: Device 0x%02X from reg 0x%02X', self.address, reg)
#				print('I2C: Device 0x%02X from reg 0x%02X', self.address, reg)
                # print('Received data', reg, result)
                return result
            except IOError:
                logging.exception('Error')
                print ("ERROR--")
#			except IOError, err:
#				logger.exception('Error %d, %s accessing 0x%02X: Check your I2C address', err.errno, err.strerror, self.address)
                # print('Error %d, %s accessing 0x%02X: Check your I2C address'% (err.errno, err.strerror, self.address))
                time.sleep(0.001)
