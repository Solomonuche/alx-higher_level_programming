-- a script that creates the database hbtn_0d_usa and the table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa
CREATE TABLE IF NOT EXISTS `unique_id` IN `hbtn_0d_usa` (
	`id` INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
	`name` VARCHAR(256) NOT NULL
)
