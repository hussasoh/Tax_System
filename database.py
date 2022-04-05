import sqlite3
from sqlite3 import Error


def initializeSoftware(db_file):
    connection = None

    try:
        connection = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
        initializeSoftware(db_file)
    finally:
        if connection:
            connection.close()
