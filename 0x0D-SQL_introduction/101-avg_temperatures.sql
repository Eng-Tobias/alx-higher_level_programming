-- Select the database
USE hbtn_0c_0;

-- Query to calculate the average temperature for each city and order by temperature in descending order
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
