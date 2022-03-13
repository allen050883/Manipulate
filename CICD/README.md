# Jenkins  
### Install Jenkins  
```
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -

sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'

sudo apt-get update -y

sudo apt-get install jenkins -y
```
  
###  Start Jenkins  
```
sudo systemctl start jenkins

sudo systemctl status jenkins

```
