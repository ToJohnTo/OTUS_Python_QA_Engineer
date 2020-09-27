# Echo server program
import socket
import json


HOST = 'localhost'
PORT = 8889


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print('Connected by', addr)
    with conn:
        dictionary = {}
        data = conn.recv(1024)
        binary_mass = data.splitlines()
        str_massiv = [el.decode('utf-8') for el in binary_mass]
        query_name = str_massiv[0]
        str_massiv = str_massiv[1:-1]

        for el in str_massiv:
            dic = el.split(":", 1)
            k = dic[0]
            v = dic[1]
            dictionary[k] = v

        print(f"Query: ", {query_name})
        send_data = json.dumps(dictionary, indent=4)
        print(send_data)
        s = json.loads(send_data)
        conn.send(f"HTTP/1.1 200 OK\n Content-Length: 100\n Connection: close\n Content-Type: text/html\n\n {send_data}".
                  encode("utf-8"))
