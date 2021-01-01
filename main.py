from Connector import DBconnector
from transaksi import transaksi
from user import user
from kamar import kamar

class main:
    
    def login (inputuser,inputpassw):
        connect = DBconnector()
        query = "SELECT nama,role.nama_role FROM user JOIN role ON user.role_id = role.id WHERE username = '%s' and passw ='%s'" %(inputuser,inputpassw)
        result = connect.executeRead(query)
        print (result[0])
        if (result[0][1]) == "RESEPSIONIS":
            main.menu_resepsionis()
        elif (result[0][1]) == "ADMIN":
            main.menu_admin()
            
    def menu_resepsionis():
        print("\t\tHALLO RESEPSIONIS")
        print("\t\t===menu transaksi===")
        print ("""
            1.masukkan transaksi
            2.cek transaksi
            3.logout
            """)
        menutransaksi = int(input("masukkan pilahan transaksi : "))
        if menutransaksi == 1:
            print("\t===DAFTAR KAMAR===")
            kamar().cekamar()
            nama = input("\tnama : ")
            no_ktp = input("\tno_ktp : ")
            no_telp = input("\tno_telp : ")
            alamat = input("\talamat : ")
            print ("""
                   1.REGULER (Rp.100.000)
                   2.VIP     (Rp.300.000)
                   3.VVIP    (Rp.500.000)""")
            kamar_id = input("\tkamar (id)")
            cek_in = input("\tcek_in : ")
            cek_out = input("\tcek_out : ")
            print("\t===HALLO RESEPSIONIS===")
            transaksi.insert(["",nama,no_ktp,no_telp,alamat,kamar_id,cek_in,cek_out,user_id])
            main.menu_resepsionis()
        elif menutransaksi == 2:
            transaksi.total()
            main.menu_resepsionis()
            
        elif menutransaksi == 3:
            main.main()
            
    def menu_admin():
        print("\t===HALLO ADMIN===")
        print("""
            1.cek data
            2.insert data
            3.update data
            4.delete data
            5.logout
            """)
        menu_admin = int(input("masukkan pilihan ADMIN : "))
        print("""
            1.data user
            2.data kamar
            3.data transaksi    
            """)
        if menu_admin == 1:
            menu_cek = int(input("masukkan pilihan data : "))
            if menu_cek == 1:
                user().read()
                main.menu_admin()
            elif menu_cek == 2:
                kamar().read()
                kamar().cekamar()
                main.menu_admin()
            elif menu_cek == 3:
                transaksi().read()
                admin.menu_admin()
            else :
                print("data yang anda masukkan salah !!!")
                print(input(""))
                main.menu_admin()
        elif menu_admin == 2:
            menu_insert = int(input("masukkan pilihan data : "))
            if menu_insert == 1:
                user.insert_user()
                main.menu_admin()
            elif menu_insert == 2:
                kamar.inset_kamar()
                main.menu_admin()
            elif menu_insert == 3:
                transaksi.insert_transaksi()
                main.menu_admin()
            else :
                print("data yang anda masukkan salah !!!")
                print(input(""))
                main.menu_admin()
        elif menu_admin == 3:
            menu_update = int(input("masukkan pilihan data : "))
            if menu_update == 1:
                user.update_user()
                main.menu_admin()
            elif menu_update == 2:
                kamar.update_kamar()
                main.menu_admin()
            elif menu_update == 3:
                transaksi.update_transaksi()
                main.menu_admin()
        elif menu_admin ==4:
            menu_delete = int(input("masukka pilihan data : "))
            if menu_delete == 1:
                user.delete_user()
            elif menu_delete == 2:
                kamar().delete()
            elif menu_delet == 3:
                transaksi().delete()
                
    def main():
        print("\t===LOGIN===")
        main.login(input("\tusername : "), input("\tpassword : "))
        
main.main()
