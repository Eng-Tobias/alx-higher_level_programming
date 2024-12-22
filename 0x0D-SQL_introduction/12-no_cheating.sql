-- This script updates the score of Bob to 10 in the second_table.
-- It uses the name field and not the id to find the record.

UPDATE second_table
SET score = 10
WHERE name = 'Bob';
