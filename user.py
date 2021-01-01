from Model import Model
from Connector import DBconnector

class user(Model):
    def __init__(self):
        super().__init__("user",["nama","alamat","jenis_kelamin","no_telp","username","passw","role_id"])
        
    def insert_user():
        nama = input("nama : ")
        alamat = input("alamat : ")
        jeni_kelamin = input("jenis kelamin : ")
        no_telp = input("no_telp : ")
        username = input("username : ")
        passw = input("password : ")
        role_id = input("1.ADMIN / 2.RESEPSIONIS \t : ")
        user().insert([nama,alamat,jeni_kelamin,no_telp,username,passw,role_id])
        
    def update_user():
        inputanID = int(input("masukkan id user yang akan di update : "))
        nama = input("nama : ")
        alamat = input("alamat : ")
        jeni_kelamin = input("jenis kelamin : ")
        no_telp = input("no_telp : ")
        username = input("username : ")
        passw = input("password : ")
        role_id = input("1.ADMIN / 2.RESEPSIONIS \t : ")
        user().update([nama,alamat,jeni_kelamin,no_telp,username,passw,role_id],inputanID)
        
# user1 = resepsionis()
# user1.read()