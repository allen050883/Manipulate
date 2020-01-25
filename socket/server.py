import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('localhost', 54321))
sock.listen(5)


while True:
    (csock, adr) = sock.accept()
    print("Client Info: ", csock, adr)
    msg = csock.recv(1024)
    if not msg:
        pass
    else:
        msg_decode = msg.decode()
        print("Client send: " + msg_decode)
        
        msg_recall = "Hello I'm Server."
        msg_encode = msg_recall.encode()
        csock.send(msg_encode)
    csock.close()