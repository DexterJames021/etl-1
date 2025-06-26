-- Example SQL queries commonly used by data engineers

-- 1. Selecting data
SELECT id, name, created_at
FROM users
WHERE status = 'active'
ORDER BY created_at DESC;

-- 2. Aggregation
SELECT department, COUNT(*) AS employee_count, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING COUNT(*) > 10;

-- 3. Joining tables
SELECT o.order_id, c.customer_name, o.total_amount
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.order_date >= '2024-01-01';

-- 4. Inserting data
INSERT INTO logs (event_type, event_time)
VALUES ('login', NOW());

-- 5. Updating data
UPDATE products
SET price = price * 1.1
WHERE category = 'electronics';

-- 6. Deleting data
DELETE FROM sessions
WHERE last_active < NOW() - INTERVAL '30 days';

-- 7. Creating an index
CREATE INDEX idx_users_email ON users(email);

-- 8. Creating a table
CREATE TABLE audit_log (
    id SERIAL PRIMARY KEY,
    action VARCHAR(100),
    user_id INT,
    action_time TIMESTAMP DEFAULT NOW()
);