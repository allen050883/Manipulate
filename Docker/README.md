# Docker

### Save docker image:  
docker save -o b5d632d87a03.tar b5d632d87a03  
### Load docker image:  
docker load -i python3-tensorflow-gpu.tar  
### Renew docker tag:(just type container ID former least 4 words)  
docker tag acbf allen/python3-tensorflow-gpu


##### nvidia-docker
```
sudo nvidia-docker run --rm -it -v /media/allen/:/workspace markliou/python3-tensorflow-gpu bash  
```
volumes can choose multiple
```
sudo nvidia-docker run -it -v /media/allen:/workspace -v /media/dataset/ markliou/python3-tensorflow-gpu bash  
```
##### docker (gpus device)
```
sudo docker run -it --gpus all --rm -e DISPLAY=$DISPLAY -v $HOME/.Xauthority:/root/.Xauthority -v /home/allen:/workspace --network=host --name=test  allentseng/python3-tensorflow-gpu bash  
```
  
### Condtion: Use public image and run the container. Finish container, and try to make it in image and try sace in tar file.  
```
$ docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                NAMES
df2caf9283e8        nginx               "nginx -g 'daemon of…"   35 seconds ago      Up 34 seconds       0.0.0.0:80->80/tcp   vigorous_jang
```
Export the container in tar file  
```
$ docker export df2c > nginx.tar
```
Make container tar file import image  
```
$ docker import - mynginx < nginx.tar
sha256:aaaed50d250a671042e8dc383c6e05012e245f5eaf555d10c40be63f6028ee7b
```
```
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
mynginx             latest              aaaed50d250a        25 seconds ago      107MB
nginx               latest              568c4670fa80        2 weeks ago         109MB
```
Save new image and remove container tar file  
```
$ docker save -o mynginx.tar mynginx
$ rm nginx.tar
```
Load image  
```
$ docker load < mynginx1.tar
```

### container 
```
sudo docker ps
sudo docker ps -a #no running  
sudo docker rm xxxx #remove container  
```  
### image  
```
sudo docker images  
sudo docker rmi xxxx #remove image  
```  
### execute container  
```
sudo docker exec -it [container_name] /bin/bash  
``  
 
 
  

---  
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


