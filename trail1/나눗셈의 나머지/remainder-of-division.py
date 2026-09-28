a, b = map(int, input().split())

arr = [0] * b

while a > 1:
  rest = a % b  
  arr[rest] += 1  
  a = a // b  

answer = 0
for i in arr:
  answer += i ** 2

print(answer)