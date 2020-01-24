```python
#create socket server
import socket

host = ''
port = 12345

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
#AF_INET: 跟外面網路, 也就是IPv4, TCP, UDP要用這種 (AF_INET6 for IPv6)
#AF_UNIX: 本地機器自己內部的溝通, 不對外

#SOCK_STREAM: 會確保資料正確的流到對方, 像是資料串流的用法, 此法是用TCP
#SOCK_DGRAM: 無確保, 像是廣播訊息的用法, 此法是用UDP

sock.bind((host, port))
sock.listen(5)
#設定最多可以讓5個連線數



```

