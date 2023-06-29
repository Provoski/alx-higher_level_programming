#!/usr/bin/python3
"""4-citie_by_state module."""
import sys
import MySQLdb


if __name__ == '__main__':
    """
    this script list all cities with the state they belong
    from hbtn_0e_4_usa database.
    """

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

    sql = '''
    SELECT cities.name FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name = %s ORDER BY cities.id ASC
    '''
    cur.execute(sql, (state,))
    query = cur.fetchall()
    listLenght = len(query)
    count = 0
    if (query):
        for row in query:
            count = count + 1
            for city in row:
                if count < listLenght:
                    print("{}".format(city), end=", ")
                else:
                    print("{}".format(city))
    else:
        print()

    cur.close()
    conn.close()
