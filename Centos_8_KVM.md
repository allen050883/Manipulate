# 用LX1430-M1為例子  
符合的Centos版本如下  
https://jp.fujitsu.com/platform/server/primergy/software/linux/products/distribution/pdf/lx1430m1-non-support-os.pdf#page=2  
Centos 8 用server的x86_64安裝  
  
# 安裝KVM在Centos 8  
```
#Step 1: Installing kvm
dnf module install virt
dnf install virt-install virt-viewer libguestfs-tools

systemctl enable libvirtd.service
systemctl start libvirtd.service
systemctl status libvirtd.service

Step 2: Verify your kvm installation


```
Reference:  https://www.cyberciti.biz/faq/how-to-install-kvm-on-centos-8-headless-server/  
