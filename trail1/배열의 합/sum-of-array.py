

for _ in range(4):
    arr = list(map(int, input().split()))
    result = 0
    for i in arr:
        result += i
    print(result)