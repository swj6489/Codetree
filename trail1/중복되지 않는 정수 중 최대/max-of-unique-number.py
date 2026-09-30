n = int(input())
nums = list(map(int, input().split()))
arr = [0] * 1001

for i in nums:
    arr[i] += 1

max_unique = -1

for i in range(len(arr) - 1, -1, -1):
    if arr[i] == 1:
        max_unique = i
        break
print(max_unique)
