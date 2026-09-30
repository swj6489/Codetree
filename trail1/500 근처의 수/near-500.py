arr = list(map(int, input().split()))
max_n = float('-inf')
min_n = float('inf')

for i in arr:
    if i < 500:
        if i > max_n: 
            max_n = i

    elif i > 500:
        if i < min_n: 
            min_n = i

print(max_n, min_n)