CREATE TABLE items (
    item_id integer SERIAL PRIMARY KEY,
    item_name varchar(25), 
    price decimal(4,2)
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    order_number integer,
    item_id integer,
    FOREIGN KEY (item_id) REFERENCES items(item_id)
);

CREATE or REPLACE FUNCTION order_price (ord_num integer) 
RETURNS decimal(6,2) AS $total_price$
BEGIN
   RETURN(SELECT SUM(items.price) 
   FROM items
   JOIN orders ON orders.item_id=items.item_id
   WHERE orders.order_number = ord_num
   ); 
    
END;
$total_price$ LANGUAGE plpgsql;
