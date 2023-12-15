#!/usr/bin/python3
"""
a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
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
    my_query = "SELECT id, name FROM states \
                WHERE states.name LIKE %s \
                ORDER by states.id ASC"
    cur.execute(my_query, (argv[4],))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    """clean up"""
    cur.close()
    connect.close()
