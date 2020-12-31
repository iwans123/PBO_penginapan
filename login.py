from Connector import DBconnector
from Model import Model

class login(Model):
    def __init__(self):
        super().__init__("user",["nama","alamat","jenis_kelamin","no.telp","username","passw","role_id"])
    
    def username (inputuser,inputpassw):
        connect = DBconnector()
        query = "SELECT nama,role.nama_role FROM user JOIN role ON user.role_id = role.id WHERE username = '%s' and passw ='%s'" %(inputuser,inputpassw)
        result = connect.executeRead(query)
        # print(result)
        print (result[0])
        if (result[0][1]) == "RESEPSIONIS":
            print("\tHALLO RESEPSIONIS")
        elif (result[0][1]) == "ADMIN":
            print("\tHALLO ADMIN")