### Install VM
1. Use ubuntu 18.04 desktop to find "virtualbox" in "Ubuntu Softeware"  
2. Set ubuntu(64 bit) and load the vmdk  
  
##### Internet
1. Use "Bridged Adapter" to connect the localhost enthernet, and it will be given an IP.  
2. (Optional) The better is given the NAT network.  
3. test to turn on the Internet:
```
#check "ifconfig -a"
sudo ifconfig enp0s3 up
sudo dhclient enp0s3
```
4. set config in  /etc/netplan/01-netcfg.yaml
```
ethernets:
    enp3s0:
dhcp4: yes
```
#####   
