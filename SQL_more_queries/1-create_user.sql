-- Drop the user if it exists
DROP USER IF EXISTS 'user_0d_1'@'localhost';

-- Create MySQL user `user_0d_1` with a temporary password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
