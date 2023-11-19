#!/usr/bin/python3
"""
The Module runs a script that takes in the name of a state as an arg and
lists all cities of that state
the script connects to a MySQL server running on localhost on port 3306
"""
import MySQLdb
import sys

def list_cities_by_state(username, password, database, stateName):
    """
    The function takes 4 args:
    username = mysql username,
    password = mysql password.
    database = myql database name,
    stateName = name to be searched 
    should be SQL Injection free
    """
    # Create a connection
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )
    cursor = db.cursor()
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """

    cursor.execute(query, (stateName,))
    # Fetch 
    results = cursor.fetchall()
    print(", ".join(city[0] for city in results))

    cursor.close()
    db.close()

if __name__ == "__main__":
    username, password, database, stateName = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    list_cities_by_state(username, password, database, stateName)
