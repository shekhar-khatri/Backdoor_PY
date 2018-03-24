import socket, sys, time

class Client:
	def __init__(self):

		try:
			#server host address
			self.host = "localhost" 
			#server port address
			self.port = 8095 
			#new socket object
			self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except:
			print("[!] Couldnot create socket object.")
		print("[*] Application Initialized")

	def connect(self):
		#try connecting to server every 3 secs
		try:
			self.client.connect((self.host, self.port))
			print("[*] Connected to command server.")
		except:
			print("[!] Command Server Down. Reconnecting...")
			time.sleep(3)
			self.connect()

	def get_command(self):
		while True:
			#receive data from command server
			response = self.client.recv(1024)
			if (len(response) > 0):
				#decode utf-8
				response = response.decode("utf-8")
				print("Server: ", response)
				self.client.send(">".encode("utf-8"))

	# def check_command(self, command):
	# 	if (command in ['Hello', 'Hi']):
	# 		print("Hello Accepted")
	# 	elif (command in ['exit', 'Exit', 'quit', 'halt']):
	# 		print("[*] Requested a halt in client execution.")
	# 		print("[*] Exiting... ")
	# 		self.client.close()
	# 		sys.exit(0)
	# 	else:
	# 		print("Server:",response)

	def main(self):
		self.connect()
		self.get_command()
		self.client.close()

client = Client()
client.main()
