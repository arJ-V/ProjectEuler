'''
find the smallest positive number evenly divisible by numbers 1-20
tldr smallest mult 1-20
use prime factorization
for each prime find the closest power such <= target 
'''
import math

def lcm():
    primes  = [2, 3, 5, 7, 11, 13, 17, 19]  
    k = 20 
    total = 1
    
    for prime in primes:
        power = math.floor(math.log(k) / math.log(prime))  # Find highest exponent within range
        total *= pow(prime, power)

    return total

print(lcm())
