# ansible  
![alt text](https://github.com/allen050883/Manipulate/blob/master/ansible/ansible_structure.png)  
reference: https://chusiang.gitbooks.io/automate-with-ansible/content/09.how-to-practive-the-ansible-with-docker-compose.html  
  
## 1. install ansible  
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

```
echo "[test]" sudo tee -a /etc/ansible/hosts
echo "172.18.35.122" sudo tee -a /etc/ansible/hosts
echo "[test]" sudo tee -a /etc/ansible/hosts

```
