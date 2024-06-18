-- Select cities and their corresponding state names
-- The output should be ordered by the cities id
-- The states table has (id, name)
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
