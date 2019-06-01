#!/bin/bash
/etc/init.d/mysql restart
mysql -uroot <<MY_QUERY
CREATE DATABASE langs;
USE langs;
MY_QUERY
mysql langs -uroot < /flask_test/db
mysql -uroot <<USER_ROOT
CREATE USER 'root1'@'localhost' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON *.* TO 'root1'@'localhost';
UPDATE user SET plugin='auth_socket' WHERE User='root1';
FLUSH PRIVILEGES;
USER_ROOT
