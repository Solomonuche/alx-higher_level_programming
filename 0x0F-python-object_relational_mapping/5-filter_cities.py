#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument and
lists all cities of that state
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
You must use format to create the SQL query with the user input
"""


import MySQLdb as DB
from sys import argv

if __name__ == "__main__":
    connect = DB.connect(user=argv[1], passwd=argv[2], db=argv[3],
                         host="localhost", port=3306)
    cur = connect.cursor()

    my_query = "SELECT DISTINCT cities.name \
                FROM cities INNER JOIN states \
                ON cities.state_id = states.id \
                WHERE states.name LIKE BINARY %s"

    cur.execute(my_query, (argv[4],))
    rows = cur.fetchall()

    if rows:
        for i in range(len(rows)):
            for item in rows[i]:
                if i < (len(rows) - 1):
                    print(item, end=", ")
                else:
                    print(item)
    else:
        print()

    """clean up"""
    cur.close()
    connect.close()
