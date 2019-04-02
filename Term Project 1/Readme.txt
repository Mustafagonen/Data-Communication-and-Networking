As a first, 
We have 5 nodes which names are 's' for source 'B' for broker 'r1' for router 1 'r2' for router 2 'd' for destination.

These are Python socket programming codes for each node.

s --->  client-tcp.py
B --->  broker-udp.py
r1 -->  r1-dp.py
r2 -->  r2-udp.py
d --->  server-udp.py

When we want to test execution of system which we built, we should run codes which we developed for nodes respectively.

As a first,
1.	server-udp.py
2.	r2-udp.py
3.	r1-udp.py
4. 	broker-udp.py
5.	client-tcp.py

After we run client-tcp.py as last, our message is arrived from both router 1 and router 2 to destination(d).
