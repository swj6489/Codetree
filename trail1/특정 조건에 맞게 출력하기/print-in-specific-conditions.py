arr = list(map(int, input().split()))
result = []

for i in range(len(arr)):
    if arr[i] == 0:
        break

    elif arr[i] % 2 == 1:
        result.append(arr[i] + 3)
    else:
        result.append(arr[i] // 2)
    
print(*result)