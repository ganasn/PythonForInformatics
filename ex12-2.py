#Chapter 12 - Sockets - Retrieve data with HTTP GET 

import socket

sock_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock_conn.connect(('www.py4inf.com',80))
#sock_conn.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.1\n\n')

sock_conn.connect(('www.github.com',80))
sock_conn.send('GET https://github.com/ganasn/PythonForInformatics/blob/master/README.txt HTTP/1.1 \n\n')

while True:
    data = sock_conn.recv(512)
    if len(data) < 1:
        break
    print data
    
sock_conn.close()
