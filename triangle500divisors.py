'''
For the "triangular numbers" which is basically the number found from adding up the sequence of real numbers from 1 - some value
find the triangular number with 500 divisors
Some optimizations: checking till sqrt n, formual for summnation derives to n(n+1)/2 as such one will be odd and even (you can prove this quite easily with cases), 
'''
import math

# Function to count divisors using trial division
def count_divisors(num):
    count = 0
    sqrt_n = int(math.sqrt(num))
    for i in range(1, sqrt_n + 1):
        if num % i == 0:
            count += 2 if i * i != num else 1  # Count both i and num/i
    return count

# Function to find the first triangular number with over 500 divisors
def find_triangular_with_500_divisors():
    n = 1
    while True:
        tri_num = n * (n + 1) // 2  # Compute nth triangular number
        if n % 2 == 0:
            divisors = count_divisors(n // 2) * count_divisors(n + 1)
        else:
            divisors = count_divisors(n) * count_divisors((n + 1) // 2)

        if divisors > 500:
            return tri_num

        n += 1

print(find_triangular_with_500_divisors())
