# microk8s 安裝環境  
  
### 安裝
Ubuntu 18.04 server板的virtual box安裝master跟node microk8s相關套件為1.21版  
也可以安裝低一點的版本，建議不要低於1.19  
1.19板才開始支援HA
```
sudo apt-get update && sudo apt-get upgrade -y
sudo snap install microk8s --classic --channel=1.21
```
  
### Clustering  
```
microk8s add-node
```
```
Join node with:
microk8s join ip-172-31-20-243:25000/DDOkUupkmaBezNnMheTBqFYHLWINGDbf

If the node you are adding is not reachable through the default
interface you can use one of the following:

microk8s join 10.1.84.0:25000/DDOkUupkmaBezNnMheTBqFYHLWINGDbf
microk8s join 10.22.254.77:25000/DDOkUupkmaBezNnMheTBqFYHLWINGDbf
```
and use this command to master,  
```
microk8s join 10.1.84.0:25000/DDOkUupkmaBezNnMheTBqFYHLWINGDbf
```
then,  
```
microk8s kubectl get no
```
```
NAME               STATUS   ROLES    AGE   VERSION
10.22.254.79       Ready    <none>   27s   v1.15.3
ip-172-31-20-243   Ready    <none>   53s   v1.15.3
```


# Reference
https://microk8s.io/docs/clustering. 


## 問題
Q: microk8s status出現 "microk8s is not running. Use microk8s inspect for a deeper inspection."  
A: 重新整個關掉vm (sudo poweroff)，再打開有機會修好  
