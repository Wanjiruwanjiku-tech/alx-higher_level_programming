#!/usr/bin/python3
"""
The script that lists all states from 
the database hbtn_0e_0_usa:
- The script should take 3 arguments 
- You must use the module MySQLdb
- Your script should connect to a MySQL 
server running on localhost at port 3306
- Results must be sorted in ascending 
order by states.id
"""

import MySQLdb
import sys

if __name__ = '__main__':

    """
    Create a Connection to acess the database
    """
    my_db = MySqldb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    """ Create a Cursor """

    myCursor = db.cursor()

    """ Execute the querry """
    myCursor.execute("SELECT * FROM states")

    rows = myCursor.fetchall()
    for row in rows:
        print row
