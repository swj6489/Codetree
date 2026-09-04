a, b, c = map(int, input().split())

# Please write your code here.

def low_num(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= c and b <= a:
        return b
    else:
        return c
    

print(low_num(a, b, c))

