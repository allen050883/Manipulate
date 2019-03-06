## docker

#save docker image: 
docker save -o b5d632d87a03.tar b5d632d87a03

#laod docker image:
docker load -i python3-tensorflow-gpu.tar

#renew docker tag:
docker tag acbf allen/python3-tensorflow-gpu

mkdir ExtStorge 

nvidia-docker run -it -v /home/allen/ExtStorage:/workspace markliou/python3-tensorflow-gpu bash

