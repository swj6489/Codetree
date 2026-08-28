A, B = map(int, input().split())

while True:
    print(A, end=' ')

    if A % 2 != 0:
        A *= 2
    else:
        A += 3

    if A > B:
        break