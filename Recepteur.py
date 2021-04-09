# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:09:16 2021

@author: aliel
"""

import socket
IP = "127.0.0.1" # adresse locale
PORT = 54321 # port local
sock = socket.socket(socket.AF_INET, # Internet
socket.SOCK_DGRAM) # UDP
sock.bind((IP,PORT)) # association de la socket avec IP/PORT
data,addr=sock.recvfrom(1024) # attente d'un message et lecture de max 1024 octets
print("sender : ", addr)
print("data : ", data.decode('utf-8'))