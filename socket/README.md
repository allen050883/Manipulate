```python
#create socket server
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET: 跟外面網路, 也就是IPv4, TCP, UDP要用這種 (AF_INET6 for IPv6)
#AF_UNIX: 本地機器自己內部的溝通, 不對外

#SOCK_STREAM: 會確保資料正確的流到對方, 像是資料串流的用法, 此法是用TCP
#SOCK_DGRAM: 無確保, 像是廣播訊息的用法, 此法是用UDP

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/374180/

sock.bind(('localhost', 54321)) #IP, port
sock.listen(5) #設定最多可以讓5個連線數


while True:
    (csock, adr) = sock.accept()
    print("Client Info: ", csock, adr)
    msg = csock.recv(1024) #能接收server端1024字元
    if not msg:
        pass
    else:
        msg_decode = msg.decode()
        print("Client send: " + msg_decode)
        
        #再丟個訊息回client端
        msg_recall = "Hello I'm Server."
        msg_encode = msg_recall.encode()
        csock.send(msg_encode)
    csock.close()
```
  
   
   
```python
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
```
