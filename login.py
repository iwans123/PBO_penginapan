from Connector import DBconnector
from Model import Model
from transaksi import transaksi

class login(Model):
    def __init__(self):
        super().__init__("user",["nama","alamat","jenis_kelamin","no.telp","username","passw","role_id"])
    
    def username (inputuser,inputpassw):
        connect = DBconnector()
        query = "SELECT nama,role.nama_role FROM user JOIN role ON user.role_id = role.id WHERE username = '%s' and passw ='%s'" %(inputuser,inputpassw)
        result = connect.executeRead(query)
        print (result[0])
        if (result[0][1]) == "RESEPSIONIS":
            transaksi.menu_resepsionis()
        elif (result[0][1]) == "ADMIN":
            transaksi.menu_admin()