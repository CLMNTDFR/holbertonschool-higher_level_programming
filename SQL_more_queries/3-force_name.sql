-- Create a table force_name with two columns id (integer) and name
-- (string, not null), if he doesn't exist, in server
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
