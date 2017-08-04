#!/usr/bin/python
#import socket

import socket
import sys

#create an AF_INET(IPv4) and STREAM socket(TCP)

try:
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print('Failed to create socket, Error code: ', str(msg[0]), 'Error message: ', msg[1])
    sys.exit();

print('socket created')

port=socket.getservbyname('http', 'tcp')

my_socket.connect(('127.0.0.1', 9999))

print('connect from', my_socket.getsockname())
print('connect to', my_socket.getpeername())

while True:

    inp=input('>>>')
    if inp=='exit'or not inp:
        my_socket.sendall(bytes(inp, encoding='utf-8'))
        break
    my_socket.sendall(bytes(inp, encoding='utf-8'))
    server_response=my_socket.recv(1024)
    print(str(server_response, encoding='utf-8'))
my_socket.close()
