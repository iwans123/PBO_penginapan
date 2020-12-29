from Connector import DBconnector
from Model import Model

class resepsionis(Model):
    def __init__(self):
        super().__init__("user",["nama","alamat","jenis_kelamin","no.telp","user","password","role_id"])
    
    def cekstatus(self):
        
        