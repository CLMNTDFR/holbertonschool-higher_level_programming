USE hbtn_0c_0;

-- List all records with score and name, filtering out rows without a name value
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;