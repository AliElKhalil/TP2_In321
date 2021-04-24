# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:32:01 2021

@author: aliel
"""
from Recepteur import *
from Emetteur import *


ip_destination="127.0.0.1"
port_destination=62000

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
addest=(ip_destination, port_destination)

test1=True
test2=True

while (test1 and test2):
    test1,name=emetteur(addest, s)
    if (test1):
        addest, test2=recepteur(s,name)


print("Fin de la conversation")