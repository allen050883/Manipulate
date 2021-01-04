# 用LX1430-M1為例子  
符合的Centos版本如下  
https://jp.fujitsu.com/platform/server/primergy/software/linux/products/distribution/pdf/lx1430m1-non-support-os.pdf#page=2  
Centos 8 用server的x86_64安裝  
  
# 安裝KVM在Centos 8  
#### Step 1: Installing kvm  
```
dnf module install virt
dnf install virt-install virt-viewer libguestfs-tools

systemctl enable libvirtd.service
systemctl start libvirtd.service
systemctl status libvirtd.service
```
  
#### Step 2: Verify your kvm installation  
```
lsmod | grep -i kvm
```
  
#### Step 3: Configure bridged networking  
By default, dnsmsq based network bridge configured by libvirtd called virbr0. You can verify that with the following simple commands:
```
virsh net-info default
nmcli device
nmcli connection show
```
The libvirtd uses a lightweight DHCP and caching DNS server named dnsmasq. We can see config file including IP ranges either using the cat command or grep command/egrep command:
```
cat /var/lib/libvirt/dnsmasq/default.conf
egrep '^(dhcp-range|interface)' /var/lib/libvirt/dnsmasq/default.conf
## use the ip command to verify info about the virbr0 ##
ip a show virbr0
ip r
```
  
#### Step 4: Configure bridged networking  
If you want your VMs available to other servers on your LAN, set up a network bridge on the server that connected to your LAN. Update your nic config files. Here is my pre-configured br0 interface enslaved with eno1 Ethernet:
```
vi /etc/sysconfig/network-scripts/ifcfg-br0
```
br0 config  
```
## my lan 192.168.2.0/24 ##
## Bridge br0 config, only IPv4 and no IPv6 here for now ##
STP=no
TYPE=Bridge
PROXY_METHOD=none
BROWSER_ONLY=no
BOOTPROTO=none
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=no
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
IPV6_ADDR_GEN_MODE=stable-privacy
NAME=br0
UUID=dd51480e-fbac-41a8-b5e6-ea3d097f5059
DEVICE=br0
ONBOOT=yes
IPADDR=192.168.2.19
PREFIX=24
GATEWAY=192.168.2.254
DNS1=192.168.2.254
DOMAIN=sweet.home
IPV6_DISABLED=yes
```
And config for eno1 Ethernet:
```
vi /etc/sysconfig/network-scripts/ifcfg-bridge-slave-eno1
```
Reference:  https://www.cyberciti.biz/faq/how-to-install-kvm-on-centos-8-headless-server/  
