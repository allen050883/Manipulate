# something trivial

## GPU to P0  
sudo nvidia-smi -pl 320 -i 1  #make power to 320W (i is the index of GPU number)  
sudo nvidia-smi -pm 1 -i 1    #make GPU state ON  
sudo nvidia-smi -cc 1 -i 1    #make GPU to P0  
  
## convert jpg to gif in linux  
sudo apt-get install imagemagick  
convert -delay 20 -loop 0 *.jpg myimage.gif  
  
## add new HDD and move /home in there  
mkfs.ext4 /dev/sda  
sudo blkid --> find the UUID on the new HDD  
sudo nano /etc/fstab --> add in fstab  
sudo mkdir /media/home  
sudo mount -a  
sudo rsync -aXS /home/. /media/home/.  
cd /  
sudo mv /home /home_backup  
sudo mkdir /home  
sudo nano /etc/fstab --> change mount from /media/home to /home  
sudo mount -a  
sudo rm -rf /home_backup  
