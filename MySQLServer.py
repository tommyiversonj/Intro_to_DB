#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="@1992myown"  # Replace with your password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.Error as err:
            print(f"Error creating database: {err}")
        finally:
            cursor.close()
            connection.close()

except mysql.connector.Error as err:
    print(f"Error connecting to MySQL server: {err}")
