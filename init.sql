CREATE DATABASE my_logs;
USE my_logs;

CREATE TABLE daily_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    weekday VARCHAR(10),
    time TIME,
    text TEXT
);
