lst1 = [list(map(int, input().split())) for _ in range(3)]
input()
lst2 = [list(map(int, input().split())) for _ in range(3)]

result = [[0] * 3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        result[i][j] = lst1[i][j] * lst2[i][j]
    
for i in range(3):
    for j in range(3):
        print(result[i][j], end=' ')
    print()
