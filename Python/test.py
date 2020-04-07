##test program for use with https://github.com/RoboDurden/hoverboard-firmware-hack

import serial
import zlib
ser = serial.Serial('COM3', 9600)  # open serial port

def sendcmd(steer,speed):
	steerB = (steer).to_bytes(2, byteorder='little', signed=True) #16 bits
	speedB = (speed).to_bytes(2, byteorder='little', signed=True) #16 bits
	crcB = zlib.crc32(steerB+speedB).to_bytes(4, byteorder='little') #32 bit CRC of byte-joined command
	ser.write(steerB)
	ser.write(speedB)
	ser.write(crcB)

while(1):
	s = int(input("Speed:"))
	sendcmd(0,s)

	def do_exit(self,*args):
		return True

ser.close()