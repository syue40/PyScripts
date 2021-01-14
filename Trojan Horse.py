import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'  # Server IP
port = 1234

server.bind((host, port))
server.listen(5)

run = True
client, addr = server.accept()
print("Connection established with:", addr)

while run:
    try:
        data = input('>>>')
        client.send(data.encode('UTF-8'))  # send
        msg = client.recv(1024)
        print(msg.decode('UTF-8'))
    except ConnectionResetError:
        print('Client Lost. Connecting...')
        client, addr = server.accept()
        print('Client established with', addr)