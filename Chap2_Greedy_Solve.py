"""
이것이 코딩 테스트다 2021 강의 몰아보기
2021.04.08

Chapter 2. 그리디 문제 풀이

"""


# 1) 큰 수의 법칙 _ 내 답
# 데이터 입력 받기.
n, m, k = map(int, input().split())
nums = sorted(list(map(int, input().split())))
# 결과값 res, 숫자 세기 cnt
res = 0
cnt = 0
# m번 만큼 더해야 하므로
for i in range(m) :
    # 만약 cnt가 k와 같다면 더이상 가장 큰 숫자를 더할 수 없으므로
    if cnt == k :
        # 두번째로 큰 숫자를 더하고, cnt 초기화.
        res += nums[-2]
        cnt = 0
    # cnt가 k와 같지 않다면
    else :
        # 가장 큰 숫자를 더하고 cnt에 더하기 1.
        res += nums[-1]
        cnt += 1
print(res)





# 큰 수의 법칙 _ 답안 예시 1
# 데이터 입력 받기.
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
# 오름차순으로 정렬, 가장 큰 수와 두번째로 큰 수를 변수에 저장.
data.sort()
first = data[n - 1]
second = data[n - 2]
# 결과값 초기화.
result = 0

while True :
    # k번 더해야 하므로
    for i in range(k) :
        # 만약 m이 0이 되면 for문 탈출.
        if m == 0 :
            break
        # 결과 값에 가장 큰 수를 더하고
        result += first
        # m 에서 1을 빼준다.
        m -= 1
    # 만약 m이 0이 되면 while문 탈출.
    if m == 0 :
        break
    # 결과 값에 두번째로 큰 수를 더하고
    result += second
    # m 에서 1을 빼준다.
    m -= 1
# 출력.
print(result)





# 큰 수의 법칙 _ 답안 예시 2
# 데이터 입력받기.
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
# 데이터 정렬. 가장 큰 수와 두번째로 큰 수를 변수에 저장
data.sort()
first = data[n - 1]
second = data[n - 2]

# 가장 큰 수가 더해지는 횟수 계산
# 가장 큰 수를 k번 더하고, 두번째로 큰 수를 1번 더하는 set의 개수를 구한 뒤 * k.
# ex) 3세트 * k = 가장 큰 수가 더해지는 횟수
count = int(m / (k + 1)) * k
# 세트가 딱 나누어 떨어지지 않고 k개 미만으로 나머지가 생길 때,
# 그 나머지 횟수만큼 가장 큰 수가 더해질 것이다.
count += m % (k + 1)

result = 0
# 가장 큰 수 더하기
result += count * first
# 두번째로 큰 수 더하기
result += (m-count) * second

print(result)





# 2) 숫자 카드 게임 _ 내 답
n, m = map(int, input().split())
# 가장 작은 카드들을 보관할 리스트
small = []
for i in range(n) :
    card = map(int, input().split())
    # 각 행에서 가장 작은 카드를 small에 추가한다.
    small.append(min(card))
# 가장 작은 카드들중 제일 큰 카드를 출력.
print(max(small))





# 숫자 카드 게임 _ 답안 예시 1
n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    # 각 행마다 가장 작은 카드를 변수에 저장.
    min_value = min(data)
    # 결과값 = 기존에 있던 가장 작은 카드와 새로 저장된 가장 작은 카드 중 큰 수.
    result = max(result, min_value)

print(result)





# 숫자 카드 게임 _ 답안 예시 2
n, m = map(int, input().split())
result = 0

for i in range(n) :
    data = list(map(int, input().split()))
    # 10000이 최대값이므로 가장 작은 값을 10001로 설정.
    # 첫번째 for문에서 무조건 카드의 가장 작은 값이 min_value에 들어가도록.
    min_value = 10001
    for a in data :
        min_value = min(min_value, a)
    # 이전 가장 작은 값 vs. 지금 가장 작은 값 중 더 큰 것을 결과값에 저장.
    # ex) 처음 result는 0이므로 무조건 지금 가장 작은 값이 저장된다.
    result = max(result, min_value)

print(result)





