# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:01:23 2021

@author: aliel
"""


import socket
IP = "127.0.0.1" 
PORT = 60243 
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
data = input("saisir un txt:")
sock.sendto(data.encode('utf-8'),(IP,PORT))


       