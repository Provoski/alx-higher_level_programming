#!/usr/bin/python3
"""filter_state module."""
import sys
import MySQLdb


if __name__ == '__main__':
    """
    this script list all states with the name starting
    with N from hbtn_0e_o_usa database.
    """
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
    sql = '''
            SELECT * FROM states WHERE name LIKE 'N%'
            COLLATE utf8mb3_bin
            ORDER BY id ASC
        '''

    cur.execute(sql)
    query = cur.fetchall()
    if query:
        for row in query:
            print(row)
    else:
        print()

    cur.close()
    conn.close()
