# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/
#
# SieveOfEratosthenes2.py
# Modified for my usage: gary7v@gmail.com; 25, May, 2025

import time
import datetime
import pickle

from cell1DNA import isNumPrime1

pickleFile = 'primeNumbers.p'

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}
    
    # The running integer that's checked for primeness
    q = 2
    ##q = 0 
    
    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        
        q += 1
        

if __name__ == "__main__":
    """
    Reference: Names of large numbers using short scale
        1,000,000         one million  Take less than a second.
        1,000,000,000     one billion  Takes about 14-15 minutes (depending on CPU).
        1,000,000,000,000 one trillion Out of scope.
    """

    start_time = time.perf_counter()
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("--- Start: SieveOfEratosthenes2.py (main):")
    print("Current Time =", current_time)

    count = 1
    limit = 100000000
    resultDict = {}

    print("limit: ", format(limit, ","))
    
    for num in gen_primes():
        if num > limit:
            break
        
        #print(count, num)
        resultDict.update({count: num}) 
        count +=1

    print("length of resultDict: ", len(resultDict))
    lastKey = list(resultDict.keys())[-1]
    lastValue = resultDict[lastKey]
    print("Last key: ", format(lastKey, ","))
    print("Last value: ", format(lastValue, ","))

    et = time.perf_counter() - start_time
    print(f"--- gen_primes(): runtime: {et:.4f} seconds")

    # Save output to pickle
    print('Saving list of prime numbers to pickle...')
    with open(pickleFile, "wb") as pf:
        pickle.dump(resultDict, pf)
        
    #for i in range(1, 120):
    #    isNumPrime1(i)

    et = time.perf_counter() - start_time
    print(f"--- END: SieveOfEratosthenes2.py (main): runtime: {et:.4f} seconds")
    print("END")
