-- Write a script that creates the database hbtn_0d_usa and the table cities

-- Creating database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Using hbtn_0d_usa database
USE hbtn_0d_usa;

-- creating table called states in hbtn_0d_usa database
CREATE TABLE IF NOT EXISTS cities(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY  UNIQUE,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) 
	REFERENCES states (id)
);


