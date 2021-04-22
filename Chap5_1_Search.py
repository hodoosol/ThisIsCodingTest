"""
이것이 코딩 테스트다 2021 강의 몰아보기
2021.04.22

Chapter 5. 정렬

"""



"""
1. 이진 탐색 알고리즘
 - 순차 탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터
              데이터를 하나씩 확인하는 방법
 - 이진 탐색 : 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 탐색하는 방법
              이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정한다.
              
              
              
이진 탐색의 동작 예시를 살펴보자.
이미 정렬된 10개의 데이터 중에서 값이 4인 원소를 찾는다.

0  2  4  6  8  10  12  14  16  18
 
 1) 시작점 : 0   중간점 : 8   끝점 : 18
    찾으려고 하는 데이터인 4가 중간점 보다 작으므로 중간점 이후는 볼 필요가 없다.
 
 2) 따라서, 시작점 : 0  중간점 : 2  끝점 : 6 으로 다시 설정한다.
    이제 중간점 2가 찾으려는 데이터 4보다 작으므로 중간점 이전으로는 볼 필요가 없다.

 3) 시작점 : 4  중간점 : 4  끝점 : 6 으로 다시 설정한다.
    4의 인덱스가 무엇인지 알았으니 탐색에 성공했다 !
    
    
     
이진 탐색의 시간 복잡도
 - 단계마다 탐색 범위를 2로 나누는 것과 동일하므로 연산 횟수는 log2N에 비례한다.
 - 예를 들어 초기 데이터 수가 32개 일 때, 이상적으로 1단계를 거치면 16개가 남는다.
     - 2단계를 거치면 8개가 남는다.
     - 3단계를 거치면 4개가 남는다.
 - 다시 말해 이진 탐색은 탐색 범위를 절반씩 줄이며, 시간 복잡도는 O(logN)을 보장한다.
 

"""



# 이진 탐색을 파이썬으로 구현해보자.
def binary_search(array, target, start, end) :
    if start > end :
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target :
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target :
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else :
        return binary_search(array, target, mid + 1, end)

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None :
    print('원소가 존재하지 않습니다.')
else :
    print(result + 1)



# 이진 탐색을 반복문으로 구현해보자.
def binary_search2(array, target, start, end) :
    while start <= end :
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target :
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target :
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else :
            start = mid + 1
    return None

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search2(array, target, 0, n - 1)
if result == None :
    print('원소가 존재하지 않습니다.')
else :
    print(result + 1)





"""
2. 파이썬 이진 탐색 라이브러리
 - bisect_left(a, x) 
    : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
 - bisect_right(a, x)
    : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환
    

"""



# 파이썬의 이진 탐색 라이브러리를 사용해보자. _ 1
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))



# 파이썬의 이진 탐색 라이브러리를 사용해보자. _ 2
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수 만들기
def count_by_range(a, left_value, right_value) :
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 배열 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 -1 ~ 3 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))





"""
3. 파라메트릭 서치(Parametric Search)
 - 파라메트릭 서치란 최적화 문제를 결정 문제(예 or 아니오)로 바꾸어 해결하는 방법이다.
     - ex) 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제     
 - 일반적으로 코테에서 파라메트릭 서치 문제는 이진 탐색을 이용하여 해결할 수 있다.


"""





"""
# 떡볶이 떡 만들기 : 문제 설명
오늘 다솔이는 여행 가신 부모님을 대신해서 떡집 일을 하기로 했다.
오늘은 떡볶이 떡을 만드는 날이다.
다솔이네 떡볶이 떡은 재밌게도 떡볶이 떡의 길이가 일정하지 않다.
대신 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다.

절단기에 높이 H를 지정하면 줄지어진 떡을 한 번에 절단한다.
높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.

ex) 높이가 19, 14, 10, 17 cm 인 떡이 나란히 있고 절단기 높이를 15 cm 로 지정하면
    자른 뒤 떡의 높이는 15, 14, 10, 15 cm 가 될 것이다.
    잘린 떡의 길이는 차례로 4, 0, 0, 2 cm 이다. 손님은 6 cm 만큼을 가져간다.
    
손님이 왔을 때 요청한 총 길이가 M 일 때 적어도 M 만큼의 떡을 얻기 위해
절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.


"""



# 떡볶이 떡 만들기 : 답안 예시
n, m = map(int, input().split())
rice = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(rice)

# 이진 탐색 수행 (반복적)
result = 0
while(start <= end) :
    total = 0
    mid = (start + end) // 2
    for x in rice :
        # 잘랐을 때의 떡의 양 계산
        if x > mid :
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
    if total < m :
        end = mid - 1
    # 떡의 양이 많은 경우 덜 자르기 (오른쪽 부분 탐색)
    else :
        # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result 에 기록
        result = mid
        start = mid + 1

# 정답 출력
print(result)





"""
# 정렬된 배열에서 특정 수의 개수 구하기 : 문제 설명
n 개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있다.
이 때 이 수열에서 x가 등장하는 횟수를 계산하라.

ex) 수열 {1, 1, 2, 2, 2, 2, 3}, x = 2
      ->  값이 2인 원소는 4개이므로 4를 출력한다.
    
단, 이 문제는 시간 복잡도 O(logN) 으로 설계하지 않으면 시간 초과 판정.

** 문제 해결 아이디어
 - 시간 복잡도 O(logN)으로 동작하는 알고리즘을 요구하고 있다.
   따라서 일반적인 선형 탐색으로는 시간 초과 판정을 받는다.
   하지만 데이터가 정렬되어 있기 대문에 이진 탐색을 수행할 수 있다.
   
 - 특정 값이 등장하는 첫 번째 위치와 마지막 위치를 찾아
   위치 차이를 계산하면 문제를 해결할 수 있다.
   
   
"""



# 정렬된 배열에서 특정 수의 개수 구하기 : 내 답
n, x = map(int, input().split())
nums = list(map(int, input().split()))

res = nums.count(x)

if res == 0 :
    print(-1)
else :
    print(res)



# 정렬된 배열에서 특정 수의 개수 구하기 : 답안 예시
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range2(array, left_value, right_value) :
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = map(int, input().split())
array = list(map(int, input().split()))

# 값이 [x, x] 범위에 있는 데이터의 개수 계산
count = count_by_range2(array, x, x)

# 값이 x인 원소가 존재하지 않는다면
if count == 0 :
    print(-1)
else :
    print(count)




