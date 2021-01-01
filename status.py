from Model import Model
from Connector import DBconnector

class status(Model):
    def __init__(self):
        super().__init__("status",["nama_status"])