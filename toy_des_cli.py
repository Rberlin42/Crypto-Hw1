import sys
import socket

#read user input
def getCommand():
	#Prompt for command
	command = raw_input("SEND or LISTEN? ")

	if command == "LISTEN":
		recvFile()
	elif command == "SEND":
		#get the file
		filename = raw_input("file: ")
		try:
			file = open(filename)
		except:
			print "Could not open file: ", filename
			getCommand()

		#Get address
		ip = raw_input("IP: ")
		port = int(input("Port: "))

		#attempt to connect
		sock.connect((ip, socket.htons(port)))

		sendFile()
	else:
		print "Invalid Command"
		getCommand()

#sets up a connection, encrypts the file and sends to the
#given address
def sendFile(file, ip, port):
	print "send"

#listens on a port for a connection
#receives a file, decrypts and saves.
def recvFile():
	print "recv"

###MAIN###
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
getCommand()