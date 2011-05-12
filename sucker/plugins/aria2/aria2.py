'''To use it first you must run aria2c --enable-rpc'''

import errno
import pexpect
import socket
import thread
import xmlrpclib
from pprint import pprint

server = "http://localhost"
port = 6800

class aria2:
	def __init__(self):
		self.su = xmlrpclib.ServerProxy("%s:%d/rpc" % (server, port))
	
	def start_download(self,dic):
		try:
			url = dic['url']
            
            args = {
                'dir':dic['dir'],
            }

			print url
			self.su.aria2.addUri([url], args)
			print('downloaded')
		except socket.error , e:
			if e.errno == errno.ECONNREFUSED:
				self.start_server()
			else:
				raise

	def start_server(self):
		ss = pexpect.run("aria2c  -D --enable-rpc --rpc-listen-port %d" % (port))
			 
	def shutdown_server(self):
		self.su.aria2.shutdown()

	def status(self,gid):
		self.su.aria2.tellStatus(gid)

	def activate(self, shell):
		print ("aria2 plugin Activated")

	def deactivate(self, shell):
		print ("aria2 plugin Deactivated")
