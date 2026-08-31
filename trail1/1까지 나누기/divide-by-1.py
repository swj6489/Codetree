N = int(input())
k = N
cnt = 0

for i in range(1, N+1):
    k = k // i
    cnt += 1

    if k <= 1:
        break


print(cnt)