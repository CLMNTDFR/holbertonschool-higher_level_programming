-- Create id_not_null table if it does not exist
-- (id INT with the default value 1)
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
