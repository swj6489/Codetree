n = int(input())
cnt = 0

for i in range(n):
    total = 0
    s1,s2,s3,s4 = map(int, input().split())
    total = s1 + s2 + s3 + s4 
    
    if total / 4 >= 60:
        print('pass')
        cnt += 1
    else:
        print('fail')

    
print(cnt)