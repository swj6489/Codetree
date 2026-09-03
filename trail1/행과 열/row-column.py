A, B = map(int, input().split())

for i in range(1, A+1):
    row = [i * j for j in range(1, B+1)]
    print(*row) 