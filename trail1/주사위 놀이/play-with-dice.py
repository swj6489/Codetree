arr = list(map(int, input().split()))
dice = [0] * 7

for i in arr:
    dice[i] += 1

for i in range(1, 7):
    print(f'{i} - {dice[i]}')