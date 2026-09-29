n = int(input())
a = list(map(int, input().split()))
min_num = float('inf')
cnt = 0

# Please write your code here.
for i in range(len(a)):
    if min_num > a[i]:
        min_num = a[i]
        cnt = 1
    elif min_num == a[i]:
        cnt += 1

print(f'{min_num} {cnt}')