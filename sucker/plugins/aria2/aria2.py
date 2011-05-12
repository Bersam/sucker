'''To use it first you must run aria2c --enable-rpc'''

import subprocess
import xmlrpclib

server = "http://localhost"
port = 6800

class aria2:
    def __init__(self):
        self.su = xmlrpclib.ServerProxy("%s:%d/rpc" % (server, port))

        self.aria_process = None
    
    def start_download(self,dic):
        if self.aria_process == None:
            self.start_server()
        url = dic['url']
        args = {
            'dir':dic['dir'],
        }
        print url
        self.su.aria2.addUri([url], args)
        print('downloaded')

    def start_server(self):
        command = 'aria2c --enable-rpc --rpc-listen-port %d' %  port

        self.aria_process = subprocess.Popen(command.split(' '))
        while True:
            try:
             
    def shutdown_server(self):
        self.su.aria2.shutdown()

    def status(self,gid):
        self.su.aria2.tellStatus(gid)

    def activate(self, shell):
        print ("aria2 plugin Activated")

    def deactivate(self, shell):
        print ("aria2 plugin Deactivated")
