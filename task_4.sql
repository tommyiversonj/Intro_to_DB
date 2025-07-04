-- task_4.sql

-- Select the database to use
USE alx_book_store;

-- Print the full description of the 'books' table without using DESCRIBE or EXPLAIN
SELECT
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_KEY,
    COLUMN_DEFAULT,
    EXTRA
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_SCHEMA = 'alx_book_store' AND TABLE_NAME = 'books';