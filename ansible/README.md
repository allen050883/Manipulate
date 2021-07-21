# ansible  
![alt text](https://github.com/allen050883/Manipulate/blob/master/ansible/ansible_structure.png)  
reference: https://chusiang.gitbooks.io/automate-with-ansible/content/09.how-to-practive-the-ansible-with-docker-compose.html  
  
## 1. install ansible  
Install ansible on control master  
1.  update, upgrade and install python  
2. install ansible by apt or pip  
```
#sudo rm /var/lib/apt/lists/*
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install python3-pip -y
echo "alias python=python3" | sudo tee -a ~/.bashrc
echo "alias pip=pip3" | sudo tee -a ~/.bashrc
source ~/.bashrc
sudo apt-get install ansible -y #also use pip install
```
  
## 2. set cluster IP ssh-key auto-login  
First, generate `ssh-key` and send public key to remote server, you can use `ssh-copy-id` or this script.  
```
ssh-key
```
the easy script
```
#!/bin/bash
for ip in `cat /home/list_of_servers`; do
    ssh-copy-id -i ~/.ssh/id_rsa.pub $ip
done
```
or this way
```
ssh-key
ssh-copy-id abc@1.2.3.4
ssh-copy-id def@1.2.3.5
```
Second, edit `/etc/ansible/hosts` to set parameter for when ansible controlling as user, password, python version or something else.  
reference: https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html  
In this `hosts`, `[local]` is the group name, the following `[test]` you can change by yourself  
  
`ansible_python_interpreter=/usr/bin/python3` set python3 as the default python version to run ansible basically  
`ansible_user="abc"` set user name to login and use  
`ansible_become_pass="123"`  user password  
  
```
sudo su -c '/bin/echo -e "[local]\nlocalhost ansible_connection=local ansible_python_interpreter=/usr/bin/python3 ansible_become_pass="123"" >> /etc/ansible/hosts'
sudo su -c '/bin/echo -e "[test]" >> /etc/ansible/hosts'
sudo su -c '/bin/echo -e "1.2.3.4 ansible_python_interpreter=/usr/bin/python3 ansible_user="abc" ansible_become_pass="abc"" >> /etc/ansible/hosts'
sudo su -c '/bin/echo -e "1.2.3.5 ansible_python_interpreter=/usr/bin/python3 ansible_user="def" ansible_become_pass="def"" >> /etc/ansible/hosts'
```
Test ping the remote IP  
`all` can ping all IP, also you can use the specific group  
```
ansible all -m ping
```
Result, successful!  
```
localhost | SUCCESS => {
    "changed": false, 
    "ping": "pong"
}
1.2.3.4 | SUCCESS => {
    "changed": false, 
    "ping": "pong"
}
1.2.3.5 | SUCCESS => {
    "changed": false, 
    "ping": "pong"
}
```
  
## 2.5 speed up ansible, important!!
In my experience, ansible run to check lots of things, so in the `/etc/ansible/ansible.cfg` and find `pipelinfing`  
```
pipelining = True 

```  
it helps to speed up, maybe you can search Mitogen more quickly.  
  
## 3.  install docker by yml document  
create a document to write yaml file installing docker
```
nano docker_install.yml
```
write the install docker method  
Introduce Parameter:  
`hosts: all` is give the order to all IP, you can give specific group 
`become`, default is false, ansible use 'username' to run command; if true, ansible use 'root'
I want to add user to new group 'docker', but it can not work!  
Therefore, when `become` is true, notice the default user is 'root' and directory will difficultly go to '/home/user/'
```
---
- hosts: all
  become: false
  
  tasks:
    - name: Install aptitude using apt
      become: true
      apt: name=aptitude state=latest update_cache=yes force_apt_get=yes

    - name: Install required system packages
      become: true
      apt: name={{ item }} state=latest update_cache=yes
      loop: [ 'apt-transport-https', 'ca-certificates', 'curl', 'software-properties-common', 'python3-pip', 'virtualenv', 'python3-setuptools']

    - name: Add Docker GPG apt Key
      become: true
      apt_key:
        url: https://download.docker.com/linux/ubuntu/gpg
        state: present

    - name: Add Docker Repository
      apt_repository:
        repo: deb https://download.docker.com/linux/ubuntu bionic stable
        state: present

    - name: Update apt and install docker-ce
      become: true
      apt: update_cache=yes name=docker-ce state=latest
      
    - name: docker to group
      become: true
      shell: groupadd docker
      shell: usermod -aG docker $USER
      shell: sudo newgrp docker
      shell: service docker restart

``` 
Run `ansible-playbook` yaml file
```
ansible-playbook docker_install.yml
```
  
## 5. create directory and copy files  
The destination is to build docker image and run container, so copy the files to the remote server.
```
nano create_and_copy.yml  
```  
`src`, soruce of folder  
`dest`, destination and use `become: true` the folder user is 'root'  
`mode`, privilege  
`with_items`, '*'  means all files  
```
---
- hosts: all
  become: true
  
  tasks:
    - name: copy files
      copy:
        src: newtaipei
        dest: /root/
        mode: 0777
      with_items: 
        - '*'

```  
  
## 6. docker image pull or build
```
nano docker_images.yml
```
write the docker images built or pull method
I do not know why need use `pip install docker-py`, but install first
`docker_image`, built by Dockerfile
`docker_container`, run container

```
---
- hosts: all
  become: true

  tasks:
    - name: apt install pip3
      apt:
        state: latest
        name: python-pip

    - name: pip install docker
      pip:
        name:
          - docker
          - requests>=2.20.1
  
    - name: build docker image
      docker_image:
        name: example
        path: /root/example/
        state: present
        
    - name: run container
      docker_container:
        name:  ex
        image: example
        volumes: 
          - /root/example/:/example
        command: python example.py
```
