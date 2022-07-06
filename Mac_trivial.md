# homebrew install
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

#https://brew.sh/index_zh-tw
```
  
# Install mysql 8.0.29
```
brew uninstall mysql --force
rm -fr /usr/local/var/mysql/

brew install mysql
brew services start mysql

#直接可以進入，不需要密碼
mysql -u root
#自行設定root密碼
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '';

```
  
# Install jdk11 and maven
```
brew install java11
sudo ln -sfn /usr/local/opt/openjdk@11/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-11.jdk
echo 'export PATH="/opt/homebrew/opt/openjdk@11/bin:$PATH"' >> ~/.zshrc
echo 'export PATH="/Library/Java/JavaVirtualMachines/openjdk-11.jdk/Contents/Home/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
java --version
```
