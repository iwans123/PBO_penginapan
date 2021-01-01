from Model import Model
from status import status
from Connector import DBconnector

class kamar(Model):
    def __init__(self):
        super(). __init__("kamar",
        ["no_kamar","status_id","kelas_id"])

    def cekamar (self):
        connect = DBconnector()
        query = "SELECT no_kamar,kelas.nama_kelas as kelas,kelas.harga,status.nama_status FROM kamar JOIN kelas ON kelas.id=kamar.kelas_id JOIN status ON status.id = kamar.status_id"
        result = connect.executeRead(query)
        # print (result)
        for i in range (len(result)):
            print(result[i])
            
    def inset_kamar():
        no_kamar = input("no kamar : ")
        status().read()
        status_id = input("status (id) : ")
        kelas_id = input("kelas (id) : ")
        kamar().insert([no_kamar,status_id,kelas_id])
        
    def update_kamar():
        inputanID = int(input("masukkan id kamar yang akan diupdate : "))
        no_kamar = input("no kamar : ")
        status().read()
        status_id = input("status (id) : ")
        kelas_id = input("kelas (id) : ")
        kamar().update([no_kamar,status_id,kelas_id],inputanID)


# kamar1 = kamar()
# kamar1.cekamar()

# kamar1 = kamar()
# kamar1.read()
# kamar1.insert(["A03","2","1"])
# Model.insert("A02","2","1")
