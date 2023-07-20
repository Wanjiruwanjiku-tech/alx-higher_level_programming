-- The script creates a database and a table
-- The table should be in the created database

-- The database:
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

-- Select the database:
USE `hbtn_0d_usa`;

-- The table:
CREATE TABLE IF NOT EXISTS `cities`(
	`id` INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
	`state_id` INTEGER NOT NULL,
	`name` VARCHAR(256) NOT NULL,
	FOREIGN KEY(`state_id`) REFERENCES `states`(`id`)
);
