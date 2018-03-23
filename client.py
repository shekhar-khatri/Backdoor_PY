import socket
import sys

class Client:
	def __init__(self):
		self.host = "localhost" #command server
		self.port = 8095 #command port
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket object
		print("[*] Application Initialized")

	def connect(self):
		self.client.connect((self.host, self.port))
		print("[*] Connected to command server.")

	def get_command(self):
		while True:
			#receive data from command server
			response = self.client.recv(1024)
			if (len(response) > 0):
				#decode utf-8
				response = response.decode("utf-8")
				print("Server:",response)

	def main(self):
		self.connect()
		self.get_command()

client = Client()
client.main()
