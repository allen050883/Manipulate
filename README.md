# Docker

## save docker image:  
docker save -o b5d632d87a03.tar b5d632d87a03  

## laod docker image:  
docker load -i python3-tensorflow-gpu.tar  

## renew docker tag:(just type container ID former least 4 words)  
docker tag acbf allen/python3-tensorflow-gpu

## for someone using, create a file and load nvidia-docker  
mkdir ExtStorage  
sudo nvidia-docker run -it -v /home/allen/ExtStorage:/workspace markliou/python3-tensorflow-gpu bash

 ---  
## search which container running
docker -ps  

## all dockers inculding open, close and dead
docker -ps


