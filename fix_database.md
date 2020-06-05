### If tables are broken, following the step to fix the tables in phpmyadmin  
  
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
