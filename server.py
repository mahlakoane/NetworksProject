import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #IPV4 and TCP
host = socket.gethostname()
port = 9999

#Establish server interface at port 9999 of this machine 
sock.bind((host, port))

sock.listen(2)

print('Waiting for client connection...')

#Accept client connection here

myclient, clientAddress = sock.accept()
print('connection established!')




while True:

 clientMsg = myclient.recv(1024)   #Buffer size.
 decodedMsg = clientMsg.decode("utf-8")
 decodedMsgUpper = decodedMsg.upper() 
       
 if decodedMsgUpper=="EXIT":

        myclient.sendall(decodedMsgUpper.encode("utf-8"))
        break

 else:
        print(decodedMsg)
 continue       

sock.close()