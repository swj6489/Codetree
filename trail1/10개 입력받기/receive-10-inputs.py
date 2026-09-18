arr = list(map(int, input().split()))
total = 0
cnt = 0

for i in arr:
    if i == 0:
        break
    else:
        total += i
        cnt += 1

mean = total / cnt

print(f'{total} {mean:.1f}')