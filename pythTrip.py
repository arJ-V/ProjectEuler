'''
find the pythagorean triple where a+b+c = 1000
triple are a < b < c
but a^2 + b^2 = c^2
This is more of the brute force method 
'''

def find_Pythag():
    goal = 1000
    flag = False
    for i in range(1,1001):
        for n in range (i+1, 1001):
            if (i+n >= 1000):
                break
            if ((pow(i, 2)+ pow(n, 2)) == (pow((1000 - n - i), 2))):
                flag = True
                save = (i, n, 1000 - n -i)
                break
        if flag:
            break
    return save





print(find_Pythag())
