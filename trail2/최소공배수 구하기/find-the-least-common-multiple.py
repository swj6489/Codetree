n, m = map(int, input().split())

# Please write your code here.

def low_num(a, b):

    i = 1
    while (a * i % b != 0):
        i += 1

    print(a * i)

low_num(n, m)    
    
