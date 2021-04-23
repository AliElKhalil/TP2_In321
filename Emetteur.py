# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:01:23 2021

@author: aliel
"""


import socket

def emetteur(addr, s):
    IP = addr[0]
    PORT = addr[1]
    data = input("saisir un txt:")
    if (data!="quit"):
        s.sendto(data.encode('utf-8'),(IP,PORT))
    return (data!="quit")


       