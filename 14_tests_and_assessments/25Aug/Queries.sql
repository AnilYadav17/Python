CREATE TABLE employee_activity (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_name VARCHAR(100),
    department VARCHAR(50) ,
    salary DECIMAL(10, 2),
    employment_type ENUM('FULL_TIME', 'PART_TIME', 'CONTRACT'),
    skills SET('PYTHON', 'MYSQL', 'JAVA', 'REACT', 'AWS', 'AI_ML'),
    joining_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    email VARCHAR(100),
    city VARCHAR(50)
);

INSERT INTO employee_activity 
(employee_name, department, salary, employment_type, skills, email, city) 
VALUES 
('Amit Sharma', 'IT', 75000, 'FULL_TIME', 'PYTHON,MYSQL,AI_ML', 'amit.sharma@gmail.com', 'Indore'),
('Priya Verma', 'HR', 52000, 'FULL_TIME', 'MYSQL,REACT', 'priya.verma@gmail.com', 'Bhopal'),
('Rahul Mehta', 'IT', 95000, 'CONTRACT', 'PYTHON,JAVA,AWS', 'rahul.mehta@gmail.com', 'Indore'),
('Neha Joshi', 'Finance', 68000, 'PART_TIME', 'MYSQL,AI_ML', 'neha.joshi@yahoo.com', 'Pune'),
('Vikas Patel', 'IT', 85000, 'FULL_TIME', 'PYTHON,REACT,AWS,AI_ML', 'vikas.patel@gmail.com', 'Mumbai');





-- Query 1
SELECT * FROM employee_activity
WHERE (department = 'IT' and salary > 80000)
   OR (department = 'Finance' and salary BETWEEN 60000 and 70000)
order by salary desc;





-- Query 2
SELECT * FROM employee_activity
WHERE department != 'HR'
  AND employment_type IN ('FULL_TIME', 'CONTRACT')
  AND salary > 70000
ORDER BY salary DESC
LIMIT 3;



-- Query 3
SELECT * FROM employee_activity
WHERE employee_name LIKE '%a%'
  AND (FIND_IN_SET('PYTHON', skills) > 0 OR FIND_IN_SET('AI_ML', skills) > 0)
ORDER BY employee_name ASC;


-- Query 4
SELECT * FROM employee_activity
WHERE joining_date BETWEEN '2025-01-01 00:00:00' AND '2025-12-31 23:59:59'
ORDER BY joining_date ASC;



-- Query 5
SELECT * FROM employee_activity
WHERE (department = 'IT' AND salary > 70000 AND employment_type IN ('FULL_TIME', 'CONTRACT'))
   OR (department = 'Finance' AND salary BETWEEN 60000 AND 75000 AND (FIND_IN_SET('MYSQL', skills) > 0 OR FIND_IN_SET('AI_ML', skills) > 0))
   OR (department = 'HR' AND employment_type = 'FULL_TIME' AND city IN ('Bhopal', 'Indore'))
ORDER BY salary DESC, employee_name ASC
LIMIT 4;



-- Query 6
SELECT * FROM employee_activity
WHERE department != 'HR'
  AND salary BETWEEN 65000 AND 95000
  AND city IN ('Indore', 'Mumbai', 'Pune')
  AND employment_type != 'PART_TIME'
  AND (FIND_IN_SET('PYTHON', skills) > 0 OR FIND_IN_SET('AWS', skills) > 0)
  AND (employee_name LIKE '%a%' OR employee_name LIKE '%i%')
  AND (department != 'Finance' OR salary > 65000)
ORDER BY salary DESC, joining_date DESC, employee_name ASC
LIMIT 2;
