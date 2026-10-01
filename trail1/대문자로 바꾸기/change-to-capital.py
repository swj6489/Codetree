result = []
for _ in range(5):
    arr = list(input().split())
    for i in arr:
        result.append(i.upper())
    print(*result)
    result = []