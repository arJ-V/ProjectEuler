''' 
find the largest palindrome number from 2, 3 digit numbers
Observation the greatest number possible from the product of 2 n digit numbers is 2n 
So, we can automatically cut our search down by understanding this property. 
My attempt is more "brute force" by educated guessing that there should be some combiantion of 9XX * 9XX that would result in the largest 
The PE solution observing the factor of 11 is a great idea but is not necessarily more efficient
'''

def flip_num(num):
    flipped = int(str(num)[::-1])
    return flipped


def find_palindrome():
    result = 0
    greatest = 0
    flag = False
    for i in range(900, 1000):
        for n in range(900, 1000):
            if (i*n) == flip_num(i*n):
                result = i*n
                if result > greatest:
                    greatest = result
    return greatest
        

print(find_palindrome())
