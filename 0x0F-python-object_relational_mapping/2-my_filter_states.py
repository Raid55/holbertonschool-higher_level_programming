#!/usr/bin/python3
""" filter some states that are in arg with format """

import MySQLdb
from sys import argv


if __name__ == "__main__":

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    query = """SELECT id, name
            FROM states
            WHERE name LIKE BINARY '{}'
            ORDER BY id ASC"""

    cur = conn.cursor()
    cur.execute(query.format(argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
