SELECT COUNT(*) FROM actors

INSERT INTO actors(first_name, last_name) 
VALUES('Thebig', 'Me')
<!-- the above line returns an error because "age" and "number_of_oscars" are left out and are assigned as NOT NULL -->