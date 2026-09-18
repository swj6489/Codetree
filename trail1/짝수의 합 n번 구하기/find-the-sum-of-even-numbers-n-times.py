n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    even_num = 0
    for i in range(a, b+1):
        if i % 2 == 0:
            even_num += i
    
    print(even_num)
