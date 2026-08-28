A , B = map(int, input().split())
cnt = 0

if B > A:
    for i in range(A , B+1):
        if i % 5 == 0:
            cnt += i
else:
    for i in range(B, A+1):
        if i % 5 == 0:
            cnt += i
print(cnt)