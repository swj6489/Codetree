n = int(input())

for i in range(1, n+1):
    result = []
    for j in range(1, n - i + 2):
        result.append(f"{i} * {j} = {i*j}")


    print(" / ".join(result))