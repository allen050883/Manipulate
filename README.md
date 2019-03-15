# Docker

### Save docker image:  
docker save -o b5d632d87a03.tar b5d632d87a03  
### Laod docker image:  
docker load -i python3-tensorflow-gpu.tar  
### Renew docker tag:(just type container ID former least 4 words)  
docker tag acbf allen/python3-tensorflow-gpu
### For someone using, create a file and load nvidia-docker(do not make the file in root state)  
1. mkdir ExtStorage  
2. nvidia-docker run -it -v /home/allen/ExtStorage:/workspace markliou/python3-tensorflow-gpu bash  
 ---  
### Search which container running  
docker ps  
### All dockers inculding open, close and dead  
docker ps -a  


