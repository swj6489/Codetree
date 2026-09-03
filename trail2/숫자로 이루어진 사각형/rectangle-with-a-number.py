def print_square(n):
  val = 1
  for i in range(n):
    for j in range(n):
      print(val, end=" ")
      val += 1
      if val > 9:
        val = 1
    print()


N = int(input())
print_square(N)