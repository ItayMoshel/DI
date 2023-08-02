-- CREATE TABLE purchases (
-- 	id SERIAL PRIMARY KEY,
-- 	customer_id INTEGER REFERENCES customers(customer_id),
-- 	item_id INTEGER REFERENCES items(item_id),
-- 	quantity_purchased INTEGER
-- );

-- INSERT INTO purchases (customer_id, item_id, quantity_purchased)
-- VALUES (
--     (SELECT customer_id FROM customers WHERE first_name = 'Scott' AND last_name = 'Scott'),
--     (SELECT item_id FROM items WHERE item_name = 'Fan'),
--     1
-- );

-- INSERT INTO purchases (customer_id, item_id, quantity_purchased)
-- VALUES (
--     (SELECT customer_id FROM customers WHERE first_name = 'Melanie' AND last_name = 'Johnson'),
--     (SELECT item_id FROM items WHERE item_name = 'Large Desk'),
--     10
-- );

-- INSERT INTO purchases (customer_id, item_id, quantity_purchased)
-- VALUES (
--     (SELECT customer_id FROM customers WHERE first_name = 'Greg' AND last_name = 'Jones'),
--     (SELECT item_id FROM items WHERE item_name = 'Small Desk'),
--     2
-- );

-- SELECT customers.first_name, customers.last_name, purchases.*
-- FROM purchases
-- JOIN customers ON purchases.customer_id = customers.customer_id;

-- SELECT * FROM purchases WHERE customer_id = 5;

-- SELECT * FROM purchases
-- WHERE item_id IN (
-- 	SELECT item_id FROM items WHERE item_name IN ('Small Desk', 'Large Desk')
-- );

-- SELECT customers.first_name, customers.last_name, items.item_name
-- FROM customers
-- JOIN purchases ON customers.customer_id = purchases.customer_id
-- JOIN items ON purchases.item_id = items.item_id;

-- it wont work. since the item_id column in the purchases table is defined
-- as a foreign key to the item_id column in the items table.

-- but we can insert NULL in item_id.
-- INSERT INTO purchases (customer_id, item_id, quantity_purchased)
-- VALUES (1, NULL, 3);


