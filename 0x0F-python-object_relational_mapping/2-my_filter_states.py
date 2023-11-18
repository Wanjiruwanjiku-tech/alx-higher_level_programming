#!/usr/bin/python3
"""
This Module runs a script that Displays states according to the provided argument
"""
import MySQLdb
import sys

def filter_my_state(username, password, database, stateName);
    """
    The function displays states according to the provided command line arg
    the function take four parameter:
    username = MySQL username,
    password = MySQL password,
    database = Mysql database,
    stateName = The statename searched
    """
    db = MySQLdb.connect(
        host="localhost"
        user=username,
        passwd=password,
        db=database,
        name=stateName,
        port=3306
    )
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name=stateName"
    cursor.execute(query)
    cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()

if __name__ == "__main__":
    username, password, database, stateName = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    filter_my_state(username, password, database, stateName)