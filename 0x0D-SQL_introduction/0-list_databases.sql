-- List initial databases
SELECT schema_name AS 'Database'
FROM information_schema.schemata
WHERE schema_name NOT IN ('information_schema', 'performance_schema', 'mysql', 'sys');

-- Create multiple databases
CREATE DATABASE my_db_01;
CREATE DATABASE my_db_02;
CREATE DATABASE my_db_03;
CREATE DATABASE holbteron_db;

-- List databases again after creation
SELECT schema_name AS 'Database'
FROM information_schema.schemata
WHERE schema_name NOT IN ('information_schema', 'performance_schema', 'mysql', 'sys');
