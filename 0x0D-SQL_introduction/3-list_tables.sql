#!/bin/bash
# This script lists all tables in a specified database

DB_NAME=$1
mysql -hlocalhost -uroot -p -e "SHOW TABLES;" $DB_NAME
