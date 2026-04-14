-- Creating a table
CREATE TABLE dino(
    sn INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    score INTEGER
);

-- Insert data in table
INSERT INTO dino(sn,name,score) VALUES(1,'Om',700);
INSERT INTO dino(sn,name,score) VALUES(2,'Jeet',600);
INSERT INTO dino(sn,name,score) VALUES(3,'Mark',100);
INSERT INTO dino(sn,name,score) VALUES(4,'Nick',250);
INSERT INTO dino(sn,name,score) VALUES(5,'Ben',870);
INSERT INTO dino (name,score) VALUES('Aman',5600);

-- Display info from the table
SELECT * FROM dino;
SELECT name,score FROM dino WHERE score > 500;
SELECT avg(score) AS 'Avarage dino game score' FROM dino;
SELECT count(*) AS 'Number of dino game players' FROM dino;

-- Updating
UPDATE dino SET score = 1200 WHERE name = 'Om';

-- Clearing all
DELETE FROM dino;

-- Clearing 1
DELETE FROM dino WHERE sn = 4;

DROP TABLE dino;