import socket
import threading

binding_host = ''
binding_port = 5000

s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_tcp.bind((binding_host, binding_port))
s_tcp.listen(7)  # bounded connection

send_for_r1  = ("172.17.1.28", 5000)
send_for_r2  = ("172.17.1.29", 5000)



print 'Now Broker is listening {}:{}'.format(binding_host, binding_port)


def client_connection(socket_tcp ): #client socket for tcp
        while(True):
                demand = socket_tcp.recv(1024)
                if(not demand): break
                print 'it is accepted {}'.format(demand)
                socket_udp_r1 = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
                socket_udp_r2 = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
                socket_udp_r1.sendto(demand , send_for_r1)
                socket_udp_r2.sendto(demand , send_for_r2)



while True:
    socket_client, addr = s_tcp.accept()
    print 'It is receieved from {}:{}'.format(addr[0], addr[1])
    constructor_client = threading.Thread(
        target=client_connection,
        args=(socket_client,)
    )
    constructor_client.start()

