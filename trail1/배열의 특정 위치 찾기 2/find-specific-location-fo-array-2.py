arr = list(map(int, input().split()))
odd = 0
even = 0

for i in range(1, len(arr)+1):
    if i % 2 == 1:
        odd += arr[i-1]
    else:
        even += arr[i-1]

if odd > even:
    print(odd - even)
else:
    print(even-odd)