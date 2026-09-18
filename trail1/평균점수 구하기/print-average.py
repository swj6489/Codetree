student = list(map(float, input().split()))
result = 0.0

for i in student:
    result += i

print(f'{result / len(student):.1f}')