SELECT city, SUM(amount) AS total_sales
FROM customer_orders
GROUP BY city;

SELECT product, AVG(amount) AS average_sales
FROM customer_orders
GROUP BY product;