-- This script creates the first_table in the specified database
-- It creates the table with two columns: id and name
-- If the table already exists, the script will not fail

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
