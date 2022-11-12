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
mkfs.ext4 /dev/sda (the new HDD)
  
# see the UUID on the new HDD  
sudo blkid                              
sudo nano /etc/fstab # add /dev/sda in fstab to mount /media/home (/dev/sda /media/home defaults 0 0)  
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
### Ubuntu  
```bat
mkdir -p ~/.ssh  
chmod 700 ~/.ssh  
ssh-keygen                             # generate public key and private key
ssh-copy-id user@host_ip               # send ssh-key to host pc
```
### Windows Powershell  
First run, 
```
function ssh-copy-id([string]$userAtMachine){   
    $publicKey = "$ENV:USERPROFILE" + "/.ssh/id_rsa.pub"
    if (!(Test-Path "$publicKey")){
        Write-Error "ERROR: failed to open ID file '$publicKey': No such file"            
    }
    else {
        & cat "$publicKey" | ssh $userAtMachine "umask 077; test -d .ssh || mkdir .ssh ; cat >> .ssh/authorized_keys || exit 1"      
    }
}
```
then, 
```
ssh-copy-id user@host_ip
```
  
## xshell public key login  
1. generate new public key rsa 2048  
2. copy this key to the remote host ./ssh/authorized_keys  
3. setting the public key login in xshell  

## Winscp public key login  
1. take remote public key to transfer into .ppk used in Windows by PuTTygen  
2. setting the public key login in WinScp advance  
  
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
  
## Install chewing in Ubuntu 18.04
1. sudo apt install ibus-chewing  
2. log out or restart  
3. Region & Language + More + Other and choose "Chinese(chewing)"  
4. log out or restart   
    
  
## docker without root  
```
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker 
docker run hello-world #test
```
  
  
## microk8s without root  
```
sudo usermod -a -G microk8s $USER
sudo chown -f -R $USER ~/.kube
newgrp microk8s
```

## Install forticlient  
```
wget -O - https://repo.fortinet.com/repo/6.4/ubuntu/DEB-GPG-KEY | sudo apt-key add -

echo"deb [arch=amd64] https://repo.fortinet.com/repo/6.4/ubuntu/ /bionic multiverse" | sudo tee /etc/apt/sources.list.d/docker.list

sudo apt-get update

sudo apt install forticlient
```
  
## Close laptop screen but not suspend
```
sudo nano /etc/systemd/logind.conf

# Find this, and change
HandleLidSwitch=ignore
  
# logout and login again  
sudo systemctl restart systemd-logind 
```
  
# tmux new name  
```
tmux new -s python
```
