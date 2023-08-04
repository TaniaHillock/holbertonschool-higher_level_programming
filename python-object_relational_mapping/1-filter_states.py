#!/usr/bin/python3
"""
db_connection will stablish the connection with the data base.
cursor creates a cursor to interact with the data base
cursor_leng shows the number of items that the object contains
list_1 converts the object into an iterable list

"""
import sys
import MySQLdb
if __name__ == "__main__":
    db_connection = MySQLdb.connect(host="localhost", port=3306,
                                    user=sys.argv[1], passwd=sys.argv[2],
                                    db=sys.argv[3])
    cursor = db_connection.cursor()
    cursor_leng = cursor.execute("SELECT * FROM states ORDER BY states.id")
    list_1 = list(cursor)
    for item in range(0, cursor_leng):
        if list_1[item][1][0] == 'N':
            print(list_1[item])
