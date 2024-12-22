# SQL Introduction

This directory contains a series of SQL scripts that introduce the basics of interacting with a MySQL database. Each script corresponds to a specific task that is designed to help you understand how to use SQL for common database operations.

## Tasks

### 0. List Databases
- **File:** `0-list_databases.sql`
- **Description:** This script lists all databases in the MySQL server.

### 1. Create a Database
- **File:** `1-create_database_if_missing.sql`
- **Description:** This script creates the database `hbtn_0c_0` in the MySQL server. If the database already exists, the script does not fail.

### 2. Delete a Database
- **File:** `2-remove_database.sql`
- **Description:** This script deletes the `hbtn_0c_0` database if it exists. If the database does not exist, the script does not fail.

### 3. List Tables
- **File:** `3-list_tables.sql`
- **Description:** This script lists all tables in a given database, passed as an argument to the MySQL command.

### 4. First Table
- **File:** `4-first_table.sql`
- **Description:** This script creates a table called `first_table` in the current database. The table has two columns: `id` (INT) and `name` (VARCHAR(256)). If the table already exists, the script does not fail.

### 5. Full Description
- **File:** `5-full_table.sql`
- **Description:** This script prints the full description (create statement) of the table `first_table` in the `hbtn_0c_0` database without using `DESCRIBE` or `EXPLAIN`.

### 6. List All in Table
- **File:** `6-list_values.sql`
- **Description:** This script lists all rows from the `first_table` in the `hbtn_0c_0` database, displaying all fields.

### 7. First Add
- **File:** `7-insert_value.sql`
- **Description:** This script inserts a new row into the `first_table` in the `hbtn_0c_0` database with `id = 89` and `name = 'Best School'`.

### 8. Count 89
- **File:** `8-count_89.sql`
- **Description:** This script counts the number of rows with `id = 89` in the `first_table` in the `hbtn_0c_0` database.

### 9. Full Creation
- **File:** `9-full_creation.sql`
- **Description:** This script creates a table called `second_table` in the `hbtn_0c_0` database and inserts multiple rows into the table. The table includes `id`, `name`, and `score` columns.

### 10. List by Best
- **File:** `10-list_by_best.sql`
- **Description:** This script lists all records from the `second_table` in the `hbtn_0c_0` database, ordered by `score` in descending order.

## Requirements

- **MySQL Version:** 8.0 (tested with version 8.0.25-0ubuntu0.20.04.1)
- **Operating System:** Ubuntu 20.04 LTS
- **Editors:** Allowed editors are vi, vim, emacs

## Setup Instructions

1. Install MySQL 8.0 on Ubuntu 20.04 LTS:
   ```bash
   sudo apt update
   sudo apt install mysql-server
