#!/usr/bin/python3
import sys
import MySQLdb
"""
4-citie_by_state module.
this script list all cities with the state they belong
from hbtn_0e_4_usa database.
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
            charset="utf8"
    )
    cur = conn.cursor()

    sql = '''
    SELECT cities.id, cities.name, states.name FROM cities
    INNER JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    '''
    cur.execute(sql)
    query = cur.fetchall()
    for row in query:
        print(row)
    cur.close()
    conn.close()
