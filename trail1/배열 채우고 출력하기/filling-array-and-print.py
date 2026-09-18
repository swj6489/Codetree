n = list(input().split())

result = []

for i in n[::-1]:
    result.append(i)

print("".join(result))