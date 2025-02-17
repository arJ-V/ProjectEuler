'''
Find the sum of all mutliples of 3 or 5 below 1000
inclusion/exclusion be careful about mutual multiples
'''

target = 999

def sum_multiples(num):
    n = target // num
    total = num*(n*(n+1))/2
    return total

final_total = sum_multiples(3) + sum_multiples(5) - sum_multiples(15)


print(final_total)
