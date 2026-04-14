CREATE TABLE IF NOT EXISTS student(
    Roll_NO TEXT PRIMARY KEY,
    Name TEXT,
    Address VARCHAR(30),
    Phone_NO TEXT,
    AGE INTEGER
);

-- Inserting Data
INSERT INTO student(Roll_NO, Name, Address, Phone_NO, Age) VALUES('1','Om','Australia','0456789630',14),('2', 'Emily Johnson', 'Manchester', '+44 7700 900002', 15), ('3', 'Harry Brown', 'Birmingham', '+44 7700 900003', 16), ('4', 'Amelia Wilson', 'Leeds', '+44 7700 900004', 14), ('5', 'Noah Taylor', 'Bristol', '+44 7700 900005', 17), ('6', 'Sophia Davies', 'Nottingham', '+44 7700 900006', 15);
INSERT INTO student(Roll_NO, Name, Address, Phone_NO, Age) VALUES('7', 'Emily Johnson', 'London', '07XXXXXXX1', 15), ('8', 'Oliver Smith', 'Manchester', '07XXXXXXX2', 14), ('9', 'Sophia Davies', 'London', '07XXXXXXX3', 16), ('10', 'Harry Brown', 'Birmingham', '07XXXXXXX4', 17), ('11', 'Amelia Wilson', 'Leeds', '07XXXXXXX5', 14), ('12', 'Jack Taylor', 'London', '07XXXXXXX6', 18), ('13', 'Isla Thompson', 'Manchester', '07XXXXXXX7', 15), ('14', 'Noah Anderson', 'Bristol', '07XXXXXXX8', 16), ('15', 'Mia Thomas', 'London', '07XXXXXXX9', 13), ('16', 'Leo Martin', 'Leeds', '07XXXXXX10', 17), ('17', 'Ella White', 'Birmingham', '07XXXXXX11', 15), ('18', 'James Harris', 'London', '07XXXXXX12', 16), ('19', 'Lily Clark', 'Manchester', '07XXXXXX13', 14), ('20', 'Ben Lewis', 'Bristol', '07XXXXXX14', 18), ('21', 'Chloe Walker', 'London', '07XXXXXX15', 15);

-- Display Table
SELECT * FROM student;
SELECT AGE, Name FROM student;
SElECT * FROM student WHERE Address = 'London' OR Address = 'Manchester';
SELECT * FROM student WHERE Address IN ('London','Manchester');

-- Update Table
UPDATE student SET Address = 'London' WHERE Roll_NO = '3';

-- Delete Row
DELETE FROM student WHERE Roll_NO = '8';

-- Sorting Table
SELECT AGE, Name FROM student ORDER BY AGE DESC;

-- Counting Table
SELECT count(*) AS 'Number of students from Manchester' FROM student WHERE Address = 'Manchester';
SELECT avg(AGE) AS 'Average age of students living in London' FROM student WHERE Address = 'London';

DROP TABLE student;