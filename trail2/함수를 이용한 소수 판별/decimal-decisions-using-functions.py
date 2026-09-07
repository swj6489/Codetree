a, b = map(int, input().split())


def is_prime(n):
  if n < 2:
    return False
  for i in range(2, n):
    if n % i == 0:
      return False
  return True


def get_prime_sum(a, b):
  total = 0
  for i in range(a, b + 1):
    if is_prime(i):
      total += i
  return total


print(get_prime_sum(a, b))