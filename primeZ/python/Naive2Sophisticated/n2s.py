# n2S.py
# Naive to Sophisticated:
# Explore how to get from "Naive" to "Sophisticated" Programmatically.
#
# It seems like before we can jump from a naive algorithm to generating
# a sophisticated algorithm the machine must first learn or know foundational
# algorithms -- to have a "toolbox" to draw from.
#
import math
import time
import datetime
## import myMath

def isPrime_Naive(num):
    # Depending on the CPU and size of input number
    # this may run for a VERY-VERY-VERY long time
    #
    print("Using naive method...")
    print("num: ", format(num, ","))
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

def isPrime_Optimized(num):
    # Optimized (Sophisticated) method
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

    # Large test numbers
    lnp = 1746281808882870
    lp  = 1746281808832303
    # Manageable test number
    tstNum = 99999989

    print("tstNum: ", format(tstNum, ","))
    ans = input("Naive or Sophisticated <N/S>? ")

    start_time = time.perf_counter()
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    
    if ans in ["N", "n"]:
        retValue = isPrime_Naive(tstNum)
    elif ans in ["S", "s"]:
        retValue = isPrime_Optimized(tstNum)
    

    print("retValue: ", retValue)

    et = time.perf_counter() - start_time
    print(f"--- END: isNumberPrime.py (main): runtime: {et:.4f} seconds")
