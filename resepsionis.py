from Model import Model
from Connector import DBconnector

class resepsionis(Model):
    def __init__(self):
        super().__init__("user",["nama","alamat","jenis_kelamin","no.telp","username","password","role_id"])
        
    def cekamar (self):
        connect = DBconnector()
        query = "SELECT no_kamar,kelas.nama_kelas as kelas FROM kamar JOIN kelas ON kelas.id=kamar.kelas_id"
        result = connect.execute(query)
        print (result)


user1 = resepsionis()
user1.cekamar()
# user1 = resepsionis()
# user1.read()