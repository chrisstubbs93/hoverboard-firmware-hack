##test program for use with https://github.com/RoboDurden/hoverboard-firmware-hack

import serial
import zlib

ser = serial.Serial('/dev/serial0', 9600)  # open front serial port

def rxcmd():
	SerialFeedbackLen = 20
	buf = bytearray()
	if ser.inWaiting() >= SerialFeedbackLen:
		for x in range(0, SerialFeedbackLen, 1):
			buf += bytearray(ser.read())
		crcR = zlib.crc32(buf[0:SerialFeedbackLen-4]).to_bytes(4, byteorder='little')
		if crcR == buf[SerialFeedbackLen-4:SerialFeedbackLen]:
			print("Checksum OK")
			iSpeedL = ((int.from_bytes(buf[0:2], byteorder='little', signed=True))/100)
			iSpeedR = ((int.from_bytes(buf[2:4], byteorder='little', signed=True))/100)
			iHallSkippedL = (int.from_bytes(buf[4:6], byteorder='little', signed=False))
			iHallSkippedR = (int.from_bytes(buf[6:8], byteorder='little', signed=False))
			iTemp = (int.from_bytes(buf[8:10], byteorder='little', signed=False))
			iVolt = ((int.from_bytes(buf[10:12], byteorder='little', signed=False))/100)
			iAmpL = ((int.from_bytes(buf[12:14], byteorder='little', signed=True))/100)
			iAmpR = ((int.from_bytes(buf[14:16], byteorder='little', signed=True))/100)
			print("iSpeedL (km/h): ", iSpeedL)
			print("iSpeedR (km/h): ", iSpeedR)
			print("iHallSkippedL: ", iHallSkippedL)
			print("iHallSkippedR: ", iHallSkippedR)
			print("iTemp: (degC)", iTemp)
			print("iVolt: (V)", iVolt)
			print("iAmpL: (A)", iAmpL)
			print("iAmpR: (A)", iAmpR)
			print("Power: (W)", (iAmpR+iAmpL)*iVolt)
			print("Power: (HP)", (iAmpR+iAmpL)*iVolt*0.00134102)
			print("=========================================")
		else:
			print("!!-CHECKSUM FAIL-!!")

try:
	while (1):
		rxcmd()
finally:
	print("Closing port")
	ser.close()
