arr = [0] * 4

for i in range(3):
    cold, temp = input().split()
    temp = int(temp)
    if cold == 'Y' and temp >= 37:
        arr[0] += 1
    elif cold == 'N' and temp >= 37:
        arr[1] += 1
    elif cold == 'Y' and temp < 37:
        arr[2] += 1
    else:
        arr[3] += 1


if arr[0] >= 2:
     arr.append('E')

for i in arr:
    print(i,end=' ')
       
    



