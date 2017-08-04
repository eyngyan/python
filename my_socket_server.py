#!/usr/bin/python
#socket server

import socket
import threading
import random

#??socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#??IP?port
s.bind(('127.0.0.1', 9999))

#????socket.listen(backlog)?backlog??????
s.listen(5)


#????link?
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    true=True
    while true:

        data = sock.recv(1024)
        #time.sleep(1)
        #number = random.randint(1,6)
        #sock.send('There is a number in my hand, guess 3 times!')
        #sock.send(number)

        if data.decode('utf-8')=='exit':
            true=False
            break
        elif data.decode('utf-8')=='hello':
            number = random.randint(1,6)
            sock.send(bytes('There is a number in my hand, guess 3 times!', encoding='utf-8'))
            #sock.send(bytes(number), encoding='utf-8')
            time=3
            while time>0:
                time=time-1

                if data.decode('utf-8')==str(number):
                    sock.send(bytes('Conguratulations'))
                    break
                elif data.decode('utf-8')<str(number):
                    sock.send(bytes('small', encoding='utf-8'))
                    #print('??')
                else:
                    sock.send(bytes('more', encoding='utf-8'))
                    #print('??')

    sock.close()
    print('Connection from %s:%s closed.' % addr)

while True:
    print('server is running')
    print('waiting for connection......')
    sock, addr=s.accept()
    trd=threading.Thread(target=tcplink, args=(sock, addr))
    trd.start()

