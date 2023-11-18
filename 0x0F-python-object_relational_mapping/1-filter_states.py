#!/usr/bin/python3
"""
This Module runs a script that filters the states printed and Lists all states
startin with uppercase N
"""
import MySQLdb
import sys

def filter_states(username, password, database):
    """
    This Function will help us Filter the States and get the desired results.
    It takes 3 parameters;
    username = MySQL username
    password = MySQL password
    database = MySQL database
    """
    # Create a connection
    db = MySQLdb.connect(
    host="localhost",
    user=username,
    passwd=password,
    db=database,
    port=3306
    )
    # Create a cursor object and execute querry
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name=N"
    cursor.execute(query)
    # Fetch all rows and Display them
    states = cursor.fetchall()
    for state in states:
        print(state)
    
    # Close cursor and connection
    cursor.close()
    db.close()
if __name__ == "__main__":
    username, password, database = sys.argv[1],sys.argv[2], sys.argv[3]
    filter_states(username, password, database)