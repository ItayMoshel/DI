-- SELECT rating, COUNT(*) AS film_count
-- FROM film
-- GROUP BY rating;

-- SELECT title FROM film
-- WHERE mpaa_rating in ('G', 'PG-13');

-- SELECT title, rating AS mpaa_rating
-- FROM film
-- WHERE rating IN ('G', 'PG-13');

-- SELECT title, length, rental_rate, rating AS mpaa_rating
-- FROM film
-- WHERE rating IN ('G', 'PG-13') AND length < 120 AND rental_rate < 3
-- ORDER BY title;

-- UPDATE customer
-- SET first_name = 'Itay',
-- 	last_name = 'Moshel',
-- 	email = 'Itay@email.com'
-- WHERE customer_id = 1;

-- extracting address_id:
-- SELECT address.address_id, address.address, customer.first_name
-- FROM customer
-- INNER JOIN address ON customer.address_id = address.address_id
-- WHERE customer_id = 1; -> Returns 5.

-- UPDATE address
-- SET address = 'Remez 901'
-- WHERE address_id = 5;

-- SELECT customer.first_name, customer.last_name, customer.email, address.address
-- FROM customer
-- INNER JOIN address ON customer.address_id = address.address_id
-- WHERE customer_id = 1;
