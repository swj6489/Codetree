N = int(input())
lst1 = []

for i in range(N):
    num = int(input())
    if num % 2 == 1 and num % 3 == 0:
        lst1.append(num)

for j in lst1:
    print(j)