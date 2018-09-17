import sys
import socket
import random
import toy_des as des

#convert bytes to a string of bits
def getBits(byte):
	hexi = byte.hex()
	binary = bin(int(hexi, 16))[2:]
	#add leading 0s
	while len(binary) < len(byte)*8:
		binary = "0" + binary
	return binary

#convert a string of bits to bytes
def getBytes(binary):
	hexi = hex(int("0b"+binary, 2))[2:]
	#add leading 0s
	while len(hexi) < len(binary)/4:
		hexi = "0" + hexi
	return bytes.fromhex(hexi)

#read user input and set up connections
def getCommand():
	#Prompt for command
	command = input("SEND or RECEIVE? ")

	if command == "RECEIVE":
		#listen for connections
		port = int(random.random()*64511 + 1024)
		sock.bind(("", socket.htons(port)))
		sock.listen(1)
		print("Listening for connections on", port)
		recvFile()
	elif command == "SEND":
		#get the file
		filename = input("file: ")
		try:
			file = open(filename, "rb")
		except:
			print ("Could not open file:", filename)
			getCommand()

		#Get address
		ip = input("IP: ")
		port = int(input("Port: "))

		#attempt to connect
		try:
			sock.connect((ip, socket.htons(port)))
		except:
			"Unable to connect"
			getCommand()

		sendFile(file)
	else:
		print("Invalid Command")
		getCommand()

#sets up a connection, encrypts the file and sends to the
#given address
def sendFile(file):
	#Send name of file first
	#ENCRYPT
	cypher = des.encrypt(getBits(bytes(file.name, "utf-8")), key)
	sock.sendall(getBytes(cypher))

	#Wait for acknowledgement
	ack = sock.recv(1024)
	if ack != b'ACK': 
		print("yh")
		return

	#Send the rest
	data = file.read(1024)
	while len(data) != 0:
		#ENCRYPT
		cypher = des.encrypt(getBits(data), key)
		sock.sendall(getBytes(cypher))
		data = file.read(1024)
	print("Complete")

#listens on a port for a connection
#receives a file, decrypts and saves.
def recvFile():
	#wait for connection
	fd, addr = sock.accept()
	print("Conncetion received from", addr)

	#receive first packet (filename)
	cypher = fd.recv(1024)
	#DECRYPT
	filename = getBytes(des.decrypt(getBits(cypher), key))
	#open the file
	file = open(filename, "ab")

	#Send Acknowledgement
	fd.sendall(b'ACK')

	cypher = fd.recv(1024)
	while len(cypher) != 0:
		#DECRYPT
		data = des.decrypt(getBits(cypher), key)
		file.write(getBytes(data))
		cypher = fd.recv(1024)

	fd.close()
	print("Received file:", filename)


###MAIN###
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
key = "1100100110"
getCommand()
sock.close()
