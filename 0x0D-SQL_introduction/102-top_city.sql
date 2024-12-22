-- Select the database
USE hbtn_0c_0;

-- Query to get the top 3 cities' average temperature for July and August and order them by temperature
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
WHERE MONTH(date) IN (7, 8)  -- July (7) and August (8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
