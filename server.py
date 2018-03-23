import socket
import sys

class Server:
	#initialize variables
	def __init__(self):
		#server host and port
		self.host  = sys.argv[1]
		self.port = int(sys.argv[2])

		#initialize a server socket
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#prevents from getting timeout issues
		self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		print("[*] Application Initialized.")
		print("[*] Host:", self.host,"Port:", self.port)

	def main(self):
		#bind server to host and port
		self.server.bind((self.host, self.port))
		print("[*] Bind socket to host successful.")
		#start listening to connections
		self.server.listen(5)
		print("[*] Listening started on", self.host, ":", self.port)

	def run_command(self, connection):
		#get user input
		command = input("> ")
		#encode data into utf-8 to send through socket
		command = command.encode("utf-8")
		connection.send(command)

	def accept_connection(self):
		connection, addr = self.server.accept()
		print("Connected to: {0}:{1}".format(addr[0], addr[1]))
		while True:
			self.run_command(connection)



server = Server()
server.main()
server.accept_connection()



