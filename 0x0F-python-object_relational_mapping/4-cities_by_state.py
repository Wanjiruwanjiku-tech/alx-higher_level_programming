#!/usr/bin/python3
"""
This Module runs a script that lists all cities in a database
The script takes 3 args and orders cities by cities_id in ASC
"""
import MySQLdb
import sys

def list_cities(username, password, database):
    """
    The function takes 3 parameters, including:
    username = MySQL username,
    password = MySQL password,
    database = The database name
    """
    # Create a Connection
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )
    # Create a cursor object and execute commands
    cursor = db.cursor()

    query = "SELECT cities.id, cities.name, states.name FROM cities \
        JOIN states ON cities.state_id = states.id \
            ORDER BY cities.id ASC"
    cursor.execute(query)
    # Fetch all cities in the rows
    cities = cursor.fetchall()
    for city in cities:
        print(city)
    # Close cursor and connection
    cursor.close()
    db.close()

if __name__ =="__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    list_cities(username, password, database)
