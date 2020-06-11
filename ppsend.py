import socket
import sys

s = socket.socket()
s.connect((sys.argv[1],9999))
f = open("aaaa","rb")
l = f.read(1024)
while (l):
	s.send(l)
	l = f.read(1024)
s.close()
