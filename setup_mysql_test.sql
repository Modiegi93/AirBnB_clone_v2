-- Create the hbnb_test_db database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create the hbnb_test user if it doesn't already exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant hbnb_test all privileges on the hbnb_test_db database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grant hbnb_test SELECT privilege on the performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
