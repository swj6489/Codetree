n = int(input())
arr= list(map(int, input().split()))

lst1 = []

for i in range(n):
    for j in range(n):
        if arr[j] - arr[i] > 0:
            lst1.append(arr[j] - arr[i])

print(min(lst1))   
