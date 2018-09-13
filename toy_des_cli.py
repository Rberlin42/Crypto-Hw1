import sys
import socket
import random

#read user input and set up connections
def getCommand():
	#Prompt for command
	command = raw_input("SEND or RECEIVE? ")

	if command == "RECEIVE":
		#listen for connections
		port = int(random.random()*64511 + 1024)
		sock.bind(("", socket.htons(port)))
		sock.listen(1)
		print "Listening for connections on", port
		recvFile()
	elif command == "SEND":
		#get the file
		filename = raw_input("file: ")
		try:
			file = open(filename)
		except:
			print "Could not open file:", filename
			getCommand()

		#Get address
		ip = raw_input("IP: ")
		port = int(input("Port: "))

		#attempt to connect
		try:
			sock.connect((ip, socket.htons(port)))
		except:
			"Unable to connect"
			getCommand()

		sendFile(file)
	else:
		print "Invalid Command"
		getCommand()

#sets up a connection, encrypts the file and sends to the
#given address
def sendFile(file):
	data = None
	while data != "":
		data = file.read(1024)
		sock.sendall(data)

#listens on a port for a connection
#receives a file, decrypts and saves.
def recvFile():
	#wait for connection
	fd, addr = sock.accept()
	print "Conncetion received from", addr

	data = None
	while data != "":
		data = fd.recv(1024)
		print data

	fd.close()



###MAIN###
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
getCommand()
sock.close()