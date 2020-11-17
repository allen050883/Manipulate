# Do the first two things  
### Install git on the Linux system  
```bash
sudo apt install git-all    
```
### SSH login without password  
```bash
ssh-keygen
ssh-copy-id user.name@user.IP
```
  
# Git server use (use ssh without apply git account)  
To use server to be the git server, and engineers use ssh to git push to the git server.  
  
### remote  
```bash
sudo mkdir /git/new_project.git
sudo 
```
1. git clone allen@example.com (create the connection)
2. git branch (can see what branch exists)
3. git branch 0.0.21.0 (create branch)
4. git checkout 0.0.21.0 (check this branch is switched)
5. copy all python file to the file
6. git add . (add to local git)
7. git config --global user.name "allen.tseng"
8. git config --global user.email "allen.tseng@example.com"
9. git commit -m"this is 0.0.21.0"
10. git push origin 0.0.21.0 (push to remote)
