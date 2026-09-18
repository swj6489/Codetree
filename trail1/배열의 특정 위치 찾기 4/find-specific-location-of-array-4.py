arr = list(map(int, input().split()))
total = 0
cnt = 0

for i in arr:
    if i == 0:
        break

    else:
        if i % 2 == 0:
            total += i
            cnt += 1

print(cnt, total)