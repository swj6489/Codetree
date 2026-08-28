N = int(input())
num = 0

for i in range(1, N):
    if N % i == 0:
        num += i
        
if N == num:
    print('P')
else:
    print('N')