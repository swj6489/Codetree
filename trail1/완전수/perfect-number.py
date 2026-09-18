start, end = map(int, input().split())

perfect_num = 0  # 완전 수 카운팅 변수
# Please write your code here.

# 본인을 제외한 약수의 총합이 본인의 값이랑 같다 -> 완전수

for i in range(start, end + 1):
    cnt = 0  # 완전 수랑 같은 지 확인하는 변수
    for j in range(1, i):  # 본인 값 제외해야하므로 i+1이 아닌 i
        if i % j == 0:
            cnt += j

    if i == cnt:
        perfect_num += 1

print(perfect_num)