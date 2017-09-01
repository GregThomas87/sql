# import random to generate a number
import sqlite3
import random

# connect to database newnum.db
with sqlite3.connect("newnum.db") as connection:
    #create cursor
    c = connection.cursor()
    # create table for hold numbers
    c.execute("DROP TABLE numbers")
    c.execute("CREATE TABLE IF NOT EXISTS numbers(number INT)")
    # loop 100 times to generate 100 numbers
    for i in range(100):
        # generate a random number between 0 and 100
        num = random.randint(0, 100)
        # insert number generated into the table
        c.execute("INSERT INTO numbers VALUES (?)",(num,))