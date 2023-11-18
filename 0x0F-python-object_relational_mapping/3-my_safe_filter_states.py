#!/usr/bin/python3
"""
This module executes a script that is safe from code injections.
The script takes in args and displays all values in the states table.
"""
import MySQLdb
import sys

def safe_filter(username, password, database, stateName):
    """
    the function will help execute a query safe from code injection.
    the function takes in four parameters:
    username = MySQL username,
    password = MySQL password,
    database = MySQL database,
    stateName = the state name searched.
    """
    # Create a connection
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database
    )
    # Create a cursor object to execute commands
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    # Execute query
    cursor.execute(query, (stateName,))
    # Fetchall rows
    states = cursor.fetchall()
    for state in states:
        print(state)
    
    # Close cursor and connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    username, password, database, stateName = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    safe_filter(username, password, database, stateName)