#!/usr/bin/python3
""" listing cities by states """
import sys
import MySQLdb

if __name__ == "__main__":
    with MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            host='localhost',
            port=3306,
    )as conn:
        cur = conn.cursor()
        query = """ SELECT c.id, c.name, s.name
                    FROM states as s, cities as c
                    WHERE c.state_id = s.id
                    ORDER BY c.id ASC
                """
        cur.execute(query)
        cities = cur.fetchall()
        for city in cities:
            print(city)
        cur.close()
