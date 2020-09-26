##test program for use with https://github.com/RoboDurden/hoverboard-firmware-hack

import serial
import zlib
import time
from getkey import getkey, keys

ser = serial.Serial('/dev/serial0', 9600)  # open front serial port
ser2 =serial.Serial('/dev/ttyUSB0', 9600)  # open rear serial port 

def sendcmd(steer,speed):
	steerB = (steer).to_bytes(2, byteorder='little', signed=True) #16 bits
	speedB = (speed).to_bytes(2, byteorder='little', signed=True) #16 bits
	crcB = zlib.crc32(steerB+speedB).to_bytes(4, byteorder='little') #32 bit CRC of byte-joined command
	ser.write(steerB)
	ser.write(speedB)
	ser.write(crcB)

	ser2.write(steerB)
	ser2.write(speedB)
	ser2.write(crcB)

while (1):
        key = getkey()
        if key == 'w':
                print("forward")
                sendcmd(0,250)
        elif key == 'a':
                print("left")
                sendcmd(-350,0)
        elif key == 's':
                print("back")
                sendcmd(0,-250)
        elif key == 'd':
                print("right")
                sendcmd(350,0)
        else:
                print("stop")
                sendcmd(0,0)
        def do_exit(self,*args):
                return True

ser.close()
