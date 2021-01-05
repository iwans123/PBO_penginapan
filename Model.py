from Connector import DBconnector
from prettytable import from_db_cursor


class Model:
    def __init__(self,table,column):
        self.table = table
        self.column = column

    def read(self):
        connect = DBconnector()
        query = "SELECT * from " +self.table
        result = connect.executeRead(query)
        for i in result:
            print (i)
        
    def insert(self,values):
        connect = DBconnector()
        query = "INSERT INTO "+self.table+" ("
        for column in self.column:
            query += column+","
        query = query[:-1]
        query += ") VALUES ("
        for val in values:
            query += "'"+val+"',"
        query = query [:-1]
        query += ")"
        connect.execute(query)
        print ("\t***INSERT BERHASIL***")

    def update(self, values, inputanID):
        connect = DBconnector()
        query = "UPDATE "+self.table+" SET "
        for i in range(len(self.column)):
            query += self.column[i]+"="
            query += "'"+values[i]+"',"
        query = query [:-1]
        query += " WHERE id ='%d'" %(inputanID)
        connect.execute(query)
        print ("\t***UPDATE BERHASIL***")

    def search(self, values):
        connect = DBconnector()
        query = "SELECT * from "+self.table+" WHERE "
        for i in range (len(self.column)):
            query += self.column[i]+" LIKE '%"+values+"%' OR "
        query = query[:-3]
        connect.execute(query)
        
    def delete(self, inputanID):
        connect = DBconnector()
        query = "DELETE FROM "+self.table+" WHERE id = '%d'" % (inputanID)
        connect.execute(query)
        print("\t***DELETE BERHASIL***")