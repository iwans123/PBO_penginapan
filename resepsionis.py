from Model import Model
from Connector import DBconnector

class resepsionis(Model):
    def __init__(self):
        super().__init__("user",["nama","alamat","jenis_kelamin","no.telp","username","password","role_id"])
        

user1 = resepsionis()
user1.read()