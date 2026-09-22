n = int(input())
arr = list(map(int, input().split()))
num = [0] * 10

for i in arr:
    num[i] += 1

for i in num[1::]:
    print(i)
    