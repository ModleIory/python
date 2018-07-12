import socket
import os
import threading

#得到socket
class get_server_socket():
    def __init__(self,ip,port):
        self.port = port
        self.ip = ip
    def get_socket(self):
        server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        config = (self.ip,self.port)
        server_socket.bind(config)
        server_socket.listen(10)
        print("Waiting for client connect...")
        return server_socket
#多线程监听客户端连接
class get_msg(threading.Thread):
    def __init__(self,socket,num):
        super(get_msg,self).__init__()
        self.socket = socket
        self.num = num
    def spy_client(self):
        print("Thread No.{} is running...".format(self.num))
        con,addr = self.socket.accept()
        print("Client has linkd：{} : {}".format(con,addr))
        while True:
            print("Waiting for client data...")
            recv = con.recv(1024) 
            con.send(b"This is reply from server port")
            print("Will show data from client : ")
            print(recv)
            print("Current thread number is {}".format(threading.activeCount()))
    def run(self):
        try:
            self.spy_client()
        except Exception as e:
            #If connection is lose,create a newer 
            print(str(e))
            print("*"*50)
            print("A thread is end , will start a new thread")
            self.spy_client()

serverSocketInstance = get_server_socket("0.0.0.0",6001)
serverSocket = serverSocketInstance.get_socket()
thread_num = 3
# for x in range(0,thread_num):
#     tmp = get_msg(serverSocket,x+1) 
#     tmp.start()
#     tmp.join()
one = get_msg(serverSocket,1)
two = get_msg(serverSocket,2)
one.start()
two.start()
one.join()
two.join()




'''    
def get_tcp_server_socket():
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    config = ("0.0.0.0",6001)
    server_socket.bind(config)
    server_socket.listen(5)
    print("Waiting for client connect...")
    return server_socket
def tcp_server_get_msg(server_socket):
    con,addr = server_socket.accept()
    print("Client has linkd：{} : {}".format(con,addr))
    while True:
        print("Waiting for client data...")
        recv = con.recv(1024) 
        con.send(b"This is reply from server port")
        print("Will show data from client : ")
        print(recv)

socket = get_tcp_server_socket()
one = threading.Thread(target=tcp_server_get_msg,args=(socket,))
two = threading.Thread(target=tcp_server_get_msg,args=(socket,))
one.start()
two.start()
'''