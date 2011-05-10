'''To use it first you must run aria2c --enable-rpc'''

import xmlrpclib

directory = "~/Download/aria2"
server = "http://localhost"
port ="6800"

class aria2:
    def __init__(self):
        self.su = xmlrpclib.ServerProxy(server + ":" + port + "/rpc")
    
    def addurl(self,url):
    	self.su.aria2.addUri([url],dict(dir=directory))
    	#return self.gid

    def status(self,gid):
    	self.su.aria2.tellStatus(gid)

    def activate(self, shell):
        print ("aria2 plugin Activated")

    def deactivate(self, shell):
        print ("aria2 plugin Deactivated")

    def start_download(self, dic):
        print dic
