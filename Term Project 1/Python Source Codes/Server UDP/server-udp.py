import socket
import random

srv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
srv_socket.bind(('', 5000))

while True:
    randomm = random.randint(0, 20)
    msg, address = srv_socket.recvfrom(1024)
    msg = msg.upper()
    print('This is your message ' + msg)
