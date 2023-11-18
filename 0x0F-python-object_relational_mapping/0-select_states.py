#!/usr/bin/python3
# This module lists all states from the database hbtn_0e_0_usa

import MySQLdb
import sys

#Define a function 
def list_states(username, password, database):
    # Create a MySQLdb connection
    db = MySQLd.connect(
        host="localhost",
        user="username",
        passwd="password",
        db="database",
        port=3306
    )
    # Create a cursor object to help execute queries
    cursor = db.connect()
    # Execute query to retrive states
    query = "SELECT * FROM states ORDER BY states.id"
    cursor.execute(query)
    # Fetch results and Display them
    states = cursor.fetchall()
    for state in states:
        print(state)
    # Close cursor and connection
    cursor.close()
    db.close

if __name__ == "__maim__":
    # Get args from command line
    username, password, database = sys.argv[1], sys.argv[2],sys.argv[3]
    # Call the Function to list states
    list_states(username, password, database)
