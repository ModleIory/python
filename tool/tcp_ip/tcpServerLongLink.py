import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
config = ("0.0.0.0",6002)
server.bind(config)
server.listen(5)
con,addr = server.accept()
while True:
    print("Client has link the server...")
    try:
        print(con.recv(1024))
        con.send(b"this is from tcp_server")
    except Exception as e:
        print("has stop")
        con.close()
        break

