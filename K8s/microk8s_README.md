# microk8s 安裝環境  
  
Ubuntu 18.04 server板的virtual box安裝master跟node microk8s相關套件為1.21版  
  
```
sudo apt-get update && sudo apt-get upgrade -y
sudo snap install microk8s --classic --channels=1.21
```

## 問題
Q: microk8s status出現 "microk8s is not running. Use microk8s inspect for a deeper inspection."
A: 重新整個關掉vm (sudo poweroff), 再打開
