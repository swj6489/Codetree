N = int(input())

for i in range(N):
    for j in range(N-1,-1,-1):
        print(j+1, end=' ')
    print()