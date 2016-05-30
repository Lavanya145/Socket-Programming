""" 
 Lavanya Somashekar
 UTA ID: 1001104262
 http://www.binarytides.com/python-socket-programming-tutorial/
 http://stackoverflow.com/questions/29110620/how-to-download-file-from-local-server-in-python
 https://docs.python.org/2/howto/sockets.html#socket-howto
 http://www.binarytides.com/receive-full-data-with-the-recv-socket-function-in-python/
 http://www.tutorialspoint.com/python/python_command_line_arguments.htm
 https://docs.python.org/2/library/socket.html
 """

import socket
import sys
import time
import os
import signal
CLRF = '\r\n'

#Main function
def Main():
	host = '127.0.0.1'
	port = 8080
	host = sys.argv[1]
	port = int(sys.argv[2])
	filename = sys.argv[3]
	
	#create an INET, STREAMing socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host,port))	
	
	#for calculating Round Trip Time (RTT)
	start = time.time()
	
	if filename != 'q':
		pass
	request_headers = 'GET /%s HTTP/1.1' % (filename) + CLRF + 'Host: localhost:8080' + CLRF + 'Connection: keep-alive' + CLRF + 'Cache-Control: max-age=0' + CLRF + 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' + CLRF + 'Upgrade-Insecure-Requests: 1' + CLRF + 'User-Agent: script' + CLRF + 'Accept-Encoding: gzip, deflate, sdch' + CLRF + 'Accept-Language: en-US,en;q=0.8'
	s.send(request_headers)
	
	#receive contents of the file from the file server
	chunks = []
	bytes_recd = 0
	while bytes_recd < 4096:
		chunk = s.recv(min(4096-bytes_recd, 4096))
		if chunk == '':
			break
		chunks.append(chunk)
		bytes_recd += len(chunk)
	
	d = ''.join(chunks)
	print d
	print "Done!"
	s.close()
	done = time.time()
	elapsed = done - start
	print "RTT: ",elapsed
	
if __name__ == '__main__':
	Main()