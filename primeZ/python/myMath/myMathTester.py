# myMathTester.py
#
from myMath1 import Arithmetic as arith
import os
import sys
import pickle
import inspect
import pymongo
from pymongo.errors import ConnectionFailure
import socket


file_path = "data.p"

def connectMongo():
    myClient = None
    if socket.gethostname() == 'pop-os':
        try:
            # Home server
            #myclient = pymongo.MongoClient("mongodb://10.0.0.20:27017")
            myClient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
            myClient.admin.command('ping')
            print("MongoDB is running and reachable.")
        except ConnectionFailure:
            sys.exit("MongoDB is not running or reachable, exit.")
        except Exception as e:
            sys.exit(f"An error occured: {e}; exit.")
    else:
        print("Unrecognized OS: ", socket.gethostname())
    return myClient

def isPickle():
    if os.path.exists(file_path):
        print(f"The file '{file_path}' exists.")
        return True
    print(f"The file '{file_path}' does not exist.")
    return False

def loadPickle():
    existingData = None
    with open(file_path, 'rb') as pf:
        existingData = pickle.load(pf)
        pf.close()
    return existingData

def savePickle(obj):
    if obj == None:
        print("No data to save to pickle: ", a)
    else:
        with open(file_path, 'wb') as pf:
            pickle.dump(obj, pf)
            pf.close()
    return

if __name__ == "__main__":

    # Initialization
    if not isPickle():
        print("use new pickle data")
        arithObj = arith()
        # This is not efficient, need to change into rules
        arithObj.setN({1,2,3,5,5,6,7,8,9})
        arithObj.setN0({0,1,2,3,5,5,6,7,8,9})
        arithObj.setZ({-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9})
        
        arithObj.setAdditionSymbol('+')

        arithObj.printAll()
        print("-----")

        ans = arithObj.myAdd(-3, 4)

        print(ans)
    else:
        print("use existing pickle data")
        arithObj = loadPickle()
        arithObj.printAll()

        ans = arithObj.myAdd(-9, 2)
        print(ans)
        print("---")
        print(arithObj.myAdd(arithObj.simpleAdd(10, 2), 3))

    # Emulate actions
    print('==========')
    arithDict = arithObj.getAll()
    print(arithDict)
    print('=====')
    arithObj.setSubtractionSymbol('-')
    arithObj.setMultiplicationSymbol('*')
    arithObj.setDivisionSymbol('/')

    print("Simple Add: -9 + 2 = ")
    print(arithObj.simpleAdd(-9, 2))
    
    print("Is Natural: ", 0)
    print(arithObj.isNatural("0"))

    print("What Is X: ", 0)
    print(arithObj.whatIsX(0))

    print("Add new: setattr:") 
    setattr(arith, 'basicNumberTypes', ['Natural'])

    print('=====')
    arithDict = arithObj.getAll()
    print(arithDict)
    
    print('-----')
    arithObj.printAll()

    print('-----')
    print(arithObj.basicNumberTypes)
    print('=====')

    # Get a list of methods using inspect module
    methods_list = [method[0] for method in inspect.getmembers(
    arithObj, predicate=inspect.ismethod)]

    print(methods_list)

    print("Saving data to pickle...")
    savePickle(arithObj)
    
    print("Saving data to Mongo...")
    arithDict = arithObj.getAll()
    print(arithDict)
    if len(arithDict) < 1:
        print("Nothing to save to MongoDB.")
    else:
        mdb = connectMongo()
        simpDB = mdb["simp"]
        simpMath = simpDB["simpMath"]
        simpMath.drop()
        for line in arithDict:
            if isinstance(arithDict[line], set):
                simpMath.insert_one({line: list(arithDict[line])})
            else:
                simpMath.insert_one({line: arithDict[line]})
    """
        Saving the object is nice, but...
            Will need to modify the original class in myMath1
    """
    print("END.")
