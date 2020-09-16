Basic Select Statement:

1. SELECT first_name as "First Name", last_name as "Last Name"
FROM employees


2. SELECT department_id FROM employees WHERE employee_id = 100

3. SELECT * FROM employees ORDER BY first_name DESC

4. SELECT first_name, last_name, salary, salary*0.15 as "PF" FROM employees
5. SELECT employee_id, first_name, last_name, salary FROM employees ORDER BY salary ASC
6. SELECT sum(salary) FROM employees 
7. SELECT max(salary), min(salary) FROM employees

8. SELECT avg(salary), count(*) FROM employees
9. SELECT count(*) FROM employees 
10. SELECT count(DISTINCT job_id) FROM employees
11. SELECT upper(first_name) FROM employees
12. SELECT substring(first_name,  1, 3) FROM employees
13. SELECT 171*214+625
14. SELECT concat(first_name, ' ', last_name) as name FROM employees
15. SELECT TRIM(first_name) FROM employees
16. SELECT first_name, last_name, length(concat(first_name, last_name)) FROM employees
17. SELECT * FROM employees where first_name like '%[0-9]%' 

18. SELECT * FROM employees LIMIT(10)
19. SELECT ROUND(salary/12, 2) FROM employees \g



Create Tables:

1. CREATE TABLE countries (
country_id integer,
country_name varchar(25),
region_id integer
);


2. CREATE TABLE countries2 (
country_id integer,
country_name varchar(25),
region_id integer,
FOREIGN KEY (country_id) REFERENCES countries(country_id),
FOREIGN KEY (country_name) REFERENCES countries(country_name),
FOREIGN KEY (region_id) REFERENCES countries(region_id),
);


3. CREATE TABLE dup_countries2 AS SELECT * FROM countries WHERE 1 = 2

4. SELECT * INTO dup_countries FROM countries

5. CREATE TABLE countries (
country_id integer NULL,
country_name varchar(25),
region_id integer
);


6. CREATE TABLE jobs (
 job_id  integer,
 job_title varchar(25),
 min_salary integer,
 max_salary integer
);

SELECT * FROM jobs WHERE max_salary > 25000


7. CREATE TABLE countries3 (
country_id integer,
country_name varchar(25),
CONSTRAINT chk_frequency CHECK (country_name IN ('Italy', 'India', 'China')),
region_id integer
);
8.
9.
10.
11.
12.
13.
14.
15.
16.


