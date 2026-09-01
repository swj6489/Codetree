result = 0.0
cnt = 0
while True:
    n = int(input())
    if n >= 30 or n < 20:
        break
    
    result += n
    cnt += 1

average = result / cnt

print(f'{average:.2f}')
    