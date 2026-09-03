N = int(input())

for x in range(N-1,-1,-1):
    for y in range(N-1,-1,-1):
        print(f'({x+1},{y+1})',end=' ')
    print()