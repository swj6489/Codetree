score = list(map(int, input().split()))
arr = []
cnt_arr = [0] * 11


for i in range(len(score)):
    if score[i] == 0:
        break
    else:
        arr.append(score[i] // 10)

for i in arr:
    cnt_arr[i] += 1

for i in range(10, 0, -1):
    print(f'{i * 10} - {cnt_arr[i]}')