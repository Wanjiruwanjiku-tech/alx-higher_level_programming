-- The script creates a new database and a  new table
-- The table should be in the new database
-- The database:
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

-- Select the database:
USE `hbtn_0d_usa`;

-- The table in new database:
CREATE TABLE IF NOT EXISTS `states` (`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL, `name` VARCHAR(256) NOT NULL);
