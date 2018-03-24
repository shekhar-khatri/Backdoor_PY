import sys, os, traceback, types

class Admin:
	def __init__(self):
		pass

	def isUserAdmin(self):
		#if os is windows
		if (os.name == 'nt'):
			import ctypes
			#only works on windows > xp sp2
			try:
				return ctypes.windll.shell32.IsUserAnAdmin()
			except:
				traceback.print_exc()
				print("[!] Failed to check Admin Status.")
				return False
		#if os is posix (unix)
		elif (os.name == 'posix'):
			return os.getuid() == 0
		else:
			raise RuntimeError, "[!] Unsupported Operating System."
	


