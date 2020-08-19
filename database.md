## Database I/O broken   
1. sudo service locator stop  
2. fix method  
3. sudo service locator start

#### easy method:  
1. cleaning table   
2. copy the other table (just the same structure)  
  
#### complicated method:
```
sudo systemctl stop nginx
rm /var/lib/mysql/DB/*.idb
mysql -uuser -ppassword
use DB_name
show TABLES;
DROP TABLES table_name;
CREATE TABLE table_name LIKE table_name
```
  
  
## python connect database method  
1. /etc/mysql/my.conf change bind_address=IP  
2. add root user and set 10.0.0.% (% any number)  
3. sudo service mysql restart  


## Creating Symlink to a directory  
ln -s {source-dir-name} {symbolic-dir-name}  
ex. ln -s /a/b/dir/ dir  
