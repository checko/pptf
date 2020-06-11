import socket
import sys

s = socket.socket()
s.bind((sys.argv[1],9999))
s.listen(10)

while True:
	sc, address = s.accept()

	print(address)
	fname = sc.recv(1024)
	f = open(fname,'wb')
	print(fname)

	sc, address = s.accept()
	print(address)
	
	while True:
		l = sc.recv(1024)
		while (l):
			f.write(l)
			l = sc.recv(1024)
	f.close()
	sc.close()
s.close()
