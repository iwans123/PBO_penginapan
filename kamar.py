from Model import Model
from Connector import DBconnector

class kamar(Model):
    def __init__(self):
        super(). __init__("kamar",
        ["no_kamar","status_id","kelas_id"])

    def cekamar (self):
        connect = DBconnector()
        query = "SELECT no_kamar,kelas.nama_kelas as kelas FROM kamar JOIN kelas ON kelas.id=kamar.kelas_id"
        result = connect.executeRead(query)
        print (result)


# kamar1 = kamar()
# kamar1.cekamar()

# kamar1 = kamar()
# kamar1.read()
# kamar1.insert(["A03","2","1"])
# Model.insert("A02","2","1")
