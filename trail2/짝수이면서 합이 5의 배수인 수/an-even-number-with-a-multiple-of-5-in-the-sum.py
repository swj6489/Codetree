n = int(input())

# Please write your code here.

def calculator():
    if n % 2 == 0 and ((n // 10) + (n % 10)) % 5 == 0:
        return print('Yes')
    else:
        return print('No')

calculator()