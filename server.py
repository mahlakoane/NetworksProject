import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 9999

#Establish server interface at port 9999 of this machine 
sock.bind((host, port))

print('waiting for UDP messages...')

while True:

 result = sock.recvfrom(1024)   #Buffer size.
 clientMsg=result[0]
 clientAddress=result[1]
 decodedMsg = clientMsg.decode("utf-8")
 decodedMsgUpper = decodedMsg.upper() 
       
 if decodedMsgUpper=="EXIT":

        sock.sendto(decodedMsgUpper.encode("utf-8"),clientAddress)
        break

 else:
        print(decodedMsg)
 continue       

sock.close()