# k3s安裝方法  
三台主機名稱  
k3s_1  
k3s_2  
k3s_3  

在/etc/hosts增加連線  
```
sudo tee -a /etc/hosts<<EOF
1.2.3.4 k3s_1
1.2.3.5 k3s_2
1.2.3.6 k3s_3
EOF
```
  
# 安裝k3s
先在Master安裝
```
curl -sfL https://get.k3s.io | sh -
```

