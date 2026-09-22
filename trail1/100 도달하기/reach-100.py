n = int(input())

arr = [1, n]

while True:
    if arr[-1] > 100:
        break
    arr.append(arr[-1] + arr[-2])

print(*arr)