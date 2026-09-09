n = int(input())
cnt = 1

for y in range(n): 
    for x in range(n):
        print(cnt, end=' ')
        cnt += 1
    print()