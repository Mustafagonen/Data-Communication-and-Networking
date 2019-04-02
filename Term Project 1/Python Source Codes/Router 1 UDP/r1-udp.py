import socket

l_host = ""
l_port = 5000
bufferSize = 1024


server_port_sender  = ("172.17.1.27", 5000)



# Create socket
socket_udp_server = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)



# Bind to address and ip
socket_udp_server.bind((l_host, l_port))
print("Now R1 is listening via UDP")




while(True):

    addrs_bytes = socket_udp_server.recvfrom(bufferSize)

    msg = addrs_bytes[0]

    addr = addrs_bytes[1]

    msg_from_client = "Received message  from Client:{}".format(msg)
    ip_from_client  = "Receieved Client IP :{}".format(addr)

    print(msg_from_client)
    print(ip_from_client)



    # Sending a reply to client

    socket_udp_server.sendto(msg, server_port_sender)

