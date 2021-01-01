from Connector import DBconnector
from kamar import kamar
from login import login


def main():
    print("\t===LOGIN===")
    login.username(input("\tusername : "), input("\tpassword : "))
    
main()