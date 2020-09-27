import socket


HOST = "localhost"
PORT = 8889


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((HOST, PORT))
    query = b'GET / HTTP/1.1 200 OK\nContent-Length:100\nContent-Type:text/html\nHost:localhost:8889\n\b'
    s.send(query)
    data = s.recv(4096)
    print('Received', repr(data))
    print('End message')
