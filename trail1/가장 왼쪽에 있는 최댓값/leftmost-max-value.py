n = int(input())
arr = list(map(int, input().split()))

# 탐색을 시작할 오른쪽 끝 인덱스 (처음에는 맨 끝인 n - 1)
end = n - 1

while True:
    # 현재 범위 [0, end]에서 최댓값과 그 위치(인덱스) 찾기
    max_val = -1
    max_idx = 0

    for i in range(end + 1):
        # '>' 연산을 사용하여 값이 같더라도 '가장 먼저(왼쪽에서)' 나온 최댓값을 유지합니다.
        if arr[i] > max_val:
            max_val = arr[i]
            max_idx = i

    # 1-indexed 기준으로 위치 출력 (문제에서 첫 번째 원소는 1번 위치를 의미)
    print(max_idx + 1,end=' ')

    # 뽑힌 위치가 첫 번째 원소(인덱스 0)라면 과정 종료
    if max_idx == 0:
        break

    # 다음 탐색 범위는 방금 구한 최댓값 위치의 바로 왼쪽까지로 제한
    end = max_idx - 1