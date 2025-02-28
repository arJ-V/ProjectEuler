'''
find the longest collatz sequence under 1 million
collatz
for n if n is even n = n/2
if odd, n = 3n + 1
A nice optimization is using memoization, basically creating a hashmap of prrevious numbers and their associated sequence count
'''
def collatz(num, cache):
    if num in cache:
        return cache[num]

    if num == 1:
        return 1

    if num % 2 == 0:
        next_num = num // 2
    else:
        next_num = 3 * num + 1

    cache[num] = 1 + collatz(next_num, cache)  # Store computed result
    return cache[num]

def find_greatest():
    cache = {}  # Dictionary to store computed Collatz sequence lengths
    most_collatz = 0
    most_num = 0

    for num in range(1000000, 700000, -1):  # Iterate in descending order
        current_collatz = collatz(num, cache)

        if current_collatz > most_collatz:
            most_collatz = current_collatz
            most_num = num

    return most_num

print(find_greatest())
