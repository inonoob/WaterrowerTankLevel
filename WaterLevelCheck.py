import serial
from time import sleep
import struct
import os.path

def CheckWaterrowerConnected():
	if os.path.exists("/dev/ttyACM0"):
		print("File exist")
		UsbRower = "/dev/ttyACM0"
		ser = serial.Serial(UsbRower, 19200, timeout=0.01)
	else:
		print("File not their")
		ser = 0
	return ser

def initWaterrower(ser):

	ser.write(b'USB\r\n')					# init the connection to the waterrower by sending the command "USB"
	sleep(0.5)
	ser.write(b'IRS0A9\r\n')

def CheckWaterLevel(ser):

	while True:
		ser.write(b'IRS0A9\r\n')			# send commande to waterrower in order to get value for the tank
		#ser.write(b'IRS47E\r\n')
		feedback = ser.readlines()			# read result
		#print(feedback)
		for element in feedback:
			if element[0:6]== b'IDS0A9':
				Tank_size_hex = feedback[-1][6:8] 	# extract the hex value for the tank e.g AA = 170 = 17.0 liter
				struct.unpack("h", Tank_size_hex)	# change it from bin to hexdecimal
				Tank_size_dec = int(Tank_size_hex,16) # convert hex to int
				Tank_size_dec = int(Tank_size_dec)
				print("Tankinhalt ist: {0} l".format(Tank_size_dec/10))			# devide value by 10 to get it in liters
			else:
				pass

		sleep(1) # wait 0.5 sec before start a new query to check new value

def CloseConnection(ser):
	print(ser.isOpen())
	ser.close()
	print(ser.isOpen())


if __name__ == '__main__':
	try:
		Waterrower = CheckWaterrowerConnected()
		initWaterrower(Waterrower)
		CheckWaterLevel(Waterrower)
	except KeyboardInterrupt:
		print('Interrupted')
		CloseConnection(Waterrower)
	# except:
	# 	print('program failed somewhere')
	# 	CloseConnection(Waterrower)
