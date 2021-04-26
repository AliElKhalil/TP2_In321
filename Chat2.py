# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:45:02 2021

@author: aliel
"""

from Recepteur import *
from Emetteur import *

port_local=62000
ip_locale="192.168.1.38"
addr=(ip_locale, port_local)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  
s.bind(addr) # association de la socket avec IP/PORT

test1=True
test2=True

while (test1 and test2):
    adenv, test1=recepteur(s)
    if (test1): 
        test2=emetteur(adenv, s) 


print("Fin de la conversation")