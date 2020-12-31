from Model import Model
from Connector import DBconnector

class transaksi(Model):
    def __init__(self):
        super(). __init__("transaksi",
        ["id","nama","no_ktp","no_telp","alamat","kamar_id","cek_in","cek_out","user_id"])

    def transaksi(self):
        connect = DBconnector()
        query = "SELECT nama,no_telp,no_ktp,alamat,kamar.no_kamar,kelas.nama_kelas,kelas.harga,SUM(DATEDIFF(cek_out,cek_in)*kelas.harga)as TOTAL from transaksi JOIN kamar ON kamar.id = transaksi.kamar_id JOIN kelas ON kamar.kelas_id = kelas.id"
        result = connect.executeRead(query)
        print (result)

    # def total(self):
    #     connect =DBconnector()
    #     query = "SELECT SUM(DATEDIFF(cek_out,cek_in)*kelas.harga)as TOTAL FROM transaksi JOIN kamar ON transaksi.kamar_id = kamar.id JOIN kelas ON kamar.kelas_id = kelas.id"
    #     result = connect.executeRead(query)
    #     print (result)

    
transaksi1 = transaksi()
# transaksi1.insert(["","iwan","123","123","TA","1","2020-12-31","2021-1-5","1"])
# transaksi1.transaksi()
# transaksi1.total()
# transaksi1.delete(2)