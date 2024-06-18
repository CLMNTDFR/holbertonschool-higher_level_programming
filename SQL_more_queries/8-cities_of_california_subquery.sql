-- Select cities of California using subquery
-- The state_id for California must be obtained from the states table
-- The output should be ordered by the cities id
SELECT id, name FROM cities
WHERE state_id IN (SELECT id FROM states WHERE name = "California") 
ORDER BY id ASC;
