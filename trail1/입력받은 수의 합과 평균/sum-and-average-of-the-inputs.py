N = int(input())
total_num = 0
cnt = 0


for i in range(1, N+1):
    num = int(input())
    cnt += 1
    total_num += num

average = total_num / cnt

print(f'{total_num} {average:.1f}')

