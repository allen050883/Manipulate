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
ssh-copy-id user@host_ip               # send ssh-key to host pc
```
  
## blacklist nouveau
```bat
sudo apt-get remove nvidia* && sudo apt autoremove
sudo apt-get install dkms build-essential linux-headers-generic
sudo nano /etc/modprobe.d/blacklist.conf
```  
add this in the .conf file  
```bat
blacklist nouveau
blacklist lbm-nouveau
options nouveau modeset=0
alias nouveau off
alias lbm-nouveau off
```
```bat
echo options nouveau modeset=0 | sudo tee -a /etc/modprobe.d/nouveau-kms.conf
sudo update-initramfs -u
sudo reboot
```  
  
## Install nvtop  
Ubuntu 19.04  
```bat
sudo apt install nvtop
```
Ubuntu 18.04 and other  
```bat
sudo apt install cmake libncurses5-dev libncursesw5-dev git
git clone https://github.com/Syllo/nvtop.git
mkdir -p nvtop/build && cd nvtop/build
cmake ..

# If it errors with "Could NOT find NVML (missing: NVML_INCLUDE_DIRS)"
# try the following command instead, otherwise skip to the build with make.
cmake .. -DNVML_RETRIEVE_HEADER_ONLINE=True

make
make install # You may need sufficient permission for that (root)
```
