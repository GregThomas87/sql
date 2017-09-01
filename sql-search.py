# SQL Search assignment
# import modules
import sqlite3

# connect to db newnum.db
with sqlite3.connect("newnum.db") as connection:
    # create cursor
    c = connection.cursor()
    
    # create dict of user commands
    commands = {
        '1': "SELECT AVG(number) FROM numbers",
        '2': "SELECT MAX(number) FROM numbers",
        '3': "SELECT MIN(number) FROM numbers",
        '4': "SELECT SUM(number) FROM numbers"
    }
    
    menu = "1. Average of numbers\n2. Maximum of numbers\n"
    menu += "3. Minimum of numbers\n4. Sum of numbers"
    # create program loop
    while(True):
        # print menu
        print(menu)
        # prompt user for a command
        prompt = input("Enter a number from the menu or '5' to quit: ")
        # quit if 5 is chosen
        if prompt == '5':
            print("Exiting...")
            # exit loop
            break
        # if number isn't 1-5 message to try again
        if prompt not in commands:
            print("Command not recognized, try again!")
        else:
            # exexcute command
            c.execute(commands[prompt])
            result = c.fetchone()[0]
            # print result to screen
            print("\nThe result is {}.\n".format(result))
    
    