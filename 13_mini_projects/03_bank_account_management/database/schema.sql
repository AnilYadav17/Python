CREATE DATABASE IF NOT EXISTS bank_db;
USE bank_db;

CREATE TABLE IF NOT EXISTS account (
    account_no INT PRIMARY KEY,
    holder_name VARCHAR(50) NOT NULL,
    balance DECIMAL(10,2) NOT NULL,
    account_type VARCHAR(20) NOT NULL
);

INSERT INTO account (account_no, holder_name, balance, account_type) VALUES
(1001, 'Amit', 25000.00, 'Savings'),
(1002, 'Rahul', 40000.00, 'Current'),
(1003, 'Priya', 15000.00, 'Savings'),
(1004, 'Neha', 55000.00, 'Savings'),
(1005, 'Rohit', 30000.00, 'Current')
ON DUPLICATE KEY UPDATE
    holder_name = VALUES(holder_name),
    balance = VALUES(balance),
    account_type = VALUES(account_type);
