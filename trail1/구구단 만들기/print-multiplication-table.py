A, B = map(int, input().split())

start = max(A, B)   # 큰 값부터
end = min(A, B)     # 작은 값까지

for j in range(1, 10):         # 곱하는 수 1부터 9까지
    parts = []
    k = start
    while k >= end:          
        parts.append(f"{k} * {j} = {k * j}")
        k -= 2
    print(" / ".join(parts))
