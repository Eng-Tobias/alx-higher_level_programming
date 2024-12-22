-- Select the database
USE hbtn_0c_0;

-- Convert the database `hbtn_0c_0` to UTF8 (utf8mb4 character set and utf8mb4_unicode_ci collation)
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Convert the table `first_table` to UTF8 (utf8mb4 character set and utf8mb4_unicode_ci collation)
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Modify the `name` column without explicitly specifying `CHARACTER SET utf8mb4`
ALTER TABLE first_table MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci;
