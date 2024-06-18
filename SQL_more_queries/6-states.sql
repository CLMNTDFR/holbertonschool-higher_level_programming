-- Create database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to using hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create states table if it does not exist
-- id INT unique, auto generated, can’t be null and is a primary key
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
