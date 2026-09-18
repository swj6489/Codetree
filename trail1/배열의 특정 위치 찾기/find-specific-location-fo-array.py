arr = list(map(int, input().split()))
even_total = 0
total = 0
cnt = 0 

for i in range(len(arr)):
    turn = i + 1 
    

    if turn % 2 == 0:
        even_total += arr[i]
    
    if turn % 3 == 0:
        total += arr[i]
        cnt += 1

print(f'{even_total} {total / cnt:.1f}')