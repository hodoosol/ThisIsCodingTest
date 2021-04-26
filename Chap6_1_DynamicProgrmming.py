"""
이것이 코딩 테스트다 2021 강의 몰아보기
2021.04.26

Chapter 6. 다이나믹 프로그래밍

"""


"""
1. 다이나믹 프로그래밍
 - 메모리를 적절히 사용하여 수행 시간의 효율성을 비약적으로 상승시키는 방법을
   동적 계획법, 혹은 다이나믹 프로그래밍이라고 한다.
 - 이미 계산된 결과(작은 문제)는 별도의 메모리 영역에 저장하여 다시 계산하지 않도록 한다.
 - 일반적으로 탑다운(하향식)과 보텀업(상향식)이라는 두 가지 방식으로 구성된다.
 
 
프로그래밍 분야에서의 동적(Dynamic)이란 어떤 의미를 가질까 ?
 - 자료구조에서 동적 할당(Dynamic Allocation)은
   프로그램이 실행되는 도중에 실행에 필요한 메모리를 할당하는 기법을 의미한다.
 - 반면에 다이나믹 프로그래밍에서 '다이나믹'은 별다른 의미없이 사용된 단어이다.  
 
 
다이나믹 프로그래밍의 조건
 1) 최적 부분 구조(Optimal Substructure)
    - 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결.
 2) 중복되는 부분 문제(Overlapping Subproblem)
    - 동일한 작은 문제를 반복적으로 해결.
    
    
ex) 피보나치 수열
 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ... 와 같은 형태의 수열이 피보나치 수열이다.
 이를 인접한 항들 사이의 관계식(점화식)으로 표현해보면 다음과 같다.
   An = An-1 + An-2  , (A1 = 1, A2 = 1) 
   -> 첫번째와 두번째 수열의 값을 알면 위의 식으로 모든 수열의 값을 알 수 있다.

 피보나치 수열이 계산되는 과정을 리스트로 표현해보자.
 [1, 1, 1+1, 1+2, 2+3, 3+5, 5+8, 8+13, 13+21, 23+34, 34+55, 55+89]
  = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
     
 즉 4번째 피보나치 수 f(4)를 구하려면
  f(4) = f(3) + f(2) 이고, 다시 f(3)은 f(2) + f(1)이므로
  f(4) = f(2) + f(1) + f(2) 의 과정을 거쳐야 한다.
  
          

"""


# 피보나치 수열을 파이썬으로 구현해보자. (단순 재귀)
def fibo(x) :
    if x == 1 or x == 2 :
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4))



"""
그러나 단순 재귀 함수로 피보나치 수열을 해결하면 지수의 시간 복잡도를 가지게 된다.
예를들어 f(6)을 구하기 위해서는
f(6) = f(5) + f(4)
     = f(4) + f(3) + f(3) + f(2)
     = f(3) + f(2) + f(2) + f(1) + f(2) + f(1) + f(2)
     = f(2) + f(1) + f(2) + f(2) + f(1) + f(2) + f(1) + f(2)
위 과정처럼 수많은 f(2)가 호출되는 것을 알 수 있다.  ->  비효율적이다.

따라서 피보나치 수열의 시간 복잡도는
theta(1.618 ... ^n) 또는 O(2^n) 이고,
빅오 표기법을 기준으로 f(30)을 계산하기 위해 약 10억번 가량의 연산을 수행해야 한다.

이러한 비효율을 해결하기 위해서, 다이나믹 프로그래밍의 사용 조건을 만족하는지 확인해보자.
 1) 최적 부분 구조 : 큰 문제를 작은 문제로 나눌 수 있다.
 2) 중복되는 부분 문제 : 동일한 작은 문제를 반복적으로 해결한다.
  ---->  피보나치 수열은 다이나믹 프로그래밍의 사용 조건을 만족한다 !
  
  
  
2. 메모이제이션 (Memoization)
 - 한 번 계산한 결과를 메모리에 메모하는 기법으로, 
   다이나믹 프로그래밍을 구현하는 방법 중 하나이다.
   
메모이제이션의 특징 ?
   1) 같은 문제를 다시 호출하면 메모 했던 결과를 그대로 가져온다.
   2) 값을 기록해 놓는다는 점에서 캐싱(Caching)이라고도 한다.  



3. 탑다운 vs. 보텀업
 - 탑다운(메모이제이션) 방식은 하향식이라고도 하며 보텀업 방식은 상향식이라고도 한다.
 - 다이나믹 프로그래밍의 전형적인 형태는 보텀업 방식이다. 
   결과 저장용 리스트는 DP 테이블이라고 부른다.
 - 엄밀히 말하면 메모이제이션은 이전에 계산된 결과를 일시적으로 기록해 놓은 넓은 개념을 의미한다.
   따라서 메모이제이션은 다이나믹 프로그래밍에 국한된 개념은 아니다.
   또, 한 번 계산된 결과를 담아 놓기만 하고 다이나믹 프로그래밍을 위해 활용하지 않을 수 있다.
    
     
     
"""


