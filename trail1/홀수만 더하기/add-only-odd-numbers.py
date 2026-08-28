N = int(input())

result = 0

for i in range(N):
    num = int(input())
    if num % 2 == 1 and num % 3 == 0:
        result += num

print(result)

