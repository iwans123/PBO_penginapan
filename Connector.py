import mysql.connector
from mysql.connector import Error

class DBconnector():
    def __init__(self):
    self.db = mysql.connector.connect(
        host="localhost",
        database="penginapan",
        username="root",
        password=""
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

# class DBconnect:
#     def __init__(self):
#         self.db = mysql.connector(
#             host="localhost",
#             database="penginapan",
#             username="root",
#             password=" "
#         )
#         self.cursor = self.db.cursor()

#     def read(self):
#         query = "SELECT * from "+self.tabel
#         cursor.execute(query)
#         results = cursor.fetchall()

#         if cursor.rowcount < 0:
#             print("Tidak ada data")
#         else:
#             for data in results:
#                 print (data)

#         read()
        
#     # def executeInsert(self,query):
#     #     try:
#     #         if self.db.is_connected():
#     #             cursor.execute(query)
#     #             self.db.commit()
#     #             print("berhasil")
#     #     except Error as e:
#     #         print(e)
        