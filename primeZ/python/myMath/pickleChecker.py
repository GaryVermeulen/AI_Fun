#
# pickleChecker.py
#

import pickle
from myMath1 import Arithmetic as pData


file_path = "data.p"

if __name__ == "__main__":
    
    # Read pickle file
    #
    cnt = 0
    pData = pickle.load(open(file_path, 'rb'))

    #print('len pData:  ', len(pData))
    print('type pData: ', type(pData))

    pData.printAll()
    print('-----')
    print(pData.basicNumberTypes)
    
    """
    lastKey = list(pNums.keys())[-1]
    lastValue = pNums[lastKey]
    
    print("Last key:   ", format(lastKey, ","))
    print("Last value: ", format(lastValue, ","))

    ans = input("List all key/value pairs <Y/n>? ")

    if ans in ["Y", 'y']:
        for k, v in pNums.items():
            print(k, v)
    """
