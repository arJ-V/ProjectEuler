'''
find the sum of primes below 2 million
for this learn about the sieve of erathostenes
imagine your array of 1-n then start "crossing" out multiples and keep going encountering a new prime each time
'''
def find_primes(n):
    prime = [True] * n
    prime[0] = prime[1] = False 
    p = 2
    while p * p < n:
        if prime[p]:
            for i in range(p * p, n, p):
                prime[i] = False  
        p += 1
    return prime


def list_iter(prime_list):
    total = 0
    for p in range(2, len(prime_list)): 
        if prime_list[p]:
            total += p
    return total


print(list_iter(find_primes(2000000)))
