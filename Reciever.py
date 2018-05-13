from socket import *
import time
host = "0.0.0.0" #coonect me First
port = 4455
s=socket(AF_INET,SOCK_STREAM)
s.bind((host,port))
s.listen(1)
conn , addr = s.accept()
print "Connected By....." , addr
while True:
    data=conn.recv(1024)
    print "Recieved: " ,repr(data)
    reply = raw_input("Reply:")
    conn.sendall(reply)
conn.close()
