import socket
import time

count = 0
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
config = ("192.168.101.67",6002)
client.connect(config)
while count < 5:
    client.send(b"this is from client")
    print(client.recv(1024))
    count+=1
    time.sleep(1)
        
        

