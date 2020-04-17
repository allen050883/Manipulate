# Docker

### Save docker image:  
docker save -o b5d632d87a03.tar b5d632d87a03  
### Load docker image:  
docker load -i python3-tensorflow-gpu.tar  
### Renew docker tag:(just type container ID former least 4 words)  
docker tag acbf allen/python3-tensorflow-gpu
### For someone using, create a file and load nvidia-docker(do not make the file in root state)  
1. mkdir ExtStorage  
2.   
##### nvidia-docker
```
sudo nvidia-docker run --rm -it -v /media/allen/:/workspace markliou/python3-tensorflow-gpu bash  
```
```
sudo nvidia-docker run -it -v /media/allen:/workspace -v /media/dataset/ markliou/python3-tensorflow-gpu bash  
```
##### docker (gpus device)
```
sudo docker run -it --gpus all --rm -e DISPLAY=$DISPLAY -v $HOME/.Xauthority:/root/.Xauthority -v /home/allen:/workspace --network=host --name=test  allentseng/python3-tensorflow-gpu bash  
```
```
sudo docker run -it --gpus device=1  --rm -e DISPLAY=$DISPLAY -v $HOME/.Xauthority:/root/.Xauthority -v /home/allen:/workspace --network=host --name=test allentseng/python3-tensorflow-gpu-2.0 bash
```  
  
### container state  
sudo docker ps -a  
sudo docker rm xxxx #remove container  
  
### image state  
sudo docker images  
sudo docker rmi xxxx #remove image  
  
### run the same docker  
docker exec -it [container_name] /bin/bash  
  
 
 
  

  
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


