from pymongo import MongoClient
import bcrypt

class dbOperations:
    
    def __init__(self):
        super().__init__()

        connection = MongoClient('localhost:27017')
        self.__db = connection['teamdatabase']
        self.__userCollection = self.__db['users']

        if( len(self.__userCollection.find({"isAdmin": True})) == 0 ):
            self.registerAdmin("Sagara Samarawickrama","12345", "Address not added", "P00000", "Canada", "abc@gmail.com", 123456789)
            



    def isUserExist(self, passportNumber, isAdmin):
        return self.__userCollection.count({"passportNumber": passportNumber, "isAdmin": isAdmin}, { limit: 1 }) != 0


    def findUser(self, passportNumber, isAdmin):
        return self.__userCollection.find_one({"passportNumber": passportNumber, "isAdmin": isAdmin})
    
    
    
    def loginAdmin(self, passportNumber, password): 
        
        if (self.isUserExist(passportNumber, True)):
            user = self.findUser(passportNumber, True)
            if bcrypt.checkpw(password, user["password"]):
                return True
            else:
                return False
        else: 
            return False
    

    
    def registerAdmin(self, userName, password, address, passportNumber, country, email, contact):
        
        if len(password) < 5:
            raise Exception("Password should be atleast 5 char long")
        elif( self.isUserExist(passportNumber, True) ): 
            raise Exception("User Already exist, try with diffent passport number.")
        else:
            hashed = bcrypt.kdf( password= password, salt='salt', desired_key_bytes=32, rounds=100)
            self.__userCollection.insert_one({"userName": userName, "password": hashed, "isAdmin": True, "balance": 0, "address": address, "country": country, "passportNumber": passportNumber, "email": email, "contact": contact})
    
    
    def addUser(self, userName, address, balance, country, passportNumber, email, contact):
        
        if( self.isUserExist(passportNumber, False) ): 
            raise Exception("User Already exist, try with different passport number.")
        else:
            self.__userCollection.insert_one({"userName": userName, "isAdmin": False, "balance": balance, "address": address, "country": country, "passportNumber": passportNumber, "email": email, "contact": contact})
    

    def addFunds(self, passportNumber, balance):
        
        if self.isUserExist(passportNumber, False):
            self.__userCollection.update_one({"passportNumber": passportNumber}, { "$inc":{ "balance": balance } });
        else:
            raise Exception("User not found!")
    
    
    def editUser(self, passportNumber, userName, address, balance, country, email, contact):
        
        if self.isUserExist(passportNumber):
            self.__userCollection.update_one({"passportNumber": passportNumber}, {"userName": userName, "balance": balance, "address": address, "country": country, "email": email, "contact": contact})
        else:
            raise Exception("User Not found!")

    def getAllUsers(self):
        return self.__userCollection.find({"isAdmin": False})

    def getAllAdmin(self):
        return self.__userCollection.find({"isAdmin": True})