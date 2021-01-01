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
        transaksi().insert([nama,no_ktp,no_telp,alamat,kamar_id,cek_in,cek_out,user_id])
        
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
        transaksi().insert([nama,no_ktp,no_telp,alamat,kamar_id,cek_in,cek_out,user_id],inputanID)
    
    def delete_transaksi():
        transaksi().read()
        inputanID = int(input("masukkan id transaksi yang akan dihapus : "))
        transaksi().delete(inputanID)

    
# transaksi1 = transaksi()
# transaksi1.insert(["","iwan","123","123","TA","1","2020-12-31","2021-1-5","1"])
# transaksi1.transaksi()
# transaksi1.total()
# transaksi1.delete(2)
# transaksi.menu_resepsionis()