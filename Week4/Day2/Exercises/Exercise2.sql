-- SELECT * FROM customer;

-- SELECT first_name || ' ' || last_name AS full_name FROM customer;

-- SELECT create_date FROM customer;

-- SELECT * FROM customer ORDER BY first_name DESC;

-- SELECT film_id, title, description, release_year, rental_rate FROM film
-- ORDER BY rental_rate ASC;

-- SELECT address, phone FROM address WHERE district = 'Texas';

-- SELECT * FROM film WHERE film_id in (15, 150);

-- SELECT film_id, title, description, length, rental_rate FROM film
-- WHERE title = 'The Godfather';

-- SELECT film_id, title, description, length, rental_rate FROM film
-- WHERE title LIKE 'Go%' ORDER BY title;

-- SELECT title, replacement_cost FROM film
-- ORDER BY replacement_cost ASC LIMIT 10;

-- SELECT title, replacement_cost FROM film
-- ORDER BY replacement_cost ASC
-- OFFSET 10 ROWS
-- FETCH NEXT 10 ROWS ONLY;

-- customer and payment - f.name l.name, amount date order by id(customer?)

-- SELECT customer.first_name, customer.last_name, payment.amount, payment.payment_date
-- FROM customer 
-- INNER JOIN payment ON customer.customer_id = payment.customer_id;

-- SELECT film.film_id, film.title 
-- FROM film
-- LEFT JOIN inventory ON film.film_id = inventory.film_id
-- WHERE inventory.film_id IS NULL;

-- SELECT country.country, city.city
-- FROM city 
-- INNER JOIN country ON city.country_id = country.country_id
-- ORDER BY country;

-- SELECT customer.customer_id, customer.first_name, customer.last_name, payment.amount, payment.payment_date, staff.staff_id, staff.first_name
-- FROM customer
-- INNER JOIN payment ON customer.customer_id = payment.customer_id
-- INNER JOIN staff ON payment.staff_id = staff.staff_id
-- ORDER BY staff.staff_id;

