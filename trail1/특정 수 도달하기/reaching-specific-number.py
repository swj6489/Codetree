num = list(map(int, input().split()))
result = 0
mean = 0.0
cnt = 0

for i in num:
    if i >= 250:
        break
    result += i
    cnt += 1

if cnt != 0:
    mean = result / cnt
else:
    mean = 0.0

print(f'{result} {mean:.1f}')