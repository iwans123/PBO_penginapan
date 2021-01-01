from Model import Model
from kamar import kamar
from user import user
from Connector import DBconnector

class transaksi(Model):
    def __init__(self):
        super(). __init__("transaksi",
        ["nama","no_ktp","no_telp","alamat","kamar_id","cek_in","cek_out","user_id"])

    def total():
        connect = DBconnector()
        query = "SELECT nama,no_ktp,no_telp,alamat,kamar.no_kamar,kelas.nama_kelas,kelas.harga,DATEDIFF(cek_out,cek_in)as selisih,(DATEDIFF(cek_out,cek_in)*(kelas.harga))as TOTAL from transaksi JOIN kamar ON kamar.id = transaksi.kamar_id JOIN kelas ON kamar.kelas_id = kelas.id"
        result = connect.executeRead(query)
        # print (result)
        print("[nama][no_ktp][no_telepon][alamat][kamar][kelas][harga][waktu][total]")
        for i in range (len(result)):
            print (result[i])
    
    def insert_transaksi():
        kamar().cekamar()
        nama = input("\tnama : ")
        no_ktp = input("\tno_ktp : ")
        no_telp = input("\tno_telp : ")
        alamat = input("\talamat : ")
        kamar_id = input("\tkamar (id) : ")
        cek_in = input("\tcek_in : ")
        cek_out = input("\tcek_out : ")
        user_id = input("\tuser (id) : ")
        transaksi().insert([nama,no_ktp,no_telp,alamat,kamar_id,cek_in,cek_out,user_id])
        
    def update_transaksi():
        print("[id][nama][no_ktp][no_telp][alamat][kamar_id]        [cek_in]                        [cek_out]       [user_id]")
        transaksi().read()
        inputanID = int(input("masukkan id transaksi yang akan diupdate : "))
        nama = input("\tnama : ")
        no_ktp = input("\tno_ktp : ")
        no_telp = input("\tno_telp : ")
        alamat = input("\talamat : ")
        kamar_id = input("\tkamar (id) : ")
        cek_in = input("\tcek_in : ")
        cek_out = input("\tcek_out : ")
        user_id = input("\tuser (id) : ")
        transaksi().insert([nama,no_ktp,no_telp,alamat,kamar_id,cek_in,cek_out,user_id],inputanID)
    
    def delete_transaksi():
        inputanID = int(input("masukkan id transaksi yang akan dihapus : "))
        transaksi().delete(inputanID)

    
    # def menu_resepsionis():
    #     print("\t\tHALLO RESEPSIONIS")
    #     print("\t\t===menu transaksi===")
    #     print ("""
    #         1.masukkan transaksi
    #         2.cek transaksi
    #         3.logout
    #         """)
    #     menutransaksi = int(input("masukkan pilahan transaksi : "))
    #     if menutransaksi == 1:
    #         print("\t===DAFTAR KAMAR===")
    #         kamar().cekamar()
    #         nama = input("\tnama : ")
    #         no_ktp = input("\tno_ktp : ")
    #         no_telp = input("\tno_telp : ")
    #         alamat = input("\talamat : ")
    #         print ("""
    #                1.REGULER (Rp.100.000)
    #                2.VIP     (Rp.300.000)
    #                3.VVIP    (Rp.500.000)""")
    #         kamar_id = input("\tkamar (id)")
    #         cek_in = input("\tcek_in : ")
    #         cek_out = input("\tcek_out : ")
    #         print("\t===HALLO RESEPSIONIS===")
    #         transaksi.insert(["",nama,no_ktp,no_telp,alamat,kamar_id,cek_in,cek_out,user_id])
    #         transaksi.menu_resepsionis()
    #     elif menutransaksi == 2:
    #         transaksi.total()
    #         transaksi.menu_resepsionis()
            
            
    # def menu_admin():
    #     print("\t===HALLO ADMIN===")
    #     print("""
    #         1.cek data
    #         2.insert data
    #         3.update data
    #         4.delete data
    #         """)
    #     menu_admin = int(input("masukkan pilihan ADMIN : "))
    #     print("""
    #         1.data user
    #         2.data kamar
    #         3.data transaksi    
    #         """)
    #     if menu_admin == 1:
    #         menu_cek = int(input("masukkan pilihan data : "))
    #         if menu_cek == 1:
    #             user().read()
    #             transaksi.menu_admin()
    #         elif menu_cek == 2:
    #             kamar().read()
    #             transaksi.menu_admin()
    #         elif menu_cek == 3:
    #             transaksi().read()
    #             transaksi.menu_admin()
    #         else :
    #             print("data yang anda masukkan salah !!!")
    #             print(input(""))
    #             transaksi.menu_admin()
    #     elif menu_admin == 2:
    #         menu_insert = int(input("masukkan pilihan data : "))
    #         if menu_insert == 1:
    #             user.insert_user()
    #             transaksi.menu_admin()
    #         elif menu_insert == 2:
    #             kamar.inset_kamar()
    #             transaksi.menu_admin()
    #         elif menu_insert == 3:
    #             transaksi.insert_transaksi()
    #             transaksi.menu_admin()
    #         else :
    #             print("data yang anda masukkan salah !!!")
    #             print(input(""))
    #             transaksi.menu_admin()
    #     elif menu_admin == 3:
    #         menu_update = int(input("masukkan pilihan data : "))
    #         if menu_update == 1:
    #             user.update_user()
    #             transaksi.menu_admin()
    #         elif menu_update == 2:
    #             kamar.update_kamar()
    #             transaksi.menu_admin()
    #         elif menu_update == 3:
    #             transaksi.update_transaksi()
    #             transaksi.menu_admin()
                
                

    # def total(self):
    #     connect =DBconnector()
    #     query = "SELECT SUM(DATEDIFF(cek_out,cek_in)*kelas.harga)as TOTAL FROM transaksi JOIN kamar ON transaksi.kamar_id = kamar.id JOIN kelas ON kamar.kelas_id = kelas.id"
    #     result = connect.executeRead(query)
    #     print (result)

    
# transaksi1 = transaksi()
# transaksi1.insert(["","iwan","123","123","TA","1","2020-12-31","2021-1-5","1"])
# transaksi1.transaksi()
# transaksi1.total()
# transaksi1.delete(2)
# transaksi.menu_resepsionis()