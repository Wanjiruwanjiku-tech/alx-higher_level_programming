#!/usr/bin/python3
"""
The script takes in an argument and displays 
all values in the states table of 
hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb as Mydb
import sys

def main():
    """
    The main function that contains the core
    logic of the script
    """

    #Retrive Credentials 
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    searchName = sys.argv[4]

    #Create a connection

    connection = Mydb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    #create a cursor

    cur = db.cursor()

    querry = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY state.id".format(searchName)

    cur.execute(querry)

    #fetch rows

    rows = cur.fetchall()
    for row in rows:
        print(row)

if __name__ == '__main__':
    main()
