As a first, 
We have 5 nodes which names are 's' for source 'B' for broker 'r1' for router 1 'r2' for router 2 'd' for destination.

These are Python socket programming codes for each node.

s --->  sTcpClient.py
B --->  brokerUdp.py
r1 -->  r1Udp.py
r2 -->  r2Udp.py
d --->  dUdpServer.py

When we want to test execution of system which we built, we should run codes which we developed for nodes respectively.

As a first,
1.	dUdpServer.py
2.	r2Udp.py
3.	r1Udp.py
4. 	brokerUDp.py
5.	sTcpClient.py

After we run sTcpClient as last, our message is arrived from both router 1 and router 2 to destination(d).


