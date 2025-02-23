'''
find the 100001st prime 
going to be computationally heavy regardless but optimize
primes are odd besides 2 
only one prime factor greater than sqrt of current number 
'''
import math

def no_multiples(primes, num):
    for prime in primes:
        if prime > math.sqrt(num):  # Optimization: Only check up to sqrt(num)
            break
        if num % prime == 0:
            return False  # num is divisible, so it's not prime
    return True  # num is prime

def primes(target):
    prime_array = [2]  # Start with 2 
    number = 3  #
    
    while len(prime_array) < target:
        if no_multiples(prime_array, number):
            prime_array.append(number)
        number += 2  #skip evens
    
    return prime_array[-1]  # Return the last prime found

print(primes(10001))

