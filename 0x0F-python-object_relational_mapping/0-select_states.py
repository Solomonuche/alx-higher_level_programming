#!/usr/bin/python3
from sys import argv
import MySQLdb as DB

"""
a script that lists all states from the database hbtn_0e_0_usa
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
"""
username = argv[1]
password = argv[2]
db_name = argv[3]

connect = DB.connect(host="localhost", port=3306, user=username,
                     passwd=password, db=db_name)
cur = connect.cursor()
cur.execute("SELECT id, name FROM states ORDER by states.id ASC")
rows = cur.fetchall()

for row in rows:
    print(row)

"""clean up"""
cur.close()
connect.close()
