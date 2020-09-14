
CREATE TABLE items (ID int Serial PRIMARY KEY,ITEM varchar(255) NOT NULL,PRICE integer);
CREATE TABLE customers (ID int Serial PRIMARY KEY,first_name varchar(25) NOT NULL,last_name varchar(25));

INSERT INTO items(item_name, item_price)
VALUES('Small Desk', 100),('Large Desk', 300),('Fan', '80')

INSERT INTO customers(first_name, last_name)
VALUES('Greg', 'Jones'),('Sandra', 'Jones'),('Scott', 'Scott'),('Trevor', 'Green'),('Melanie','Johnson')

SELECT * from items where item_price > 80

SELECT * from items where item_price < 30

SELECT * from customers where last_name = 'Smith'

SELECT * from customers where first_name != 'Craig'