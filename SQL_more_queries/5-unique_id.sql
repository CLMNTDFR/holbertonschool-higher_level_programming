-- Script to create the table unique_id in MySQL
-- This script creates a table with a unique constraint on the id column.
-- Create unique_id table if it does not exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);