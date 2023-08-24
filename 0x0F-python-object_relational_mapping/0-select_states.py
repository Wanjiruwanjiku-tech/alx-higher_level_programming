#!/usr/bin/python3
"""The script that lists all states"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    """
    Create a Connection to acess the database
    """
    my_db = MySQLdb.connect(host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])
{

    """ Create a Cursor """

    myCursor = my_db.cursor()

    """ Execute the querry """
    myCursor.execute("SELECT * FROM states")

    rows = myCursor.fetchall()
    for row in rows:
        print(row)

    myCursor.close()
    my_db.close()
