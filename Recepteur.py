# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:09:16 2021

@author: aliel
"""

import socket

def recepteur(s):
    name=socket.gethostname()
    data,addr=s.recvfrom(1024)
    txt=data.decode('utf-8')
    if (txt!="quit"):
        print("sender : ", name)
        print("data : ", txt)
    return (addr, txt!="quit")