from Connector import DBconnector
from Model import Model

class kelas(Model):
    def __init__(self):
        super(). __init__("kelas",
                          ["nama_kelas","harga"])
    