#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """
import mysql.connector
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':

    # make a connection to the database
    db = mysql.connector.connect(
        host="new-mysql-container",  # Use the MySQL container name as the host
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )

    # It gives us the ability to have multiple separate working environments
    # through the same connection to the database.
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()
    for i in rows:
        print(i)
    # Clean up process
    cur.close()
    db.close()
