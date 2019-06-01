#!/bin/bash
/etc/init.d/mysql restart
mysql -u root -p <<MY_QUERY
CREATE DATABASE langs;
USE langs;
MY_QUERY
mysql langs -uroot -p < /flask_test/db
mysql -u root -p <<USER_ROOT
CREATE USER 'root1'@'localhost' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON *.* TO 'root1'@'localhost';
UPDATE user SET plugin='auth_socket' WHERE User='root1';
FLUSH PRIVILEGES;
USER_ROOT
