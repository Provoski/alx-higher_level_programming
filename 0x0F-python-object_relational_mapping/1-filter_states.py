#!/usr/bin/python3
"""filter_state module."""
import sys
import MySQLdb
"""
this script list all states with the name starting
with N from hbtn_0e_o_usa database.
"""


if __name__ == '__main__':
    arguments = sys.argv
    username = arguments[1]
    password = arguments[2]
    database = arguments[3]
    conn = MySQLdb.connect(
            host="localhost",
            port=3306, user=username,
            password=password,
            db=database,
            charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    query = cur.fetchall()
    for row in query:
        print(row)
    cur.close()
    conn.close()
