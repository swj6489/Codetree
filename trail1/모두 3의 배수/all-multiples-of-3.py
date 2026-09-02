result = True

for i in range(5):
    n = int(input())

    if n % 3 != 0:
        result = False
        break
    else:
        continue

if result:
    print('1')
else:
    print('0')
