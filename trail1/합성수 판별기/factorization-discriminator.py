N = int(input())
cnt = 0

for i in range(2, N):
    if N % i == 0:
        cnt += 1
        break
    else:
        continue

if cnt == 1:
    print('C')
else:
    print('N')
