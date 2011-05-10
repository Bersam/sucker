'''To use it first you must run aria2c --enable-rpc'''

import xmlrpclib,pexpect
import errno,socket
import thread

directory = "~/Download/aria2"
server = "http://localhost"
port ="6800"

class aria2:
	def __init__(self):
		self.su = xmlrpclib.ServerProxy(server + ":" + port + "/rpc")
	
	def start_download(self,dic):
		try:
			url = dic['url']
			self.su.aria2.addUri([url],dict(dir=directory))
		except socket.error , e:
			if e.errno == errno.ECONNREFUSED:
				self.start_server()
			else:
				raise

	def start_server(self):
		ss = pexpect.run("aria2c --enable-rpc --rpc-listen-port %d" % (port))
			 
	def shutdown_server(self):
		self.su.aria2.shutdown()

	def status(self,gid):
		self.su.aria2.tellStatus(gid)

	def activate(self, shell):
		print ("aria2 plugin Activated")

	def deactivate(self, shell):
		print ("aria2 plugin Deactivated")