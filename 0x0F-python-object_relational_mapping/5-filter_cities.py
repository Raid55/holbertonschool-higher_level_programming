#!/usr/bin/python3
""" joining two tables """

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

    cur = conn.cursor()
    cur.execute("""SELECT cities.name
                FROM cities
                JOIN states
                ON cities.state_id=states.id
                WHERE name LIKE BINARY %s
                ORDER BY cities.id ASC""", (argv[4], ))

    print (', '.join([i[0] for i in cur.fetchall()]))

    cur.close()
    conn.close()
