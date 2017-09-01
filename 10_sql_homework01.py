# SQL JOIN - Homework01

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    
    # Create new table orders
    c.execute("""CREATE TABLE orders
            (make TEXT, model TEXT, order_date DATE)
            """)
    
    orders = [
        ('Ford', 'Focus', '2017-04-30'),
        ('Ford', 'Focus', '2017-04-30'),
        ('Ford', 'Focus', '2017-02-21'),
        ('Ford', 'Mondeo', '2017-04-13'),
        ('Ford', 'Mondeo', '2017-02-19'),
        ('Ford', 'Mondeo', '2017-03-17'),
        ('Ford', 'Fiesta', '2017-05-18'),
        ('Ford', 'Fiesta', '2017-01-02'),
        ('Ford', 'Fiesta', '2017-06-01'),
        ('Honda', 'Civic', '2017-01-24'),
        ('Honda', 'Civic', '2017-03-04'),
        ('Honda', 'Civic', '2017-07-23'),
        ('Honda', 'Jazz', '2017-08-10'),
        ('Honda', 'Jazz', '2017-05-01'),
        ('Honda', 'Jazz', '2017-07-08')
        ]
        
    c.executemany("INSERT INTO orders VALUES(?, ?, ?)", orders)