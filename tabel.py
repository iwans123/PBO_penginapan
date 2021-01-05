from Model import Model
from Connector import DBconnector
import datetime

class user(Model):
    def __init__(self):
        super().__init__("user",["nama","alamat","jenis_kelamin","no_telp","username","passw","role_id","record"])
        
    def insert_user():
        tgl = datetime.date.today().strftime('%Y-%m-%d')
        nama = input("nama : ")
        alamat = input("alamat : ")
        jeni_kelamin = input("jenis kelamin (L/P): ")
        no_telp = input("no_telp : ")
        username = input("username : ")
        passw = input("password : ")
        role_id = input("1.ADMIN / 2.RESEPSIONIS \t : ")
        user().insert([nama,alamat,jeni_kelamin,no_telp,username,passw,role_id,tgl])
        
    def update_user():
        tgl = datetime.date.today().strftime('%Y-%m-%d')
        print("\t===DAFTAR USER===")
        user().read()
        inputanID = int(input("masukkan id user yang akan di update : "))
        nama = input("nama : ")
        alamat = input("alamat : ")
        jeni_kelamin = input("jenis kelamin (L/P): ")
        no_telp = input("no_telp : ")
        username = input("username : ")
        passw = input("password : ")
        role_id = input("1.ADMIN / 2.RESEPSIONIS \t : ")
        user().update([nama,alamat,jeni_kelamin,no_telp,username,passw,role_id,tgl],inputanID)
        
    def delete_user():
        user().read()
        inputanID = int(input("masukkan id user yang akan dihapus : "))
        user().delete(inputanID)
        
class kamar(Model):
    def __init__(self):
        super(). __init__("kamar",
        ["no_kamar","status_id","kelas_id"])

    # def update_statusada(id_kamar):
    #     connect = DBconnector()
    #     query = "SELECT no_kamar,kelas_id FROM kamar WHERE id ='%d'" %(id_kamar)
    #     result = connect.executeRead(query)
    #     kamar().update([(result[0][0]),1,(result[0][1])],id_kamar)

    def cekamar (self):
        connect = DBconnector()
        query = "SELECT kamar.id,no_kamar,kelas.nama_kelas as kelas,kelas.harga,status.nama_status FROM kamar JOIN kelas ON kelas.id=kamar.kelas_id JOIN status ON status.id = kamar.status_id WHERE status.id = 2 ORDER BY no_kamar"
        result = connect.executeRead(query)
        print("[id][no_kamar][kelas][harga][status]")
        for i in range (len(result)):
            print(result[i])
            
    def inset_kamar():
        kamar().cekamar()
        no_kamar = input("no kamar : ")
        status().read()
        status_id = input("status (id) : ")
        kelas().read()
        kelas_id = input("kelas (id) : ")
        kamar().insert([no_kamar,status_id,kelas_id])
        
    def update_kamar():
        kamar().read()
        inputanID = int(input("masukkan id kamar yang akan diupdate : "))
        no_kamar = input("no kamar : ")
        status().read()
        status_id = input("status (id) : ")
        kelas().read()
        kelas_id = input("kelas (id) : ")
        kamar().update([no_kamar,status_id,kelas_id],inputanID)
        
    def delete_kamar():
        kamar().cekamar()
        inputanID = int(input("masukkan id kamar yang akan dihapus : "))
        kamar().delete(inputanID)

class kelas(Model):
    def __init__(self):
        super(). __init__("kelas",
                          ["nama_kelas","harga"])

class status(Model):
    def __init__(self):
        super().__init__("status",["nama_status"])

class transaksi(Model):
    def __init__(self):
        super(). __init__("transaksi",
        ["nama","no_ktp","no_telp","alamat","kamar_id","cek_in","cek_out","user_id"])

    def total():
        connect = DBconnector()
        query = "SELECT nama,no_ktp,no_telp,alamat,kamar.no_kamar,kelas.nama_kelas,kelas.harga,transaksi.cek_out,DATEDIFF(cek_out,cek_in)as selisih,(DATEDIFF(cek_out,cek_in)*(kelas.harga))as TOTAL from transaksi JOIN kamar ON kamar.id = transaksi.kamar_id JOIN kelas ON kamar.kelas_id = kelas.id"
        result = connect.executeRead(query)
        print("[nama][no_ktp][no_telepon][alamat][kamar][kelas][harga][cek_out][waktu][total]")
        for i in range (len(result)):
            print (result[i])
    
    def insert_transaksi():
        # id_kamar = []
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
        # id_kamar.append(kamar_id)
        transaksi().insert([nama,no_ktp,no_telp,alamat,kamar_id,cek_in,cek_out,user_id])
        # kamar().update_statusada((id_kamar))
        
        
    def update_transaksi():
        print("\t\t===DAFTAR TRANSAKSI===")
        print("[id][nama][no_ktp][no_telp][alamat][kamar_id]        [cek_in]                        [cek_out]       [user_id]")
        transaksi().read()
        inputanID = int(input("masukkan id transaksi yang akan diupdate : "))
        nama = input("\tnama : ")
        no_ktp = input("\tno_ktp : ")
        no_telp = input("\tno_telp : ")
        alamat = input("\talamat : ")
        kamar().cekamar()
        kamar_id = input("\tkamar (id) : ")
        cek_in = input("\tcek_in (yyyy-mm-dd) : ")
        cek_out = input("\tcek_out (yyyy-mm-dd) : ")
        user_id = input("\tuser_id anda : ")
        transaksi().update([nama,no_ktp,no_telp,alamat,kamar_id,cek_in,cek_out,user_id],inputanID)
    
    def delete_transaksi():
        transaksi().read()
        inputanID = int(input("masukkan id transaksi yang akan dihapus : "))
        transaksi().delete(inputanID)