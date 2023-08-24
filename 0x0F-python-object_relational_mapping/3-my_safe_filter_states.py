#!/usr/bin/python3

"""
The script takes in arguments and displays all
values in the states table of hbtn_0e_0_us

where name matches the argument. But this time
one that is safe from MySQL injections!
"""

import MySQLdb as Mydb
from sys import argv

if __name__ == '__main__':

    """
    Create a connection to Access the 
    database, retrieve the comand line args
    Create a cursor and Execute Query
    """

    conection = Mydb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    cur = connection.cursor()

    #Execute the query

    cur.execute("SELECT * FROM states WHERE name LIKE \ BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})

    """
    Fetch all rows returned by the query and
    have them displayed
    """
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    connection.close()
