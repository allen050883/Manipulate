# k3s安裝方法  
三台主機名稱  
k3s_1  
k3s_2  
k3s_3  

在/etc/hosts增加連線  
```
sudo tee -a /etc/hosts<<EOF
1.2.3.4 master
1.2.3.5 worker1
1.2.3.6 worker2
EOF
```
  
# 安裝k3s
先在Master安裝
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
