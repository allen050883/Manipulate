# 安裝環境：  
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
