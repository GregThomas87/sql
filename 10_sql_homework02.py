# SQL JOIN Homework 02

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    
    c.execute("""SELECT inventory.make, inventory.model, inventory.quantity,
        orders.order_date FROM inventory INNER JOIN orders ON
        inventory.model = orders.model ORDER BY inventory.Make, inventory.Model
        """)
        
    rows = c.fetchall()
    
    last_model = ""
    
    for r in rows:
        if not last_model == r[1]:
            print("\nMake: {}, Model: {}".format(r[0], r[1]))
            print("Quantity: {}".format(r[2]))
            print("Orders:")
        print(r[3])
        last_model = r[1]
    print()
