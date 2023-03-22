-- Create the hbnb_dev_db database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create the hbnb_dev user if it doesn't already exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant hbnb_dev all privileges on the hbnb_dev_db database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grant hbnb_dev SELECT privilege on the performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
