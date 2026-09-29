arr= list(map(int, input().split()))
result = 0

for i in range(len(arr)):
    if arr[i] > result:
        result = arr[i]

print(result)