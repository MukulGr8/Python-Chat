from socket import *
import os
host = "192.168.3.2"  #ip of victim
port = 4455
s=socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.connect((host,port))
while True:
    msg = raw_input("Your Message:")
    s.send(msg)
    print "Awaiting Reply......."
    reply = s.recv(1024)
    print "Recieved:" , repr(reply)
s.close()
