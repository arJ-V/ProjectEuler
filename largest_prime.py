'''
find the largest prime factor from n
iteratign through all ints from 1 to floor(sqrt(n)) allows us to compute all possible factors,
from here we can iterate using the same function to find which ones have ony 2 factors
'''



import math
def factor(num):
    factor_list = []
    n = math.isqrt(num) # kind of taking the easy way out with basically floor(sqrt(num)) could also make your own function
    
    for i in range(1, n + 1):  
        if num % i == 0:  
            factor_list.append(i)
            if i != num // i:  
                factor_list.append(num // i)

    return factor_list


def prime_factors(num):
    factors = factor(num)
    my_primes = []

    for n in factors:
        if len(factor(n)) == 2: 
            my_primes.append(n)

    return my_primes




print(prime_factors(600851475143))
