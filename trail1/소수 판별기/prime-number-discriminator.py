N = int(input())
result = True

for i in range(2, N):
    if N % i == 0:
        result = False
        break
    else:
        continue

if result:
    print('P')
else:
    print('C')