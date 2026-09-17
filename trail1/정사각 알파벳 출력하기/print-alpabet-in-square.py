n = int(input())
cnt = 'A'

for i in range(1, n+1):
    for j in range(n):
        print(cnt ,end ='')
        cnt = chr(ord(cnt) + 1)
    print()