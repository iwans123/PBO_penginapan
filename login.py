from Connector import DBconnector
from Model import Model

class login(Model):
    def __init__(self,getTable,getColumn):
        super().__init__(getTable,getColumn)
    
    # def username(self,inputan):
    #     connect = DBconnector()
    #     query = "SELECT username FROM user WHERE username = '%s'" %inputan
    #     result = connect.execute(query)
    #     return result