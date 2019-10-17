# Manipulate-Docker-git
Docker and git methods

# GPU to P0  
sudo nvidia-smi -pl 320 -i 1  #make power to 320W (i is the index of GPU number)  
sudo nvidia-smi -pm 1 -i 1    #make GPU state ON  
sudo nvidia-smi -cc 1 -i 1    #make GPU to P0  
  
# convert jpg to gif in linux
sudo apt-get install imagemagick
convert -delay 20 -loop 0 *.jpg myimage.gif
