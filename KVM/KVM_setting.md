## Install Ubuntu 18.04 LVM  
  
## Let LV to be new disk
```
sudo lvcreate -l 100%FREE -n storage ubuntu-vg
sudo fdisk -l  #show the disk list
sudo mkfs.ext4 /dev/ubuntu-vg/storage  #format disk
#last  mount
```
## Update system
```
sudo apt-get update -y
sudo apt-get upgrade -y
```
  
## Install KVM need packages
```
sudo apt install -y qemu-kvm
sudo apt install -y bridge-utils
sudo apt install -y virtinst
sudo apt install -y qemu-utils
```
  
## Setting encryption on the grub
```
sudo grub-mkpasswd-pbkdf2
```
Enter the password and it will generate the encryption string  
Then, copy to the following document  
```
sudo vi /etc/grub.d/00_header
```
Add at end of file  
```
set superusers="User"
password_pbkdf2 User grub.pbkdf2.sha512.10000.XXX   #copy encryption string here
```

## Entering OS not need to enter password if no choose the grub
```
sudo vi /etc/grub.d/10_linux
```
Add '--unrestricted' in one line  
```
echo "menuentry '$(echo "$os" | grub_quote)' ${CLASS} --unrestricted \$menuentry_id_option 'gnulinux-simple-$boot_device_id' {" | sed "s/^/$submenu_indentation/"
```
```
sudo update-grub
```
