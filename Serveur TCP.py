# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 14:55:44 2021

@author: aliel
"""

import socket

TCP_IP = '127.0.0.1'
TCP_PORT1 = 55000     
TCP_PORT2=55001            
BUFFER_SIZE = 1024               

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


print("binding to "+ TCP_IP +":"+str(TCP_PORT1)," ...")
s1.bind((TCP_IP, TCP_PORT1))  # Demande à l’OS d’associer la socket à une ip/port
s2.bind((TCP_IP, TCP_PORT2))

s1.listen(1)   # transforme la socket en socket de connexion
s2.listen(1)
print(" Waiting client… ")
scom1, caddr1 = s1.accept()
scom2, caddr2 = s2.accept()
print("client connected with address : \n", caddr1)
print("\n", caddr2)
print("listening...")
data1 = scom1.recv(BUFFER_SIZE)
data2 = scom2.recv(BUFFER_SIZE)
print("received data from first client : ", data1.decode('utf-8'))
print("received data from second client : ", data2.decode('utf-8'))
scom1.send("Message reçu".encode('utf-8'))  #confirmation message reçu
scom2.send("Message reçu".encode('utf-8'))


scom1.close()
s1.close()
scom2.close()
s2.close()