# 피보나치 수열 : 탑다운 다이나믹 프로그래밍

# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수를 재귀함수로 구현 (탑다운)
def fibo(x) :
    # 종료 조건 (1 혹은 2일 때 1을 반환)
    if x == 1 or x == 2 :
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0 :
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라 피보나치 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))



# 피보나치 수열 : 보텀업 다이나믹 프로그래밍

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 98

# 피보나치 함수를 반복문으로 구현 (보텀업)
for i in range(3, n + 1) :
    d[i] = d[i - 1] + d[i - 2]

print(d[n])



"""
4. 피보나치 수열을 메모이제이션으로 해결할 때의 프로그래밍 동작을 분석해보자.
아래의 식은 메모이제이션 하지 않을 때이다.
f(6) = f(5) + f(4)
     = f(4) + f(3) + f(3) + f(2)
     = f(3) + f(2) + f(2) + f(1) + f(2) + f(1) + f(2)
     = f(2) + f(1) + f(2) + f(2) + f(1) + f(2) + f(1) + f(2) 
     
이제 이미 계산된 결과를 메모리에 저장하여 f(6)을 구해본다면,     
  1. f(6)을 구하기 위해 f(5)를 호출한다.
  2. f(5)를 구하기 위해 f(4)를 호출한다.
  3. f(4)를 구하기 위해 f(3)을 호출한다.
  4. f(3)을 구하기 위해 f(2)와 f(1)을 호출한다. 
     각각의 값은 1이므로 바로 f(3)의 값을 구할 수 있다.
  5. 이제 f(3)의 값을 메모리에 저장하고 f(2)의 값과 함께 f(4)의 값을 구한다.
  6. f(4)의 값을 메모리에 저장하고 f(3)의 값과 함께 f(5)의 값을 구한다.
  7. f(5)의 값을 메모리에 저장하고 f(4)의 값과 함께 f(6)의 값을 구한다. 끝 !

따라서 메모이제이션을 이용하는 경우 피보나치 수열 함수의 시간 복잡도는 O(n)이다.



"""


# 위의 의사코드를 파이썬으로 구현해보자.

d = [0] * 100

def fibo(x) :
    print('f(' + str(x) + ')', end = ' ')
    if x == 1 or x == 2 :
        return 1
    if d[x] != 0 :
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 1)
    return d[x]

fibo(6)
# f(6) f(5) f(4) f(3) f(2) f(2) f(3) f(4) f(5) 가 출력된다.



"""
5. 다이나믹 프로그래밍 vs. 분할 정복
 - 두 방법 모두 최적 부분 구조를 가질 때 사용할 수 있다.
     큰 문제를 작은 문제로 나눌 수 있고,
     작은 문제의 답을 모아서 큰 문제를 해결할 수 있는 상황이다.
 - 두 방법의 차이점은 부분 문제의 중복이다.
     DP 문제에서는 각 부분 분제들이 서로 영향을 미치며 부분 문제가 중복되지만,
     분할 정복 문제에서는 동일한 부분 문제가 반복적으로 계산되지 않는다.
     
     
분할 정복의 대표적인 예시인 퀵 정렬을 살펴보자.
 1) 한 번 기준 원소(Pivot)가 자리를 변경해서 자리를 잡으면 그 기준 원소의 위치는 바뀌지 않는다.  
 2) 분할 이후에 해당 피벗을 다시 처리하는 부분 문제는 호출하지 않는다.
 
 5  7  9  0  3  1  6  2  4  8        피벗 : 5
 (1  4  2  0  3)  5  (6  9  7  8)    5를 기준으로 분할 완료
   ->  이제 5는 다른 부분의 문제에 포함되지 않고 자리를 그대로 유지한다.
       따라서, 부분 문제가 중복되지 않는다.
       
       
6. 다이나믹 프로그래밍 문제에 접근하는 방법
 - 주어진 문제가 다이나믹 프로그래밍 유형임을 파악하는 것이 중요하다.
 - 가장 먼저 그리디, 구현, 완전 탐색 등의 아이디어로 해결할 수 있는지 검토해야 한다.
   다른 알고리즘으로 풀이 방법이 떠오르지 않는다면 DP를 고려해보자.
 - 일단 재귀 함수로 비효율적인 완전 탐색 프로그램을 작성한 뒤에(탑다운),
   작은 문제에서 구한 답이 큰 문제에서 그대로 사용될 수 있다면 DP로 코드를 개선하자.
 - 일반적인 코딩 테스트 수준에서는 기본 유형의 DP문제가 출제되는 경우가 많다.     



"""