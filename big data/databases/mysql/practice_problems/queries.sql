# ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
# Create database - create database db_name;
# Switch Database - use db_name;
/*CREATE TABLE CUSTOMERS (
    ID INT NOT NULL,
    NAME VARCHAR(20) NOT NULL,
    AGE INT NOT NULL,
    ADDRESS CHAR(25),
    SALARY DECIMAL(18 , 2 ),
    PRIMARY KEY (ID)
);
DESC CUSTOMERS;

LOAD DATA INFILE 'c:/tmp/discounts.csv' 
INTO TABLE discounts 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
*/

create database if not exists assignment_1;
use assignment_1;

