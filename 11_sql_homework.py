# SQLITE Functions Homework

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    
    cars = []
    
    c.execute("SELECT make, model FROM inventory")
    
    rows = c.fetchall()
    
    for r in rows:
        cars.append((r[0], r[1]))
        
    for make, model in cars:
        c.execute("SELECT COUNT(*) FROM orders WHERE make=? AND model=?", (make, model))
        result = c.fetchone()[0]
        print("Number of {} {} car orders is {}".format(make, model, result))