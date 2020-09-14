ALTER TABLE students
ADD id SERIAL PRIMARY KEY
ADD first_name varchar(25)
ADD last_name varchar(25)
ADD birth_date TIMESTAMP

INSERT INTO students (first_name, last_name, birth_date)
VALUES ('Marc', 'Dupont', '1998-11-02 00:00:00'),
		('Yoan', 'Durant', '2010-03-12 00:00:00'),
		('Lea', 'Martin', '1987-07-24 00:00:00'),
		('Sarah', 'Benichou', '1996-04-07 00:00:00'),
		('lea', 'Dupont', '2003-06-14 00:00:00'),
		('Omer', 'Simpson', '1980-03-10 00:00:00')

INSERT INTO students (first_name, last_name, birth_date)
VALUES ('Dovid', 'Levine', '1997-09-22 09:33:00')

INSERT INTO students (first_name, last_name, birth_date)
VALUES ('Charlie', 'Greenman', '1990-09-12 04:03:00'),
('Benny', 'Green', '1990-03-26 00:00:00')

SELECT * FROM students

SELECT first_name, last_name FROM students

SELECT first_name, last_name FROM students WHERE id = 2

SELECT first_name, last_name FROM students WHERE first_name = 'Marc' and last_name = 'Dupont'

SELECT first_name, last_name FROM students WHERE first_name = 'Marc' or last_name = 'Dupont'
