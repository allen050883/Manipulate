# Setting Juniper_EX2200-24P-4G POE switch  
  
1. Need RJ45(Internet) to RS232(USB) from console port to laptop, but RJ45 to RJ45 can not use  
2. switch to the ethernet and open putty 'Serial'(find to COM number in device management)  
  
## Login, Configure and Exit  
```
login: root
password:
root# cli  
root# configure  
root# exit
```
  
# Setting Configure  
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
  
  
## Other setting  
```
root# run show configuration | display set
root# load set terminal (paste config here)
root# run show arp (show mac information)
```  
## Factory reset
```
root# request system zeroize
```
  
## Config file  
```
set poe interface all telemetries
set poe interface ge-0/0/2 maximum-power 20
set poe interface ge-0/0/3 maximum-power 20
set poe interface ge-0/0/4 maximum-power 20
set poe interface ge-0/0/5 maximum-power 20
set poe interface ge-0/0/6 maximum-power 20
set poe interface ge-0/0/7 maximum-power 20
set poe interface ge-0/0/8 maximum-power 20
set poe interface ge-0/0/9 maximum-power 20
set poe interface ge-0/0/10 maximum-power 20
set poe interface ge-0/0/11 maximum-power 20
set poe interface ge-0/0/12 maximum-power 20
set poe interface ge-0/0/13 maximum-power 20
set poe interface ge-0/0/14 maximum-power 20
set poe interface ge-0/0/15 maximum-power 20
set poe interface ge-0/0/16 maximum-power 20
set poe interface ge-0/0/17 maximum-power 20
set poe interface ge-0/0/18 maximum-power 20
set poe interface ge-0/0/19 maximum-power 20
set poe interface ge-0/0/20 maximum-power 20
set poe interface ge-0/0/21 maximum-power 20

set interfaces vlan unit 0 family inet address 10.10.10.1/24
set routing-options static route 0.0.0.0/0 next-hop 10.10.10.254

set system host-name Jeno-TEST
set vlans default l3-interface vlan.0
set system root-authentication plain-text-password


=============================================================================================



set poe interface ge-0/0/x priority low => 設定POE優先權
set poe interface ge-0/0/X priority high => 設定POE優先權

set interfaces vlan unit 0 family inet address 10.10.10.1/24 ＝>設定vlan 0 的IP

set system host-name Jeno-TEST ＝>設定hostname
set vlans default l3-interface vlan.0 ＝>開啟L3的功能

set routing-options static route 0.0.0.0/0 next-hop 10.10.10.254 =>設定預設砸道

set system services ssh root-login allow =>開啟ssh 可用root登入
set system services telnet =>開啟telnet
set system services web-management http =>開啟Http
set system services web-management https system-generated-certificate ＝>開啟Https

set system root-authentication plain-text-password  ＝>設定root 密碼

>request system zeroize  ＝>還原工廠預設值
```
  
# Other setting detail    
## power to set class or static mode  
https://www.juniper.net/documentation/software/topics/task/configuration/poe-cli.html  
If the PoE power budget for the switch is insufficient to provide maximum power to all the PoE ports, we recommend that you do not change the management mode from class to static. If you change the power management mode to static and do not change the other default settings, the PoE controller allocates maximum power to the PoE ports in the order of port number, which means PoE will be disabled on higher-numbered ports when the PoE power budget runs out.  
In class mode, on the other hand, the PoE controller does not allocate power to a port until a powered device is connected. The class of the connected device determines the amount of power allocated. Thus in class mode, any PoE port can be used to power a device and all the PoE ports on the switch can be used as long as the combined power demand does not exceed the PoE power budget.  
  
## Problem  
1. 'dhcp' incompitable with interface assigned with address  
ans: delete interfaces vlan.0 family inet dhcp  
  
