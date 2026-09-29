N, Q = map(int, input().split())

# 1번 인덱스부터 편하게 쓰기 위해 앞에 0 추가 (1-indexed 맞춤)
arr = [0] + list(map(int, input().split()))

for _ in range(Q):
  lst1 = list(map(int, input().split()))
  cmd = lst1[0]

  # 1번 질의: a번째 원소 출력
  if cmd == 1:
    a = lst1[1]
    print(arr[a])

  # 2번 질의: 값이 b인 원소 중 가장 작은 인덱스 찾기 (없으면 0)
  elif cmd == 2:
    b = lst1[1]
    found = 0
    for i in range(1, N + 1):
      if arr[i] == b:
        found = i
        break  # 가장 작은 인덱스를 찾아야 하므로 첫 발견 시 탈출
    print(found)

  # 3번 질의: s번째부터 e번째 원소까지 출력
  elif cmd == 3:
    s, e = lst1[1], lst1[2]
    print(*arr[s : e + 1])