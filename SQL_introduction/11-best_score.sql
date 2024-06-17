-- Query to select records with score >= 10 from second_table ordered by score descending
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;