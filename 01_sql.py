# Create tables homework

# Import sqlite3
import sqlite3

# create database connection
conn = sqlite3.connect("new.db")

# create a cursor
cursor = conn.cursor()

# execute SQL query to create my table
cursor.execute("""CREATE TABLE population
                (City TEXT, State TEXT, population INT)
                """)
                
# close database connection
conn.close()