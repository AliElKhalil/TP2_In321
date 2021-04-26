# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 14:56:51 2021

@author: aliel
"""

import socket

TCP_IP = '192.168.1.38'  # IP du serveur vers lequel on se connecte
TCP_PORT = 55000	 # port du serveur
BUFFER_SIZE = 1024          		# taille des lectures

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("connecting to : ", TCP_IP, TCP_PORT)
s.connect((TCP_IP, TCP_PORT))
MESSAGE = input("Saisir un texte : ").encode("utf-8")
print("sending data... ")
s.send(MESSAGE)
print("data sent.")

data = s.recv(BUFFER_SIZE)
print("received data:\n", data.decode('utf-8'))

s.close()

