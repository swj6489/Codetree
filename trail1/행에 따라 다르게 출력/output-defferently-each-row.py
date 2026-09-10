n = int(input())
num = 1

for i in range(n):
    if i % 2 == 0:
        step = 1 
    else:
        step = 2
    for j in range(n):
        print(num, end=' ')
        num += step
    print()

    if i < n - 1:
        if (i + 1) % 2 == 0:
            next_step = 1  
        else: 
            next_step = 2
    num = (num - step) + next_step