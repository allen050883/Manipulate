import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 54321))

word = "Hello I'm Client."
word_encode = word.encode()
sock.send(word_encode)
msg = sock.recv(1024)
msg_decode = msg.decode()
print("Server send: " + msg_decode)
sock.close()