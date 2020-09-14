<!-- EXERCISE 1 -->

UPDATE students
SET first_name = 'Lea'
WHERE first_name = 'lea';

UPDATE students
SET birth_date = '1998-11-02 00:00:00'
WHERE last_name = 'Dupont';

DELETE FROM students WHERE first_name = 'Lea' and last_name = 'Dupont'

SELECT COUNT(*) FROM students

SELECT COUNT(*) FROM students WHERE birth_date > '2000-01-01 00:00:00'

ALTER TABLE students
ADD COLUMN math_grade int

UPDATE students SET math_grade = 80
WHERE id = 1 

UPDATE students SET math_grade = 90
WHERE id = 2 or id = 4 

INSERT INTO students (first_name, last_name, birth_date, math_grade)
VALUES('Omer', 'Simpson', '1980-03-10 00:00:00', 70)

SELECT SUM(math_grade)
FROM students

<!-- EXERCISE 2 -->

SELECT * FROM items ORDER BY item_price ASC

SELECT * FROM items 
WHERE item_price > 80
ORDER BY item_price DESC 

SELECT first_name, last_name FROM customers WHERE customer_id < 4 ORDER BY last_name ASC


SELECT first_name, last_name FROM customers WHERE customer_id > 3 ORDER BY last_name DESC

SELECT first_name, last_name FROM customers ORDER BY first_name DESC OFFSET 3 

SELECT last_name FROM customers
ORDER BY last_name DESC

CREATE TABLE purchases (
    customer_id int,
    item_id int,
	FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
	FOREIGN KEY (item_id) REFERENCES items(item_id)
);

INSERT INTO purchases (customer_id)
VALUES(2) 
<!-- worked -->

INSERT INTO purchases (customer_id, item_id)
VALUES(1, 1), (2, 2), (3, 3), (4, 1), (4, 2) 

SELECT purchases.customer_id, purchases.item_id, customers.first_name, customers.last_name 
FROM purchases
INNER JOIN customers ON purchases.customer_id=customers.customer_id;

SELECT *
FROM purchases
WHERE customer_id = 4

SELECT *
FROM purchases
WHERE item_id = 1 or item_id = 2


INSERT INTO purchases(customer_id, item_id)
VALUES(3, 3)


DELETE FROM purchases WHERE customer_id = 3

SELECT * FROM purchases WHERE customer_id = 3



SELECT customers.first_name, customers.last_name, items.item_name 
FROM customers
INNER JOIN purchases ON customers.customer_id=purchases.customer_id 
INNER JOIN items ON items.item_id=purchases.item_id;