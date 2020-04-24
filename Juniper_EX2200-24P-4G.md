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
  
root# request system configuration rescue delete
root# start shell user root
Password:
root# cd /config
root# rm -rf juniper.conf*
root# cd /config/db/config
root# rm -rf juniper.conf.*
root# reboot
```
  
power to set class or static mode    
https://www.juniper.net/documentation/software/topics/task/configuration/poe-cli.html  
If the PoE power budget for the switch is insufficient to provide maximum power to all the PoE ports, we recommend that you do not change the management mode from class to static. If you change the power management mode to static and do not change the other default settings, the PoE controller allocates maximum power to the PoE ports in the order of port number, which means PoE will be disabled on higher-numbered ports when the PoE power budget runs out.  
In class mode, on the other hand, the PoE controller does not allocate power to a port until a powered device is connected. The class of the connected device determines the amount of power allocated. Thus in class mode, any PoE port can be used to power a device and all the PoE ports on the switch can be used as long as the combined power demand does not exceed the PoE power budget.  
