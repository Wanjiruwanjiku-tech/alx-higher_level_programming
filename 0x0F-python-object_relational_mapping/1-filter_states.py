#!/usr/bin/python3
"""
The script lists all the states in the 
specified database that begin with
N (uppercase)
"""
# Import the required Modules

import MySQLdb
import sys

if __name__ == '__main__':

    # Create a Connection
    connection = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    """
    Create a cursor to interact with the 
    database
    """
    cur = db.cursor()

    # Execute the query
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"

    cur.execute(query)

    """
    Fetch the rows returned by the querry and
    have them displayed
    """

    rows = cur.fetchall()
    for row in rows:
        print(row)
