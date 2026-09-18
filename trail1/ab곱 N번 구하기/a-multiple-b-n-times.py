n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    cnt = 1

    for j in range(a, b+1):
        cnt *= j

    print(cnt)