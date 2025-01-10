#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
The script accepts 3 arguments: mysql username, mysql password, and database name.
Results are sorted by states.id in ascending order and displayed.
"""
import MySQLdb
import sys

def main():
    db = MySQLdb.connect(
        host="localhost", 
        port=3306, 
        user=sys.argv[1], 
        passwd=sys.argv[2], 
        db=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
