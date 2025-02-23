'''
find the difference between the square of sums and the sum of squares for natural numbers 1-100
idea: understand the formula for summnation of n and n^2 
use both to reduce runtime/calculations 
'''

def square_diff(num):
    sum_square = (num*(num+1)*(2*num + 1))/6
    square_sum = pow((num*(num+1)/2), 2)
    return (square_sum - sum_square)

print(square_diff(100))
