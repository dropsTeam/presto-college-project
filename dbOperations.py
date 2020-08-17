from pymongo import MongoClient
import bcrypt

class dbOperations:
    
    def __init__(self):
        super().__init__()

        connection = MongoClient('localhost:27017')
        self.__db = connection['teamdatabase']
        self.__userCollection = self.__db['users']


    def isUserExist(self, passportNumber, isAdmin):
        return self.__userCollection.count({"passportNumber": passportNumber, "isAdmin": isAdmin}, { limit: 1 }) != 0


    def findUser(self, passportNumber, isAdmin):
        return self.__userCollection.find_one({"passportNumber": passportNumber, "isAdmin": isAdmin})
    
    
    
    def loginAdmin(self, passportNumber, password): 
        
        if (isUserExist(passportNumber, True)):
            user = self.findUser(passportNumber, True)
            if bcrypt.checkpw(password, user["password"]):
                return True
            else:
                return False
        else: 
            return False
    

    
    def registerAdmin(self, userName, password, address, passportNumber, country, email, contact):
         
        if( isUserExist(passportNumber, True) ): 
            raise Exception("User Already exist, try with diffent passport number.")
        else:
            hashed = bcrypt.kdf( password= password, salt='salt', desired_key_bytes=32, rounds=100)
            self.__userCollection.insert_one({"userName": userName, "password": hashed, "isAdmin": True, "balance": 0, "address": address, "country": country, "passportNumber": passportNumber, "email": email, "contact": contact})
    
    
    def addUser(self, userName, address, balance, country, passportNumber, email, contact):
        
        if( isUserExist(passportNumber, False) ): 
            raise Exception("User Already exist, try with different passport number.")
        else:
            self.__userCollection.insert_one({"userName": userName, "isAdmin": False, "balance": balance, "address": address, "country": country, "passportNumber": passportNumber, "email": email, "contact": contact})
    

    def addFunds(self, passportNumber):
        
        if isUserExist(passportNumber, False):
            return True
