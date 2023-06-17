-- Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
-- lists all records of the table second_table of the database hbtn_0c_0a showing only score and name field

SELECT score, name FROM second_table
ORDER BY score DESC;
