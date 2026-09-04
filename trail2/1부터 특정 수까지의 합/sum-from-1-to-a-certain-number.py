
# Please write your code here.
def add_num(n):
    result = 0
    for i in range(1, n+1):
        result += i
    answer = result / 10
    return int(answer)

n = int(input())

print(add_num(n))
