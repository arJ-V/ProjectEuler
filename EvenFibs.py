''' 
Find the sum of even fibs for n below 4,000,000
idea: brute force is fine but to optimize look at paritiies
Proposition observe sequence of parities (when parities = then eve) thus a sequence of odd odd will return even so odd odd even and so forth

Thus every 3rd will be even 
'''
def fibeven():
    prev = 1
    curr = 1
    other = 2
    total = 0 
    limit =  4000000# 
    
    # While the next Fibonacci number is less than 4,000,000
    while curr < limit:
        total += other
        prev = curr + other
        curr = prev + other
        other = prev + curr
    return total

print(fibeven())
