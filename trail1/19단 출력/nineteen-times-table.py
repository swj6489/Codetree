n = 19

for i in range(1, n + 1):
    cnt = 0
    for j in range(1,  n + 1):
        if j % 2 == 1:
            print(i, "*", j , "=", i * j,end='')
        else:
            print(" /", i, "*", j, '=', i * j)

        if j == 19:
            print()
        