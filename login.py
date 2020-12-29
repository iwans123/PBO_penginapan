from Connector import DBconnector
from Model import Model

class login(Model):
    def __init__(self):
        super().__init__("user",["nama","alamat","jenis_kelamin","no.telp","user","password","role_id"])
    
    def username(self,inputan):
        connect = DBconnector()
        query = "SELECT username FROM user WHERE username = '%s'" %inputan
        result = connect.execute(query)
        return result