## Do these things first  
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
sudo chgrp -R group_name new_project.git
sudo chmod 771 -R new_project.git
git init --bare
```
### local  
##### Setting  
```bash
git config --global user.name "userA"
git config --global user.email "userA@example.com"
git remote add origin ssh://userA@user.host:
```
##### Upload  
```bash
git add new_test.txt
git commit -m "add new_test.txt"
git push origin master
```
(origin can be considered the ssh way, so 'git push origin local:server')
(server show in 'git branch -a' is 'remote/origin/master')
  
##### Delete  
```bash
git rm new_test.txt
git commit -m "delete new_test.txt"
git push
```
##### Revert
back to the before commit
```bash
git revert commit_number
#or
git stash drop commit_number
git revert HEAD
```
  
##### plot graph
```bash
git log --graph --full-history --all --color \
--pretty=format:"%x1b[31m%h%x09%x1b[32m%d%x1b[0m%x20%s"
```
  
  
##### for the case  
get the master and branch the new one in the local
if finished, upload the branch and merge the master on the git server.
```bash
git pull master
git branch -b new_branch
```
  
##### function    
```bash
git branch -d <branch>  #remove branch
git log --oneline
git reset <id>
```
