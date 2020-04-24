Setting Juniper_EX2200-24P-4G POE switch  
  
1. Need RJ45(Internet) to RS232(USB) from console port to laptop, but RJ45 to RJ45 can not use  
2. switch to the ethernet and open putty 'Serial'(find to COM number in device management  
3. then, we can use the terminal  
  
```
login: root
password:
root# cli  
root# configure  
root# exit
```
Then, Start to set.  
```
root# set system host-name EX2200-24P-4G
root# set interfaces vlan.0 family inet address 172.17.99.33/24
root# set vlans default l3-interface vlan.0
root# set system services web-management http
root# set system services web-management https system-generated-certificate
root# set system services telnet
root# set system services ssh root-login allow
root# set system root-authentication plain-text-password
root# commit
```  
  
factory reset, but it can not clear completely
```
root# rm -rf /config/juniper.conf.*.gz
root# rm -rf /config/db/config/juniper.conf.*.gz
root# reboot

root# load factory-default
root# set system root-authentication plain-text-password
root# commit
```
