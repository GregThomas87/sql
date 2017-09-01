# SQL Section 7 - Homework 1

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    
    cars = [
        ('Ford', 'Focus', 200),
        ('Ford', 'Ka', 1000),
        ('Ford', 'Fiesta', 23000),
        ('Honda', 'Civic', 302),
        ('Honda', 'Jazz', 20392)
        ]
        
    c.executemany("INSERT INTO inventory VALUES(?, ?, ?)", cars)