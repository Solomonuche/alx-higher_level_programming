#!/usr/bin/python3
import MySQLdb as DB

"""
a script that lists all states from the database hbtn_0e_0_usa
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
"""

connect = DB.connect(user="root", passwd="", db="hbtn_0e_0_usa")
cur = connect.cursor()
cur.execute("SELECT id, name FROM states ORDER by states.id ASC")
rows = cur.fetchall()

for row in rows:
    print(row)

"""clean up"""
connect.close()
cur.close()
