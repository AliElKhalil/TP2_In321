# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:09:16 2021

@author: aliel
"""

import socket

def recepteur(s):
    data,addr=s.recvfrom(1024)
    print("sender : ", addr)
    print("data : ", data.decode('utf-8'))
    return (addr, data!="quit")