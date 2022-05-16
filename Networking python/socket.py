import socket
server_socket=socket.socket(
    socket.AF_INET,socket.SOCK_STREAM
)
host=socket.gethostname()
port=999
serversocket.bind((host, port))
# queue up to 5 requests
serversocket.listen(5)
while True:
 # establish a connection
 clientsocket,addr = serversocket.accept()
 print("Got a connection from %s" % str(addr))

 msg='Thank you for connecting'+ "\r\n"
 clientsocket.send(msg.encode('ascii'))
 clientsocket.close()