CREATE TABLE customer (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    city VARCHAR(50)
);

INSERT INTO customer (customer_id, customer_name, city) VALUES
(1, 'Amit', 'Indore'),
(2, 'Rahul', 'Pune'),
(3, 'Priya', 'Mumbai'),
(4, 'Neha', 'Delhi'),
(5, 'Karan', 'Bhopal'),
(6, 'Sneha', 'Jaipur');

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    order_date DATE,
    amount DECIMAL(10,2),
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);

INSERT INTO orders (order_id, order_date, amount, customer_id) VALUES
(101, '2026-01-10', 25000, 1),
(102, '2026-01-15', 18000, 2),
(103, '2026-02-05', 35000, 1),
(104, '2026-02-10', 12000, 3),
(105, '2026-02-15', 45000, 4),
(106, '2026-03-01', 22000, 2),
(107, '2026-03-05', 50000, 3),
(108, '2026-03-10', 15000, 1),
(109, '2026-03-15', 30000, 5);









-------------------------------   QUESTIONS -------------------------

SELECT c.customer_id, c.customer_name, c.city, o.order_id, o.amount
FROM customer c
JOIN orders o ON c.customer_id = o.customer_id;
---"""
mysql> select c.customer_id,c.customer_name,c.city,o.order_id,o.amount from customer as c join orders as o on c.customer_id  = o.customer_id;
+-------------+---------------+--------+----------+----------+
| customer_id | customer_name | city   | order_id | amount   |
+-------------+---------------+--------+----------+----------+
|           1 | Amit          | Indore |      101 | 25000.00 |
|           1 | Amit          | Indore |      103 | 35000.00 |
|           1 | Amit          | Indore |      108 | 15000.00 |
|           2 | Rahul         | Pune   |      102 | 18000.00 |
|           2 | Rahul         | Pune   |      106 | 22000.00 |
|           3 | Priya         | Mumbai |      104 | 12000.00 |
|           3 | Priya         | Mumbai |      107 | 50000.00 |
|           4 | Neha          | Delhi  |      105 | 45000.00 |
|           5 | Karan         | Bhopal |      109 | 30000.00 |
+-------------+---------------+--------+----------+----------+
--9 rows in set (0.00 sec)





SELECT c.customer_name, SUM(o.amount) AS total_amount
FROM customer c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name;
---
---mysql> select c.customer_name,sum(o.amount) from customer as c join orders as o
on c.customer_id = o.customer_id group by c.customer_id;
+---------------+---------------+
| customer_name | sum(o.amount) |
+---------------+---------------+
| Amit          |      75000.00 |
| Rahul         |      40000.00 |
| Priya         |      62000.00 |
| Neha          |      45000.00 |
| Karan         |      30000.00 |
+---------------+---------------+
5 rows in set (0.06 sec)
---



SELECT c.customer_name, SUM(o.amount) AS total_amount
FROM customer c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING SUM(o.amount) > 40000;
---
mysql> select c.customer_name,sum(o.amount) from customer as c join orders as o
on o.amount > 40000 group by c.customer_id;
+---------------+---------------+
| customer_name | sum(o.amount) |
+---------------+---------------+
| Amit          |      95000.00 |
| Rahul         |      95000.00 |
| Priya         |      95000.00 |
| Neha          |      95000.00 |
| Karan         |      95000.00 |
| Sneha         |      95000.00 |
+---------------+---------------+
6 rows in set (0.00 sec)
----






SELECT order_id, order_date, amount, customer_id
FROM orders
WHERE amount > (SELECT AVG(amount) FROM orders);
---
+----------+------------+----------+-------------+
| order_id | order_date | amount   | customer_id |
+----------+------------+----------+-------------+
|      103 | 2026-02-05 | 35000.00 |           1 |
|      105 | 2026-02-15 | 45000.00 |           4 |
|      107 | 2026-03-05 | 50000.00 |           3 |
|      109 | 2026-03-15 | 30000.00 |           5 |
+----------+------------+----------+-------------+
4 rows in set (0.02 sec)
---





SELECT c.customer_name, c.city, o.amount
FROM customer c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.amount = (SELECT MAX(amount) FROM orders);
---
+---------------+--------+----------+
| customer_name | city   | amount   |
+---------------+--------+----------+
| Priya         | Mumbai | 50000.00 |
+---------------+--------+----------+
---



SELECT DISTINCT c.customer_id, c.customer_name, c.city
FROM customer c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.amount > (SELECT AVG(amount) FROM orders);
---
+-------------+---------------+--------+
| customer_id | customer_name | city   |
+-------------+---------------+--------+
|           1 | Amit          | Indore |
|           4 | Neha          | Delhi  |
|           3 | Priya         | Mumbai |
|           5 | Karan         | Bhopal |
+-------------+---------------+--------+
---




SELECT c.customer_name, MAX(o.amount) AS highest_order
FROM customer c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING MAX(o.amount) > (SELECT AVG(amount) FROM orders);
---
+---------------+---------------+
| customer_name | highest_order |
+---------------+---------------+
| Amit          |      35000.00 |
| Priya         |      50000.00 |
| Neha          |      45000.00 |
| Karan         |      30000.00 |
+---------------+---------------+
---