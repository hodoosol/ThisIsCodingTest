"""
이것이 코딩 테스트다 2021 강의 몰아보기
2021.04.07

Chapter 2. 그리디 & 구현
2. 구현

"""


"""
1. 구현(Implementation)이란 ?
머리 속에 있는 알고리즘을 소스코드로 바꾸는 과정.
구현 문제란 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제를 뜻한다.
 - 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제
 - 실수 연산을 다루고, 특정 소수점까지 출력해야하는 문제
 - 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
 - 적절한 라이브러리를 찾아서 사용해야 하는 문제
 
일반적으로 알고리즘 문제에서의 2차원 공간은 행렬의 의미로 사용된다.
시뮬레이션 및 완전 탐색 문제에서는 2차원 공간에서의 방향 벡터가 자주 활용된다.

#### 동, 북, 서, 남 
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0] 으로 표현할 수 있다.


"""





"""
# 상하좌우 : 문제 설명

여행가 a는 n * n 크기의 정사각형 공간 위에 서있다.
이 공간은 1 * 1 크기의 정사각형으로 나누어져 있고 
가장 왼쪽 위 좌표는 (1, 1), 가장 오른쪽 아래 좌표는 (n, n)이다.
여행가 a는 상 하 좌 우 방향으로 이동할 수 있으며 시작 좌표는 항상 (1, 1)이다.
우리 앞에는 여행가 a가 이동할 계획이 적힌 계획서가 놓여있다.

계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 
L, R, U, D 중 하나의 문자가 반복적으로 적혀있다.
 - L : 왼쪽으로 한 칸 이동
 - R : 오른쪽으로 한 칸 이동
 - U : 위쪽으로 한 칸 이동
 - D : 아래로 한 칸 이동
 
이 때, 여행가 a가 n * n 크기의 정사각형 공간을 벗어나는 움직임은 무시된다.
예를 들어 (1, 1)의 위치에서 L 혹은 U를 만나면 무시된다.
 

"""



# 상하좌우 _ 내 답
n = int(input())
plan = input().split()

x = y = 1

for i in plan :
    if x > 1 :
        if i == 'L' :
            x -= 1
    if x < n :
        if i == 'R' :
            x += 1
    if y > 1 :
        if i == 'U' :
            y -= 1
    if y < n :
        if i == 'D' :
            y += 1

print(y, x)



# 상하좌우 _ 답안 예시
# 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()
# L, R, U, D에 따른 이동 방향
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
move_types = ['L', 'R', 'U', 'D']
# 이동 계획을 하나씩 확인하기
for plan in plans :
    # 이동 후 좌표 구하기
    for i in range(len(move_types)) :
        if plan == move_types[i] :
            nx = x + dx[i]
            ny = y + dy[i]
     # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n :
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)





"""
# 시각 : 문제 설명
정수 n이 입력되면 00시 00분 00초부터 N시 59분 59초까지의
모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.

예를 들어 1을 입력했을 때 다음은 3이 하날도 포함되어 있으므로 세어야하는 시각이다.
 - 00시 00분 03초
 - 00시 13분 30초
 
반면에 3이 하나도 포함되어 있지 않다면 세면 안된다.
 - 00시 02분 55초
 - 01시 27분 45초
 
 
"""



# 시각 _ 내 답
n = int(input())
res = 0
# 0부터 59까지 3이 들어가는 모든 경우의 수 15개를 초로 설정하고,
# 3이 들어가지 않는 분 * 3이 들어가는 초와 3이 들어가는 분 * 모든 초 60
# 두 개를 더한 것이 시에 3이 들어가지 않을 때 세어야 하는 모든 경우의 수이다.
not_3 = (15 * 45) + (60 * 15)

for i in range(n + 1) :
    # 만약 시에 3이 들어간다면 모든 초를 세어야하므로 60 * 60을 더해준다.
    if i == 3 or i == 13 or i == 23 :
       res += 60 * 60
    # 시에 3이 들어가지 않는다면 not_3를 더해준다.
    else :
        res += not_3

print(res)





# 시각 _ 답안 예시
h = int(input())

count = 0
for i in range(h + 1) :
    for j in range(60) :
        for k in range(60) :
            #매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k) :
                count += 1
print(count)





"""
# 왕실의 나이트 : 문제 설명
8 * 8 좌표 평면상에서 나이트의 위치가 주어졌을 때 
나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오.
왕실의 정원에서 행 위치를 표현할 때는 1부터 8로 표현하며,
열 위치를 표현할 때는 a부터 h로 표현한다.
나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 할 수 있으며
정원 밖으로는 나갈 수 없다. 따라서 다음 두가지 경우로 이동할 수 있다.
 - 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
 - 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기 

 
"""



# 왕실의 나이트 : 내 답
first = input()
# 이동할 수 있는 경우의 수 좌표를 리스트에 넣기.
dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]
res = 0
# x, y를 현재 위치로 초기화 하고 경우의 수 마다 더해보기.
for i in range(8) :
    x = ord(first[0])
    y = int(first[1])
    x += dx[i]
    y += dy[i]
    # 만약 x와 y가 체스판을 벗어나지 않는다면 결과에 더해주기
    if 'a' <= chr(x) <= 'h' and 1 <= y <= 8 :
        res += 1
# 출력
print(res)





# 왕실의 나이트 _ 답안 예시
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1),
         (2, 1), (1, 2), (-1, 2), (-2, 1)]
# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps :
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8 :
        result += 1

print(result)





"""
# 문자열 재정렬 : 문제 설명
알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어진다.
이 때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에,
모든 숫자를 더한 값을 이어서 출력하는 프로그램을 작성하시오.

ex) 입력 : K1KA5CB7
    출력 : ABCKK13
     
"""



# 문자열 재정렬 _ 내 답
string = sorted(input())
nums = 0
char = ''
for i in string :
    if ord(i) <= 57 :
        nums += int(i)
    else :
        char += i
print(char + str(nums))



# 문자열 재정렬 _ 답안 예시
data = input()
result = []
value = 0
# 문자를 하나씩 확인하며
for x in data :
    # 알파벳인 경우 결과 리스트에 삽입.
    if x.isalpha() :
        result.append(x)
    # 숫자는 따로 더하기.
    else :
        value += int(x)
# 알파벳을 오름차순으로 정렬한다.
result.sort()
# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입.
if value != 0 :
    result.append(str(value))
# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))





"""
# 게임 개발 : 문제 설명
n * m 크기의 직사각형의 육지 또는 바다가 존재하는 게임 맵이 있다.
캐릭터는 동서남북 중 한 곳을 바라본다.
맵의 각 칸은 (a, b)로 나타낼 수 있고
a는 북쪽으로부터 떨어진 칸의 개수, b는 서쪽으로부터 떨어진 칸의 개수이다.
캐릭터는 상하좌우로 움직일 수 있고 바다로 되어있는 공간에는 갈 수 없다.  


"""



# 게임 개발 _ 답안 예시
# n, m을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
# 현재 좌표 방문 처리
d[x][y] = 1

# 전체 맵 정보를 입력받기
array = []
for i in range(n) :
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left() :
    global direction
    direction -= 1
    if direction == -1 :
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True :
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0 :
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else :
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4 :
        nx = x - dx[direction]
        ny = y - dx[direction]
        # 뒤로 갈 수 있다면 이동하기.
        if array[nx][ny] == 0 :
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else :
            break
        turn_time = 0
# 정답 출력
print(count)




