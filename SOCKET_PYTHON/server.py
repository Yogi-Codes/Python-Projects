#!/usr/bin/python

import socket

from art import *

import subprocess


tprint("Dark  Shell",font="rnd-large")
tprint("Made By Darkist")

s =  socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(("127.0.0.1",8000))
print("Listening!!")
s.listen(1)

client,addr = s.accept()
print("connected")


while True:
	cmd = input("> ")
	client.send(cmd.encode())
	if cmd == 'exit':
		break
	if cmd == 'help':
		print(" Enter command")
		print(" exit ")
		continue
	output= (client.recv(1024).decode())
	print(output)



client.close()
s.close()	
