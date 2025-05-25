#
# pickleChecker.py
#

import pickle



if __name__ == "__main__":
    
    # Read prime numbers from pickle file
    #
    cnt = 0
    pNums = pickle.load(open('primeNumbers100M.p', 'rb'))

    print('len pNums:  ', len(pNums))
    print('type pNums: ', type(pNums))

    lastKey = list(pNums.keys())[-1]
    lastValue = pNums[lastKey]
    
    print("Last key:   ", format(lastKey, ","))
    print("Last value: ", format(lastValue, ","))

    ans = input("List all key/value pairs <Y/n>? ")

    if ans in ["Y", 'y']:
        for k, v in pNums.items():
            print(k, v)

