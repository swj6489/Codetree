arr = list(map(int, input().split()))
result = []

for i in arr:
    if i == 0:
        break
    else:
        result.append(i)

print(*result[::-1])