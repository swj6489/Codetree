n1, n2 = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

is_subsequence = False

# A에서 B의 길이만큼 잘라내어 비교할 수 있는 시작점(i)을 순회합니다.
for i in range(n1 - n2 + 1):
  # A의 i번째부터 B의 길이(n2)만큼 잘라낸 조각이 B와 완전히 일치하는지 확인
  if arr_a[i : i + n2] == arr_b:
    is_subsequence = True
    break

# 연속 부분 수열이면 1, 아니면 0 출력 (문제 요구사항에 맞게 출력)
if is_subsequence:
  print('Yes')
else:
  print('No')