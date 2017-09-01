# SQL Section 07 - Homework 2 - Update and print records

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    
    c.execute("UPDATE inventory SET Quantity = 999 WHERE Make='Ford' AND Model='Focus'")
    c.execute("UPDATE inventory SET Model = 'Mondeo' WHERE Model='Ka'")
    
    c.execute("SELECT * FROM inventory")
    
    rows = c.fetchall()
    
    print("\nNEW DATA\n")
    
    for r in rows:
        print(r[0], r[1], r[2])