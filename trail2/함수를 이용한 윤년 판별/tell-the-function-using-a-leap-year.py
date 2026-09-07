y = int(input())

# Please write your code here.

def yun_year(n):
    if n % 400 == 0:
        return True
    elif n % 100 == 0:
        return False
    elif n % 4 == 0:
        return True
    else:
        return False

if yun_year(y) == True:
    print('true')
else:
    print('false')
