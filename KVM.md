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
eno1 config:
```
TYPE=Ethernet
NAME=bridge-slave-eno1
UUID=f43a8688-81f0-4860-91d4-f8f41efe2d10
DEVICE=eno1
ONBOOT=yes
BRIDGE=br0
```
Restart the networking service (warning ssh command will disconnect, it is better to reboot the Linux box):
```
systemctl restart NetworkManager.service
## OR ##
nmcli con up br0
nmcli connection delete eno1
```
Verify it with the nmcli command
```
nmcli device
```
Sample Output:
```
DEVICE      TYPE      STATE      CONNECTION        
br0         bridge    connected  br0               
virbr0      bridge    connected  virbr0            
eno1        ethernet  connected  bridge-slave-eno1 
lo          loopback  unmanaged  --                
virbr0-nic  tun       unmanaged  --                
wlp1s0      wifi      unmanaged  --  
```
  
#### Step 5: Create your first virtual machine/guest VM  
```
cd /var/lib/libvirt/boot/
wget https://mirrors.edge.kernel.org/centos/8/isos/x86_64/CentOS-8.1.1911-x86_64-boot.iso
wget https://mirrors.edge.kernel.org/centos/8/isos/x86_64/CHECKSUM
sha256sum --ignore-missing -c CHECKSUM
```
Create CentOS 8.x VM  
In this following example, I creating CentOS 8.x VM with 1GB RAM, 1 CPU core, 1 nics and 20GB hard disk space, enter:
```
virt-install \
--virt-type=kvm \
--name centos8-vm \
--memory 1024 \
--vcpus=1 \
--os-variant=rhel8.1 \
--cdrom=/var/lib/libvirt/boot/CentOS-8.1.1911-x86_64-boot.iso \
--network=bridge=br0,model=virtio \
--graphics vnc \
--disk path=/var/lib/libvirt/images/centos8.qcow2,size=20,bus=virtio,format=qcow2
```
Reference:  https://www.cyberciti.biz/faq/how-to-install-kvm-on-centos-8-headless-server/  
