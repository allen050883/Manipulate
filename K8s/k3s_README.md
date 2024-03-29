# k3s安裝方法  
三台主機名稱  
master  
worker1  
worker2  
worker3  
  
在/etc/hosts增加連線  
```
sudo tee -a /etc/hosts<<EOF
1.2.3.4 master
1.2.3.5 worker1
1.2.3.6 worker2
1.2.3.7 worker3
EOF
```
  
# 安裝k3s
## 在Master安裝
```
curl -sfL https://get.k3s.io | sh -
```
完成結果如下  
```
[INFO]  Finding release for channel stable
[INFO]  Using v1.21.4+k3s1 as release
[INFO]  Downloading hash https://github.com/k3s-io/k3s/releases/download/v1.21.4+k3s1/sha256sum-amd64.txt
[INFO]  Downloading binary https://github.com/k3s-io/k3s/releases/download/v1.21.4+k3s1/k3s
[INFO]  Verifying binary download
[INFO]  Installing k3s to /usr/local/bin/k3s
[INFO]  Creating /usr/local/bin/kubectl symlink to k3s
[INFO]  Creating /usr/local/bin/crictl symlink to k3s
[INFO]  Creating /usr/local/bin/ctr symlink to k3s
[INFO]  Creating killall script /usr/local/bin/k3s-killall.sh
[INFO]  Creating uninstall script /usr/local/bin/k3s-uninstall.sh
[INFO]  env: Creating environment file /etc/systemd/system/k3s.service.env
[INFO]  systemd: Creating service file /etc/systemd/system/k3s.service
[INFO]  systemd: Enabling k3s unit
Created symlink /etc/systemd/system/multi-user.target.wants/k3s.service → /etc/systemd/system/k3s.service.
[INFO]  systemd: Starting k3s
```
  
檢查狀態  
```
systemctl status k3s
```
狀態結果
```
● k3s.service - Lightweight Kubernetes
   Loaded: loaded (/etc/systemd/system/k3s.service; enabled; vendor preset: enabled)
   Active: active (running) since Fri 2021-09-03 07:15:59 UTC; 6min ago
     Docs: https://k3s.io
  Process: 1656 ExecStartPre=/sbin/modprobe overlay (code=exited, status=0/SUCCESS)
  Process: 1655 ExecStartPre=/sbin/modprobe br_netfilter (code=exited, status=0/SUCCESS)
  Process: 1643 ExecStartPre=/bin/sh -xc ! /usr/bin/systemctl is-enabled --quiet nm-cloud-setup.service (code=exited, status=0/SUCCESS)
 Main PID: 1657 (k3s-server)
    Tasks: 85
```
  
k3s.yaml設定值可在這邊看到
```
sudo cat /etc/rancher/k3s/k3s.yaml
```
```
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: XXXXX
    server: https://127.0.0.1:6443
  name: default
contexts:
- context:
    cluster: default
    user: default
  name: default
current-context: default
kind: Config
preferences: {}
users:
- name: default
  user:
    client-certificate-data: XXXXX
    client-key-data: XXXXX
```
  
## 在Worker安裝  
先在master中找到建好的token
```
sudo cat /var/lib/rancher/k3s/server/node-token
```
```
K105dXXXXX::server:e0fc8XXXXX
```
在每一台worker準備安裝前，先將master的IP跟token輸入成參數
```
k3s_url="https://1.2.3.4:6443"
k3s_token="K105dXXXXX::server:e0fc8XXXXX"
```
開始安裝  
```
curl -sfL https://get.k3s.io | K3S_URL=${k3s_url} K3S_TOKEN=${k3s_token} sh -
```
```
[INFO]  Finding release for channel stable
[INFO]  Using v1.21.4+k3s1 as release
[INFO]  Downloading hash https://github.com/k3s-io/k3s/releases/download/v1.21.4+k3s1/sha256sum-amd64.txt
[INFO]  Downloading binary https://github.com/k3s-io/k3s/releases/download/v1.21.4+k3s1/k3s
[INFO]  Verifying binary download
[INFO]  Installing k3s to /usr/local/bin/k3s
[INFO]  Creating /usr/local/bin/kubectl symlink to k3s
[INFO]  Creating /usr/local/bin/crictl symlink to k3s
[INFO]  Creating /usr/local/bin/ctr symlink to k3s
[INFO]  Creating killall script /usr/local/bin/k3s-killall.sh
[INFO]  Creating uninstall script /usr/local/bin/k3s-agent-uninstall.sh
[INFO]  env: Creating environment file /etc/systemd/system/k3s-agent.service.env
[INFO]  systemd: Creating service file /etc/systemd/system/k3s-agent.service
[INFO]  systemd: Enabling k3s-agent unit
Created symlink /etc/systemd/system/multi-user.target.wants/k3s-agent.service → /etc/systemd/system/k3s-agent.service.
[INFO]  systemd: Starting k3s-agent
```
到此為止，連clustering都已經建置完成  
接下來在master檢查nodes  
```
sudo kubectl get nodes
```
結果如下
```
NAME      STATUS   ROLES                  AGE     VERSION
worker3   Ready    <none>                 7m50s   v1.21.4+k3s1
master    Ready    control-plane,master   40m     v1.21.4+k3s1
worker2   Ready    <none>                 7m25s   v1.21.4+k3s1
worker1   Ready    <none>                 11m     v1.21.4+k3s1
```
