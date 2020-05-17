import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #IPV4 and TCP
host = socket.gethostname()
port = 9999

#Request connection with server at this port. 
sock.connect((host, port))




info = input("Enter message you wish to send to server : ")

#stream vs byte-stream in python 3

converter=info.encode("utf-8")

sock.send(converter)   #access the server through this interface

sock.close()





