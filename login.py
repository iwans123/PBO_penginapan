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
            # print("\tHALLO RESEPSIONIS")
            # print("\t===transaksi===")
            # menutransaksi = input("""
            #       1.masukkan transaksi
            #       2.cek transaksi
            #       """)
            # if menutransaksi == 1:
            #     transaksi1.insert(nama,no_telp,no_ktp,alamat,kamar_id,cek_in_cek_out,user_id)
            # elif menutransaksi ==2:
            #     transaksi1.read()
        elif (result[0][1]) == "ADMIN":
            transaksi.menu_admin()