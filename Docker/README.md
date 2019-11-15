# Docker

### Save docker image:  
docker save -o b5d632d87a03.tar b5d632d87a03  
### Load docker image:  
docker load -i python3-tensorflow-gpu.tar  
### Renew docker tag:(just type container ID former least 4 words)  
docker tag acbf allen/python3-tensorflow-gpu
### For someone using, create a file and load nvidia-docker(do not make the file in root state)  
1. mkdir ExtStorage  
2. sudo nvidia-docker run -it -v /media/allen/:/workspace markliou/python3-tensorflow-gpu bash  
(nvidia-docker run -it -v /media/allen:/workspace -v /media/dataset/ markliou/python3-tensorflow-gpu bash)  
(sudo docker run -it --gpus all --rm -e DISPLAY=$DISPLAY -v $HOME/.Xauthority:/root/.Xauthority -v /media/allen:/workspace --network=host --name=VAETEST  markliou/python3-tensorflow-gpu bash)  
  
 ---  
### Search which container running  
docker ps  
### All dockers including open, close and dead  
docker ps -a  
  
  
  
---  
# Screen
## In terminal, type 'screen' to open. It is useful when leaving the ssh mode.  
## command line:  
1. enter screen (Deatched mode): screen -r PID  
2. enter screen (Attached mode): screen -D -r PID  
3. watch existing screen: screen -ls  
4. delete screen: kill PID  
  
# command line in screen  
5. deatched screen: ctrl + A ^ D (press 'ctrl' and 'A' in the same time, and then press 'D')  
6. see previous content: ( ctrl + A ^ [ ) then ( ctrl + B )(back) or ( ctrl + F )(forward)  


