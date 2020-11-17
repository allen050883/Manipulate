# Do these things first  
### Install git on the Linux system  
```bash
sudo apt install git-all    
```
### SSH login without password  
```bash
ssh-keygen
ssh-copy-id user.name@user.IP
```
### add user to git group
```bash
# remote
sudo usermod --gid group_name userA
```
  
  
# Git server use (use ssh without apply git account)  
To use server to be the git server, and engineers use ssh to git push to the git server.  
  
### remote  
```bash
sudo mkdir /git/new_project.git
sudo chmod -R 770 new_project.git
sudo chgrp group_name new_project.git
git init --bare
```
### local  
##### Setting  
```bash
git config --global user.name "userA"
git config --global user.email "userA@example.com"
```
##### Upload  
```bash
git add new_test.txt
git commit -m "add new_test.txt"
git push origin master
```
##### Delete  
```bash
git rm new_test.txt
git commit -m "delete new_test.txt"
git push
```
  
