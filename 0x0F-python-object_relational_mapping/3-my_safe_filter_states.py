#!/usr/bin/python3
import sys
import MySQLdb
"""
2-my_filter_state module.
this script list all states matching the state name
argument from hbtn_0e_o_usa database.
it prevente sql injection
"""


if __name__ == '__main__':
    arguments = sys.argv
    username = arguments[1]
    password = arguments[2]
    database = arguments[3]
    state = arguments[4]
    conn = MySQLdb.connect(
            host="localhost",
            port=3306, user=username,
            password=password,
            db=database,
            charset="utf8"
    )
    cur = conn.cursor()
    sql = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    cur.execute(sql, (state,))
    query = cur.fetchall()
    for row in query:
        print(row)
    cur.close()
    conn.close()
