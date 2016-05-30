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
import threading
import os
import sys
import signal
s = None
CLRF = '\r\n'
host = '127.0.0.1'
port = 8080

#defining the types on socket family and socket protocol
socket_family = ['socket.UNIX', 'socket.INET', 'socket.INET6']
socket_protocol = ['socket.SOCK_STREAM', 'socket.SOCK_DGRAM', 'socket.SOCK_RAW', 'socket.SOCK_RDM', 'socket.SOCK_SEQPACKET']

#function to retrieve requested file and send it to teh client through a socket
def RetrFile(name, sock):
	print "Name ", name
	request_data = sock.recv(1024)
	print "HTTP Headers for request"
	print request_data
	filename = file_path = ""
	try:
		#fetch the file contents by extracting file from the file directory provided by the HTTP header
		filename = request_data.split("\n")[0].split(" ")[1][1:]
		if filename is "":
			raise AttributeError
		current_dir = os.path.dirname(os.path.realpath("__file__"))
		file_path = os.path.join(current_dir, filename)
	
	#handling the exception when any other process interrupts
	except (IndexError, AttributeError) as e:
		print "Bad Request"
		sock.send("HTTP/1.1 400 Bad Request" + CLRF)
		sock.close()
		return
	if os.path.isfile(file_path):
		sock_name = sock.getsockname()
		peer_name = sock.getpeername()
		print "File %s exists" % (filename)
		
		#print the Server details on the Client side if the file exists
		sock.send("HTTP/1.1 200 OK" + CLRF*2)
		sock.send("Server Details:" + CLRF )
		sock.send("Host : %s" % sock_name[0] + CLRF)
		sock.send("Peer name: %s %s " % (peer_name[0], peer_name[1]) + CLRF)
		sock.send("Protocol: %s" % socket_protocol[sock.proto]  + CLRF)
		sock.send("Socket Family %s\n" % socket_family[sock.type] + CLRF)
		
		#print each line in the file o the Client side
		with open(file_path, 'r') as f:
			for line in f.read(2048):
				sock.send(line)
	else:
		#error message when file is not found
		print "File not found"
		sock.send("HTTP/1.1 404 Not Found" + CLRF)
	sock.close()

#Main function
def Main():
	global port
	try:
		#Initialize 1st argument as the port number
		if sys.argv[1]:
			port = int(sys.argv[1])
	except IndexError:
		pass
	global s
	
	#create an INET, streaming socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host,port))

	print 'Socket Created'
	
	#listen to any requests from the client
	s.listen(5)

	print "Server Started"
	while True:
		c, addr = s.accept()
		print "client connected ip:<" + str(addr) + ">"
		
		#create a thread to handle each request from the client
		t = threading.Thread(target=RetrFile, args=("retrThread", c))
		#print threading.current_thread()
		print t
		t.start()

	s.close()

#close the port when connection terminates
def gracefully_kill_script(signum, frame):
	global s
	print "killing program"
	#close the socket
	s.close()
	print "Closed all the sockets"
	sys.exit(1)


if __name__ == '__main__':
	#registering ctrl + z handler
	try:
		signal.signal(signal.SIGTSTP, gracefully_kill_script)
	except AttributeError:
		pass
	Main()