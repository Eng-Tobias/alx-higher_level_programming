-- This script lists all records with a non-NULL name from the second_table.
-- The results are ordered by score in descending order.

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
