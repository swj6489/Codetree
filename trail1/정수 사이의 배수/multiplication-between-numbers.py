A, B = map(int, input().split())

start = min(A, B)
end = max(A, B)

total_sum = 0
cnt = 0

for i in range(start, end + 1):
    if i % 5 == 0 or i % 7 == 0:
        total_sum += i
        cnt += 1  

if cnt > 0:
    average = total_sum / cnt
else:
    average = 0.0

print(f"{total_sum} {average:.1f}")