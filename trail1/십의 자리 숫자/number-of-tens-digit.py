arr = list(map(int, input().split()))
num = [0] * 10
result = []

for i in range(len(arr)):
    if arr[i] == 0:
       break
    else:
        result.append(arr[i] // 10)

for i in result:
    num[i] += 1

for i in range(len(num))[1::]:
    print(f'{i} - {num[i]}')