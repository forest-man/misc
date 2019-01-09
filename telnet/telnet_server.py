import os
import SocketServer
 
HOST = "0.0.0.0"
PORT = 12321
 
flag = {}

# this server uses ThreadingMixIn - one thread per connection
# replace with ForkMixIn to spawn a new process per connection
 
class EchoServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    # no need to override anything - default behavior is just fine
    pass
 
class EchoRequestHandler(SocketServer.StreamRequestHandler):
    """
    Handles one connection to the client.
    """
    def handle(self):
        print "connection from %s" % self.client_address[0]
        while True:
            line = self.rfile.readline()
            if not line: 
                break
            flag[line.rstrip()] = 0
            print(flag)
            if 'kill' in flag:
                print('Ku')

        print "%s disconnected" % self.client_address[0]

# Create the server
server = EchoServer((HOST, PORT), EchoRequestHandler)
 
# Activate the server; this will keep running until you
# interrupt the program with Ctrl-C
print "server listening on %s:%s" % server.server_address
server.serve_forever()

