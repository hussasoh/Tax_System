import sqlite3
from sqlite3 import Error


class Database:
    def __init__(self, db_file):
        self.__connection = None
        self.__cursor = None
        self.__db_file = db_file
        self.__initializeDatabase()
        self.__addUserTable()
        self.addUser("test", "test")
        self.addUser("test2", "test2")

    def __initializeDatabase(self):
        self.__connection = None
        try:
            self.__connection = sqlite3.connect(self.__db_file)
            self.__cursor = self.__connection.cursor()
            print(sqlite3.version)
        except Error as e:
            print(e)
            self.__initializeDatabase()

    def __addUserTable(self):
        query = "CREATE TABLE Users (id INTEGER,username TEXT NOT NULL UNIQUE,password TEXT NOT NULL " \
                "UNIQUE,PRIMARY KEY(id AUTOINCREMENT)); "

        if self.__cursor is not None:
            try:
                self.__cursor.execute(query)
                print("Table Created Successfully successfully")
            except Error as e:
                print(e)
        self.__connection.commit()

    def checkUserExists(self, username):
        queryCheck = "SELECT * FROM Users WHERE username = ?"
        exists = False
        if self.__cursor is not None:
            try:
                self.__cursor.execute(queryCheck, [username])
                rows = self.__cursor.fetchall()
                if rows is not None and len(rows) > 0:
                    exists = True
                return exists
            except Error as e:
                print(e)
                return exists

    def addUser(self, username, password):
        queryInsert = "INSERT INTO Users(username,password) VALUES (?,?)"
        if self.__cursor is not None:
            try:
                if not self.checkUserExists(username):
                    self.__cursor.execute(queryInsert, (username, password))
                    print("Added successfully")
            except Error as e:
                print(e)
        self.__connection.commit()
