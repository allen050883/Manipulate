## ssh簡易說明:  
反向代理 ssh -fCNR  
正向代理 ssh -fCNL  
  
-f 後臺執行ssh指令  
-C 允許壓縮資料  
-N 不執行遠端指令  
-R 將遠端主機(伺服器)的某個埠轉發到本地端指定機器的指定埠  
-L 將本地機(客戶機)的某個埠轉發到遠端指定機器的指定埠  
-p 指定遠端主機的埠  
  
## 從內部port轉到外部port
新增：
```
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-ports 80
```
刪除：
```
sudo iptables -t nat -D PREROUTING -p tcp --dport 80 -j REDIRECT --to-ports 80
```
狀態檢查：
```
sudo iptables -t nat -L -n -v
```
