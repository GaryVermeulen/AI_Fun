# isNumberPrime.py
#
import math
import time
import datetime

def isNumPrime1(num):
    # Depending on the CPU and size of input number
    # this may run for a VERY-VERY-VERY long time
    #
    print("Using naive method...")
    print("num: ", num)
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

def isNumPrime2(num):
    # Optimized method
    print("Using optimized method...")
    print("num : ", num)

    if num <= 1:
        return False

    if num == 2 or num == 3:
        return True

    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i <= math.sqrt(num):
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True


if __name__ == "__main__":
    
    start_time = time.perf_counter()
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    
#    inputNumber = 1746281808882870
#    inputNumber = 1746281808832303
    inputNumber = 8832303

    retValue = isNumPrime1(inputNumber)
    

    print("retValue: ", retValue)

    et = time.perf_counter() - start_time
    print(f"--- END: isNumberPrime.py (main): runtime: {et:.4f} seconds")
