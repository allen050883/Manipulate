# php socket
```php
<?php
//php server
$host = "127.0.0.1";
$port = 25003;
set_time_limit(0);
$socket = socket_create(AF_INET, SOCK_STREAM, 0) or die("Could not create socket\n");
$result = socket_bind($socket, $host, $port) or die("Could not bind to socket\n");
$result = socket_listen($socket, 3) or die("Could not set up socket listener\n");
$spawn = socket_accept($socket) or die("Could not accept incoming connection\n");
$input = socket_read($spawn, 1024) or die("Could not read input\n");
$input = trim($input);
echo "Client Message: ".$input;
$output = $input;
socket_write($spawn, $output, strlen ($output)) or die("Could not write output\n");
socket_close($spawn);
socket_close($socket);
?>
```

```php
<?php
//php client 
$host    = "127.0.0.1";
$port    = 25003;
$message = "Hello Server";
echo "Message To server:".$message ."\n";
$socket = socket_create(AF_INET, SOCK_STREAM, 0) or die("Could not create socket\n");
$result = socket_connect($socket, $host, $port) or die("Could not connect to server\n");  
socket_write($socket, $message, strlen($message)) or die("Could not send data to server\n");
$result = socket_read ($socket, 1024) or die("Could not read server response\n");
echo "Reply From Server :".$result;
socket_close($socket);
?>
```
reference: https://stackoverflow.com/questions/22401079/how-to-test-php-socket-programming-in-localhost-ubuntu/22401126  
  
# python scoket  
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
