import socket
import time
import sys

host = '172.17.1.26'
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #we created socket object usint TCP

s.connect((host, port)) #we connected target

sending_time=time.clock()

for i in range(1000):
        s.send(str(sending_time)) #we sent time' 1000 times

