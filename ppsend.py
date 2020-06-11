import socket
import sys
import ntpath

s = socket.socket()
s.connect((sys.argv[1],9999))
s.send(ntpath.basename(sys.argv[2]).encode())
s.close()

s = socket.socket()
s.connect((sys.argv[1],9999))
f = open(sys.argv[2],"rb")
l = f.read(1024)
while (l):
	s.send(l)
	l = f.read(1024)
s.close()
