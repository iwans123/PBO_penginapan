from Connector import DBconnector
from transaksi import transaksi
from user import user
from kamar import kamar

class main:
    def login (inputuser,inputpassw):
        connect = DBconnector()
        query = "SELECT nama,role.nama_role FROM user JOIN role ON user.role_id = role.id WHERE username = '%s' and passw ='%s'" %(inputuser,inputpassw)
        result = connect.executeRead(query)
        if not result:
            return True
        else :
            print(result[0])
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
            kamar_id = input("\tkamar (id) : ")
            cek_in = input("\tcek_in (yyyy-mm-dd) : ")
            cek_out = input("\tcek_out (yyyy-mm-dd) : ")
            user_id = input("\tuser_id anda : ")
            print("\t===HALLO RESEPSIONIS===")
            transaksi.insert([nama,no_ktp,no_telp,alamat,kamar_id,cek_in,cek_out,user_id])
            print(input(""))
            main.menu_resepsionis()
        elif menutransaksi == 2:
            transaksi.total()
            print(input(""))
            main.menu_resepsionis()
            
        elif menutransaksi == 3:
            main.main()
            
    def menu_admin():
        print("\t===HALLO ADMIN===")
        print("\t===MENU ADMIN===")
        print("""
            1.cek data
            2.insert data
            3.update data
            4.delete data
            5.logout
            """)
        menu_admin = int(input("masukkan pilihan ADMIN : "))
        if menu_admin == 1:
            print("\t===MENU===")
            print("""
            1.data user
            2.data kamar
            3.data transaksi 
            4.kembali   
            """)
            menu_cek = int(input("masukkan pilihan data : "))
            if menu_cek == 1:
                user().read()
                print(input("PRESS ENTER TO CONTINUE"))
                main.menu_admin()
            elif menu_cek == 2:
                kamar().cekamar()
                print(input("PRESS ENTER TO CONTINUE"))
                main.menu_admin()
            elif menu_cek == 3:
                transaksi().read()
                print(input("PRESS ENTER TO CONTINUE"))
                admin.menu_admin()
            elif menu_cek == 4:
                main.menu_admin()
            else :
                print("data yang anda masukkan tidak sesuai !!!")
                print(input("\nPRESS ENTER TO CONTINUE"))
                main.menu_admin()
        elif menu_admin == 2:
            print ("\t===MENU===")
            print("""
            1.data user
            2.data kamar
            3.data transaksi
            4.kembali menu admin
            """)
            menu_insert = int(input("masukkan pilihan data : "))
            if menu_insert == 1:
                user.insert_user()
                print(input("PRESS ENTER TO CONTINUE"))
                main.menu_admin()
            elif menu_insert == 2:
                kamar.inset_kamar()
                print(input("PRESS ENTER TO CONTINUE"))
                main.menu_admin()
            elif menu_insert == 3:
                transaksi.insert_transaksi()
                print(input("PRESS ENETER TO CONTINUE"))
                main.menu_admin()
            elif menu_insert == 4:
                main.menu_admin()
            else :
                print("data yang anda masukkan tidak sesuai !!!")
                print(input("\nPRESS ENTER TO CONTINUE"))
                main.menu_admin()
        elif menu_admin == 3:
            print("\t===MENU===")
            print("""
            1.data user
            2.data kamar
            3.data transaksi
            4.kembali menu admin
            """)
            menu_update = int(input("masukkan pilihan data : "))
            if menu_update == 1:
                user.update_user()
                print(input("PRESS ENTER TO CONTINUE"))
                main.menu_admin()
            elif menu_update == 2:
                kamar.update_kamar()
                print(input("PRESS ENTER TO CONTINUE"))
                main.menu_admin()
            elif menu_update == 3:
                transaksi.update_transaksi()
                print(input("PRESS ENTER TO CONTINUE"))
                main.menu_admin()
            elif menu_update == 4:
                main.menu_admin()
            else :
                print ("\tdata yand anda masukkan tidak sesuai !!!")
                print(input("\tPRESS ENTER TO CONTINUE"))
                main.menu_admin()
        elif menu_admin ==4:
            print("\t===MENU===")
            print("""
            1.data user
            2.data kamar
            3.data transaksi 
            4.kembali menu admin
            """)
            menu_delete = int(input("masukka pilihan data : "))
            if menu_delete == 1:
                user.delete_user()
                print(input("PRESS ENTER TO CONTINUE"))
                main.menu_admin()
            elif menu_delete == 2:
                kamar.delete_kamar()
                print(input("PRESS ENTER TO CONTINUE"))
                main.menu_admin()
            elif menu_delete == 3:
                transaksi.delete_transaksi()
                print(input("PRESS ENTER TO CONTINUE"))
                main.menu_admin()
            elif menu_delete == 4:
                main.menu_admin()
            else :
                print ("\tdata yand anda masukkan tidak sesuai !!!")
                print(input("\tPRESS ENTER TO CONTINUE"))
                main.menu_admin()
                
        elif menu_admin == 5:
            main.main()
            
        else :
            print ("\tdata yand anda masukkan tidak sesuai !!!")
            print(input("\tPRESS ENTER TO CONTINUE"))
            main.menu_admin()
                
    def main():
        print("\t===LOGIN===")
        while (main.login(input("\tusername : "), input("\tpassword : "))):
            print("USERNAME DAN PASSWORD YANG ANDA MASUKKAN SALAH !!!")
            print("\t===LOGIN===")
        
main.main()