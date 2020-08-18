
from pymongo import MongoClient


jashan = MongoClient("mongodb://localhost:27017/")
mydb = jashan['testDB']
collection = mydb['jashanpreetSingh_C0752052']

def _insert():
    try:
    
        name = input('Enter Student Name: ')
        program = input('Enter Program: ')
        city = input('Enter City: ')

        if( len(name.strip()) == 0 | len(program.strip()) == 0 | len(city.strip()) == 0 ):
            print(' \n *** Validation Error ***')
            return
    
        payload = { "name": name, "prog": program, "city": city }
        x = collection.insert_one(payload)
        print(x.inserted_id)

    except:
        print('\n ** Something went wrong, try again **')

def _update():
    name = input('Enter the student name: ')
    newName = input('PLease enter progam: ')
    newCity = input('Please enter new city: ')

    collection.update_many({"name": name}, {"$set": {"prog": newName, "city": newCity}} )
    print('Done !!')


def _read():
    try:
        name = input('PLease enter the student name: ')
        
        for doc in collection.find({"name": name}):
            print(doc)

    except:
        print('\n ** Something went wrong, try again **')
        pass
 


def _delete():
    name = input('Enter the student name: ')
    collection.delete_many({"name": name})
    print('Done !!')


while True: 
    
    print('\n *** Please add the following commands *** \n')
    print('Select C to insert, U to update, R to read, D to delete : \n')
    
    command =  input('Please enter the command: ').capitalize()
    
    if command == 'C':
        print('\n lets Insert \n')
        _insert()
    elif command == 'U':
        print('\n lets Update \n')

        _update()
    elif command == 'R':
        print('\n lets Read \n')

        _read()
    elif command == 'D':
        print('\n lets Delete \n')

        _delete()
    else:
        print('Oops, Wrong Command !! ')
    


