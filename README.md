# something trivial

## GPU to P0  
```bat
sudo nvidia-smi -pl 320 -i 1  #make power to 320W (i is the index of GPU number)  
sudo nvidia-smi -pm 1 -i 1    #make GPU state ON  
sudo nvidia-smi -cc 1 -i 1    #make GPU to P0  
```
  
## convert jpg to gif in linux  
```bat
sudo apt-get install imagemagick  
convert -delay 20 -loop 0 *.jpg myimage.gif  
```
  
## add new HDD and move /home in there  
```bat
mkfs.ext4 /dev/sda  
  
# see the UUID on the new HDD  
sudo blkid                              
sudo nano /etc/fstab # add in fstab  
sudo mkdir /media/home  
sudo mount -a  
sudo rsync -aXS /home/. /media/home/.  
cd /  
sudo mv /home /home_backup  
sudo mkdir /home  
  
# modify mounting from /media/home to /home  
sudo nano /etc/fstab                     
sudo mount -a  
sudo rm -rf /home_backup  
```  
  
## ssh auto login  
```bat
mkdir -p ~/.ssh  
chmod 700 ~/.ssh  
ssh-keygen                             # generate public key and private key
ssh-copy-id user@host_ip                  # send ssh-key to host pc
```
