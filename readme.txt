# Lavanya Somashekar
# UTA ID: 1001104262
--------------------------------------
Contents of this file:
--------------------------------------
1. Introduction
2. Language used
3. Requirements
4. Instructions on how to run the code
5. Screenshots
6. Results
7. References

--------------------------------------
1. Introduction
--------------------------------------
I have developed a multithreaded Web Server which interacts with a Web Client(Google Chrome). The Web Client downloads the content of any file and displays it. It also displays the connection parameters of the server and displays appropriate error messages.

--------------------------------------
2. Language used
--------------------------------------
I have used Python programming to implement this project. There are two python scripts Server.py and Client.py which performs the respective functions. There is a sample text file test.txt for testing the results.

--------------------------------------
3. Requirements
--------------------------------------
The following need to be installed in order to run the program:
-> Windows 7/8 OS
-> Python 2.7
-> Google Chrome Version 46.0.2490.80 m

--------------------------------------
4. Instructions on how to run the code
--------------------------------------
-> Open a command prompt and run the server using the command "python Server.py"
-> Start Google Chrome and type http://localhost:8080/test.txt in the address bar
   All the relevant Server details and contents of the file test.txt will be displayed!
-> Also open another command prompt and run the command "python Client.py 127.0.0.1 8080 test.txt"
   All the relevant Server details and contents of the file test.txt will be displayed!

--------------------------------------
5. Screenshots
--------------------------------------
I have included 4 screenshots in the zip file for the outputs that I got when I used browser and command prompt, each as a client.
Image1 - File contents and appropriate information displayed on the browser
Image2 - 404 error File not found
Image3 - File contents and appropriate information displayed on the command prompt
Image4 - 404 error File not found

--------------------------------------
6. Results
--------------------------------------
-> We get the expected output when we run the Client. The Server connection parameters will be printed on the Client and vice versa.
-> Observer the screenshots carefully.

--------------------------------------
7. References 
--------------------------------------
-> http://www.binarytides.com/python-socket-programming-tutorial/
-> http://stackoverflow.com/questions/29110620/how-to-download-file-from-local-server-in-python
-> https://docs.python.org/2/howto/sockets.html#socket-howto
-> http://www.binarytides.com/receive-full-data-with-the-recv-socket-function-in-python/
-> http://www.tutorialspoint.com/python/python_command_line_arguments.htm
-> https://docs.python.org/2/library/socket.html