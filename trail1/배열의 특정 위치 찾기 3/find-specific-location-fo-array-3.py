arr = list(map(int, input().split()))
result = 0

for i in range(len(arr)):
    if arr[i] == 0:
        result = arr[i-1] + arr[i-2] + arr[i-3]
        break

print(result)