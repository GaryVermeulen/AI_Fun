# cell1DNA.py
#

startNum = 1

# Simple function
#
def cellFunction(newNum):
    # Principal cell function using: add one
    #/START
    return newNum + 1
    #/END


# Prime number function
#
def isNumPrime1(num):
    #print("isNumPrime1: num: ", num)
    retValue = False
    # Negative numbers, 0 and 1 are not primes
    if num > 1:
        # Iterate from 2 to n // 2
        for i in range(2, (num//2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
            retValue = True
    else:
        print(num, "is not a prime number")

    return retValue
