n = int(input())
arr = list(map(int, input().split()))

result = [arr[i] ** 2 for i in range(len(arr))]

print(*result)
