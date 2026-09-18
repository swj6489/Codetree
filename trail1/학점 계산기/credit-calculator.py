n = int(input())
grade = list(map(float, input().split()))
result = 0

for i in grade:
    result += i

mean = result / len(grade)

if mean >= 4.0:
    print(f'{mean:.1f}')
    print('Perfect')

elif mean >= 3.0:
    print(f'{mean:.1f}')
    print('Good')

else:
    print(f'{mean:.1f}')
    print('Poor')


