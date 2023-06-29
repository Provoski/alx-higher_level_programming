#!/usr/bin/python3
"""select_state module"""
import sys
import MySQLdb


if __name__ == '__main__':
    """select_state module"""

    arguments = sys.argv
    username = arguments[1]
    password = arguments[2]
    database = arguments[3]

    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            password=password,
            db=database,
            charset="utf8"
            )
    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query = cur.fetchall()
    for row in query:
        print(row)

    cur.close()
    conn.close()
