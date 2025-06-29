#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server (without specifying a database yet)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="@1992myown"  # <-- Replace with your actual password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        try:
            # Attempt to create database
            cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_BOOK_STORE")
            print("Database 'alx_book_store' created successfully!")
        except Error as e:
            print(f"Error creating database: {e}")
        finally:
            cursor.close()
            connection.close()

except Error as e:
    print(f"Error connecting to MySQL server: {e}")
