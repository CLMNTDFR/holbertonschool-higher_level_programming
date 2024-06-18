-- Create database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to using hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create cities table if it does not exist
-- id INT unique, auto generated, can’t be null and is a primary key
-- state_id INT not null, foreign key to states table
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
