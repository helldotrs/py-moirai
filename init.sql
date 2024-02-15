-- Log in to your MariaDB server using the MySQL command-line client:
mysql -u root -p

-- Once logged in, create a new database for the Moirai software. Let's name it `moirai_db`:
CREATE DATABASE moirai_db;

-- After creating the database, switch to using it:
USE moirai_db;

-- Now, create a table named `punch_records` with the specified fields:
CREATE TABLE punch_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE DEFAULT CURRENT_DATE,
    time TIME DEFAULT CURRENT_TIME,
    weekday VARCHAR(9),
    maintext VARCHAR(255),
    comment VARCHAR(255)
);

-- Your database and table are now set up. You can start using them with the Moirai software.
