 from pymongo import MongoClient
import bcrypt

class dbOperations:
    
    def __init__(self):
        super().__init__()

        connection = MongoClient('localhost:27017')
        self.__db = connection['teamdatabase']
        self.__userCollection = self.__db['users']
    

    def findUser(self, passportNumber, isAdmin):
        return self.__userCollection.find_one({"passportNumber": passportNumber, "isAdmin": isAdmin})
    
    
    def loginAdmin(self, passportNumber, password): 
        user = self.findUser(passportNumber, True)
        
        if bcrypt.checkpw(password, user["password"]):
            return True
        else:
            return False
    

    def registerAdmin(self, userName, password, address, passportNumber, country):
         
        if(self.__userCollection.count({"passportNumber": passportNumber, "isAdmin": True}, { limit: 1 }) != 0): 
            raise Exception("User Already exist, try with diffent passport number.")
        else:
            hashed = bcrypt.kdf( password= password, salt='salt', desired_key_bytes=32, rounds=100)
            self.__userCollection.insert_one({"userName": userName, "password": hashed, "isAdmin": True, "balance": 0, "address": address, "country": country, "passportNumber": passportNumber})
    
    def addUser(self, userName, address, balance, country, passportNumber):
        
        if(self.__userCollection.count({"passportNumber": passportNumber, "isAdmin": False}, { limit: 1 }) != 0): 
            raise Exception("User Already exist, try with different passport number.")
        else:
            self.__userCollection.insert_one({"userName": userName, "isAdmin": False, "balance": balance, "address": address, "country": country, "passportNumber": passportNumber})