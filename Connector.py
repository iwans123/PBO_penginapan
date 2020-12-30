import mysql.connector
from mysql.connector import Error

class DBconnector():
    def __init__(self):
        self.db = mysql.connector.connect(
            host = "127.0.0.1",
            port = "3306",
            database = "penginapan",
            user = "root",
            password = ""
        )

    def execute(self, query):
        try:
            if self.db.is_connected():
                cursor = self.db.cursor()
                cursor.execute(query)
                self.connection.commit()
        except Error as e:
            print (e)

    def executeRead(self, query):
        try:
            if self.db.is_connected():
                cursor = self.db.cursor()
                cursor.execute(query)
                record = cursor.fetchall()
                return record
        except Error as e:
            print (e)