import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 9999 



while True:

 info = input("Enter message you wish to send to server : ")

 #stream vs byte-stream in python 3

 converter=info.encode("utf-8")

 sock.sendto(converter,(host,port))   #access the server through this interface
 
 #if ever this is the case, terminate.
 if info=="EXIT":   
     break
  

sock.close()





