total_sum = 0
cnt = 0

for i in range(10):
    n = int(input())
    if 0 <= n <= 200:
        cnt += 1
        total_sum += n

avr = total_sum / cnt

print(f'{total_sum} {avr:.1f}')