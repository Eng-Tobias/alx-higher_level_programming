-- Select the database
USE hbtn_0c_0;

-- Query to get the max temperature for each state ordered by state name
SELECT state, MAX(temperature) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
