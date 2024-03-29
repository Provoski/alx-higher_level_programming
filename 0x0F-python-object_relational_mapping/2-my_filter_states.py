#!/usr/bin/python3
"""2-my_filter_state module."""
import sys
import MySQLdb


if __name__ == '__main__':
    """
    this script list all states matching the state name
    argument from hbtn_0e_o_usa database.
    """

    arguments = sys.argv
    username = arguments[1]
    password = arguments[2]
    database = arguments[3]
    state_name = arguments[4]
    conn = MySQLdb.connect(
            host="localhost",
            port=3306, user=username,
            password=password,
            db=database,
            charset="utf8")
    cur = conn.cursor()

    sql = '''
        SELECT * FROM states WHERE name = '{}'
        COLLATE utf8mb3_bin
        ORDER BY id ASC
        '''
    sql_format = sql.format(state_name)
    cur.execute(sql_format)
    query = cur.fetchall()
    if query:
        for row in query:
            print(row)
    else:
        print()

    cur.close()
    conn.close()
