def max_num():
    for i in range(min(n,m), -1, -1):
        if n % i == 0 and m % i == 0:
            print(i)
            break

n, m = map(int, input().split())
max_num()