UPDATE film SET language_id = 3
WHERE film_id = 133 or film_id = 384

INSERT INTO customer (store_id, first_name, last_name, email, address_id, activebool, create_date, last_update, active)
VALUES(1, 'Davi', 'Lewman', 'davi.lewman@sakilacustomer.org', 123, true, '2020-09-15', '2020-09-15 15:25:00', 1 ),
(2, 'Levid', 'Leviman', 'levid.leviman@sakilacustomer.org', 145, false, '2020-09-15', '2020-09-15 15:25:00', 0 ),
(1, 'Olaf', 'Gobbleman', 'olaf.gobbleman@sakilacustomer.org', 127, true, '2020-09-15', '2020-09-15 15:32:00', 1 )

INSERT INTO film (title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, rating, last_update, special_features)
VALUES('Harry Potter 6', '6th book of hp', 2009, (SELECT language_id FROM language WHERE name = 'English'), 5, 4.50, 107, 16.99, 'PG-13', '2020-09-15 15:42:23', '{Trailers}'),('Harry Potter 5', '5th book of hp', 2007, (SELECT language_id FROM language WHERE name = 'English'), 5, 4.50, 107, 16.99, 'PG-13', '2020-09-15 15:42:23', '{Trailers}'),('Harry Potter 3', '3rd book of hp', 2005, (SELECT language_id FROM language WHERE name = 'English'), 5, 4.50, 107, 16.99, 'PG-13', '2020-09-15 15:42:23', '{Trailers}')

DROP TABLE customer_review

SELECT * 
FROM film 
INNER JOIN film_actor ON film_actor.film_id=film.film_id
INNER JOIN actor ON film_actor.actor_id=actor.actor_id
WHERE film.description LIKE 'sumo wrestler' and actor.first_name = 'Penelope'

SELECT * 
FROM film 
WHERE length < 60 and rating = 'R' and description LIKE 'Documentary'


SELECT * 
FROM film 
JOIN inventory ON film.film_id=inventory.film_id
JOIN rental ON inventory.inventory_id=rental.inventory_id
JOIN customer ON rental.customer_id=customer.customer_id
WHERE customer.last_name = 'Mahan' and film.rental_rate > 4.00 and rental.return_date > '2005-07-28 00:00:00' and rental.return_date < '2005-08-01 00:00:00'   

SELECT * 
FROM film 
JOIN inventory ON film.film_id=inventory.film_id
JOIN rental ON inventory.inventory_id=rental.inventory_id
JOIN customer ON rental.customer_id=customer.customer_id
WHERE customer.last_name = 'Mahan' and film.replacement_cost > 20.00 and (film.description LIKE '%boat%' or film.title LIKE '%boat%')



SELECT *
FROM film 
JOIN film_actor ON film.film_id=film_actor.film_id
JOIN actor ON film_actor.actor_id=actor.actor_id
WHERE first_name = 'Joe'  and last_name = 'Swank' and film.description LIKE '%Action%'



INSERT INTO rental (staff_id, rental_date, inventory_id, customer_id, return_date)
VALUES(1, '2020-09-15 00:00:00', 1525, (SELECT customer_id FROM customer WHERE first_name = 'Davi'), '2020-09-27 00:00:00'),
(1, '2020-09-15 00:00:00', 2079, (SELECT customer_id FROM customer WHERE first_name = 'Davi'), '2020-09-27 00:00:00'),
(1, '2020-09-15 00:00:00', 2001, (SELECT customer_id FROM customer WHERE first_name = 'Davi'), '2020-09-27 00:00:00')