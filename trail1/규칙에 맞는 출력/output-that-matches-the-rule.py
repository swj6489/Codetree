T = int(input())
# 5
start = T
# 행
for i in range(T):
    # 반복문 범위를 지정하는게 중요 range(start, end, step = 1) 증가
    # start ~ end-1 (1, 5) 1 2 3 4
    # (5, 6) 5
    # start = 4
    # (4, 6) 4 5
    # start = 3
    # (3, 6) 3 4 5
    # step -1 반대
    for j in range(start, T+1):
        print(j, end = " ")

    print()
    start -= 1