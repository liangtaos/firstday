import threading
import SocketServer

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        while True:
            self.cmd = self.request.recv(1024).strip()
            self.cmd_list = self.cmd.split()
            if self.cmd_list:
                if self.cmd_list[0] == 'get':
                    with open(self.cmd_list[1]) as fd:
                        while True:
                            self.data = fd.read(1024)
                            self.request.sendall(self.data)
                            if not self.data:
                                self.request.sendall('EOF')
                                break
            if not self.cmd: break

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == "__main__":
    HOST = ""
    PORT = 9997

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print "Server loop running in thread:", server_thread.name

    server.serve_forever()

