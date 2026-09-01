N = int(input())
cnt = 0

while True:
    if N != 1:
        N = N // 2
        cnt += 1
    else:
        break

print(cnt)