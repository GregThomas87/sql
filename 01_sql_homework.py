# Create tables homework

# Import sqlite3
import sqlite3

# create database connection
conn = sqlite3.connect("cars.db")

# create a cursor
cursor = conn.cursor()

# execute SQL query to create my table
cursor.execute("""CREATE TABLE inventory
                (Make TEXT, Model TEXT, Quantity INT)
                """)
                
# close database connection
conn.close()