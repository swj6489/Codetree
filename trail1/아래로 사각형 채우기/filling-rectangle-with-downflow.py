n = int(input())

maps = [[0] * n for _ in range(n)]
cnt = 1

for i in range(n):
    for j in range(n):
        maps[i][j] += cnt
        cnt += n
    cnt = i + 2

    
for i in maps:
    print(*i)