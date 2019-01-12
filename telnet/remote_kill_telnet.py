import os
import time
import SocketServer
import subprocess
from argparse import RawTextHelpFormatter
from multiprocessing import Manager, Pool, Process, cpu_count

manager = Manager()

flag = manager.dict()
def echo_server():

    HOST = "0.0.0.0"
    PORT = 12321
 

 
    class EchoServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
        pass
 
    class EchoRequestHandler(SocketServer.StreamRequestHandler):
        def handle(self):
            print "connection from %s" % self.client_address[0]
            while True:
                line = self.rfile.readline()
                if not line: 
                    break
                flag[line.rstrip()] = 0
                #print(flag)

            print "%s disconnected" % self.client_address[0]

    server = EchoServer((HOST, PORT), EchoRequestHandler)
 
    print "server listening on %s:%s" % server.server_address
    server.serve_forever()

def count():
    x = 1
    
    while True:
        if 'kill' in flag:
            break
        else:
            print x
            time.sleep(1)
            x = x + 1

p = Process(target=echo_server)
c = Process(target=count)
c.start()
p.start()
c.join()
p.join()
print(p)







