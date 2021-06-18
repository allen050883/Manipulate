# 安裝環境  
Ubuntu 18.04桌面板的virtual box安裝master跟node
k8s相關套件為1.21版  
備：以下命令無法執行時, 請改用root為使用者
  
## Kubelet / Kubeadm 安裝與概念  
先說明kubelet, kubeadm, kubectl  
  
1. kubelet 是基於 pod 來做執行 https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/  
2. kubeadm 用於部署及監控, ex.kubeadm init & join https://kubernetes.io/docs/reference/setup-tools/kubeadm/  
3. kubectl 管理 k8s cluster https://kubernetes.io/docs/reference/kubectl/overview/  
  
## 於欲執行 Kubernetes 的機上，必須要有 kubelet / kubeadm ( Master 與 node 皆要執行此步驟 )
Kubernetes 的主要程式是透過 runtime 來實現 pods (runtime 可以是 Docker / CRI-O / Container)  
  
a. 先設定 k8s server上網路  
```
cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF

sudo sysctl --system
```
b. 安裝 kubeadm / kubelet  
```
sudo apt-get update && sudo apt-get install -y apt-transport-https curl
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
cat <<EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
deb https://apt.kubernetes.io/ kubernetes-xenial main
EOF

sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl
```
c. 驗證  
只要輸入 kubeadm 就可以知道是否安裝成功 (如下畫面)  
![alt text](https://github.com/allen050883/Manipulate/blob/master/K8s/read_img/kubeadm_finish.png)
  
  
  
   
  
## 安裝 CRI-O for K8s  
CRI-O 是設計給 k8s 的 Container Runtime Interface，k8s 當然也可以使用 Docker 作為 Container Runtime，但是我們這邊遵循選擇 CRI-O 為主  
(CRI-O github 於此 : https://github.com/cri-o/cri-o)  
  
這邊皆以root執行  
a. 先設定 Linux kernel 模組  
```
modprobe overlay
modprobe br_netfilter
```
b. 設定網路給 CRI-O  
```
cat > /etc/sysctl.d/99-kubernetes-cri.conf <<EOF
net.bridge.bridge-nf-call-iptables  = 1
net.ipv4.ip_forward                 = 1
net.bridge.bridge-nf-call-ip6tables = 1
EOF

sysctl --system
```
c. 安裝 CRI-O (請注意這邊的 VERSION 與 OS，如果你選擇非本教學的版本請自行修改
詳細參數可以在官網看到)  
```
export VERSION=1.21
export OS=xUbuntu_18.04

echo "deb https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/$OS/ /" > /etc/apt/sources.list.d/devel:kubic:libcontainers:stable.list

echo "deb http://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable:/cri-o:/$VERSION/$OS/ /" > /etc/apt/sources.list.d/devel:kubic:libcontainers:stable:cri-o:$VERSION.list

curl -L https://download.opensuse.org/repositories/devel:kubic:libcontainers:stable:cri-o:$VERSION/$OS/Release.key | apt-key add -

curl -L https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/$OS/Release.key | apt-key add -

apt-get update
apt-get install -y cri-o cri-o-runc
```
d. 啟動 CRI-O  
```
systemctl daemon-reload
systemctl start crio
```
e. 關閉 swap  
k8s 預設不希望我們系統有 swap 存在，所以
編輯 /etc/fstab ( 執行 sudo nano /etc/fstab )，將 swap 註解掉
```
# /swap.img     none    swap    sw      0       0
```
然後執行 Ubuntu 關閉 Swap 指令  
```
sudo swapoff -a
```

```

```
