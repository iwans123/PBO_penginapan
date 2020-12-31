from Connector import DBconnector
from Model import Model

class login(Model):
    def __init__(self):
        super().__init__("user",["nama","alamat","jenis_kelamin","no.telp","username","passw","role_id"])
    
    def username (inputuser,inputpassw):
        connect = DBconnector()
        query = "SELECT username,passw FROM user WHERE username = '%s' and passw ='%s'" %(inputuser,inputpassw)
        result = connect.executeRead(query)
        print (result)