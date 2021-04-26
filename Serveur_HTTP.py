# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 14:55:44 2021

@author: aliel
"""

import socket
import time

import base64
with open("C:\\Users\\aliel\\OneDrive\\Documents\\GitHub\\TP2_In321\\doubt.gif","rb") as i:     
    encoded_string = base64.b64encode(i.read()).decode( 'utf-8' )
    

http_head = "HTTP/1.1 200 OK\r\n"
http_head += "Date:"+ time.asctime() +"GMT\r\n"
http_head += "Expires: -1\r\n"
http_head += "Cache-Control: private, max-age=0\r\n"
http_head += "Content-Type: text/html;"
http_head += "charset=utf-8\r\n"
http_head += "\r\n"
data = "<html><head><meta charset='utf-8'/></head>"
data += "<body><h1>In321 is the best course ! </h1>"
data += "\r\n"
#data += f'<img src="data:image/png;base64, {encoded_string}"alt="No doubt gif">' 
data += "</body></html>\r\n"
data += "\r\n"
http_response = http_head.encode("ascii") + data.encode("utf-8")

TCP_IP = '192.168.1.38'
TCP_PORT = 55000                 
BUFFER_SIZE = 1024               

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((TCP_IP, TCP_PORT))  # Demande à l’OS d’associer la socket à une ip/port


s.listen(1)   # transforme la socket en socket de connexion
print(" Waiting client… ")
scom, caddr = s.accept()
print("client connected with address : ", caddr)
data = scom.recv(BUFFER_SIZE)
print("received data:", data.decode('utf-8'))
scom.send(http_response)  

s.close()
scom.close()


 

