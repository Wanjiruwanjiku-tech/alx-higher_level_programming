#!/usr/bin/python3

"""
The script lists all cities from the database
hbtn_0e_4_usa

Results must be sorted in ascending order by 
cities.id
"""

import MySQLdb as Mydb
from sys import argv

if __name__ == '__main__':

    """
    Create a Connection inorder to access
    the database
    """

    connection = Mydb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    """
    Create a Cursor to interact with the
    connected database
    """

    with connection.cursor() as cur:
        #Execute Query

        query = "SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"

        cur.execute(query)

        rows = cur.fetchall
        
    if rows is not None:
        for row in rows:
            print(row)
