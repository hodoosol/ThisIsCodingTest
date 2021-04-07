"""
이것이 코딩 테스트다 2021 강의 몰아보기
2021.04.06

Chapter 1. 코딩 테스트 출제 경향 분석 및 파이썬 문법 부수기

"""


"""
1. 알고리즘 성능 평가

복잡도로 알고리즘의 성능을 나타낼 수 있다.
 - 시간 복잡도 : 알고리즘의 수행 시간을 분석한다.
 - 공간 복잡도 : 알고리즘의 메모리 사용량을 분석한다.
일반적으로, 복잡도가 낮을수록 좋은 알고리즘이다.

복잡도는 빅오 표기법(Big-O)으로 표현한다.
 -> 가장 빠르게 증가하는 항만을 고려하고, 알고리즘 수행 시간의 상한을 나타낸다.

아래로 갈수록 좋은 성능을 나타낸다.
O(2^n)
O(n^3)
O(n^2)
O(n log n)
O(n)
O(log n)
O(1)



- 간단하게 시간 복잡도 계산해보기(1)
array = [3, 5, 1, 2, 4]
sum = 0

for x in array :
    sum += x
    
print(sum)
 -> 수행 시간은 데이터의 개수 n에 비례할 것이다. 따라서 O(n)이다.
 


- 간단하게 시간 복잡도 계산해보기(2)
array = [3, 5, 1, 2, 4]

for i in array :
    for j in array :
        temp = i * j
        print(temp)

 -> for문을 2번 돌려야하므로 시간 복잡도는 O(n^2)가 된다.
    모든 2중 for문이 O(n^2)인 것은 아니다.
    내부적으로 다른 함수를 호출한다면 그 함수의 시간복잡도까지 고려해야 한다.
    
    

** 일반적으로 파이썬에서 연산 횟수가 5억을 넘어가는 경우 5 ~ 15초가 소요된다.
   코테에서 시간제한은 보통 1 ~ 5초이므로 유의해야 한다.
   
   
   
알고리즘 문제 해결 과정
 1) 지문 분석, 컴퓨터적 사고
 2) 요구사항(복잡도) 분석
 3) 문제 해결을 위한 아이디어 찾기
 4) 소스코드 설계 및 코딩



- 알고리즘의 수행시간을 측정하는 코드를 짜보자.
import time
start_time = time.time() # 측정 시작

end_time = time.time() # 측정 종료
print('time : ", end_time - start_tiem) # 수행 시간 출력





2. 자료형
모든 프로그래밍은 결국 데이터를 다루는 행위이므로
자료형에 대한 이해는 프로그래밍의 첫단계이다 !

1) 정수형 integer
 : 양의 정수, 음의 정수, 0



2) 실수형 float
 : 변수에 소수점을 붙이면 실수로 인식한다. ex) 157.93, -1837.2
   ** 지수를 표현하고 싶다면 e나 E를 사용하면 된다.
       ex) 1e9 = 10의 9제곱
      파이썬에서 지수는 실수형으로 처리된다.
   실수형을 저장하기 위해서 4나 8byte의 고정된 크기의 메모리를 할당한다.
   이는 실수 정보의 정확성을 떨어트려 미세한 오차가 발생하게 된다.
   ex)
   a = 0.3 + 0.6
   print(a)           -> 0.89999999999999 출력됨.
   if a == 0.9 :
       print(True)
   else :
       print(False)   -> False 출력됨.
   
   이 문제를 해결하기 위해서, 보통 round() 함수를 이용하여 반올림한 값을 사용한다.
   
   
   
3) 리스트
 : 데이터를 연속적으로 담아 처리하는 자료형이다.
 
   리스트의 인덱스는 0부터 시작하므로 인덱싱할 때 주의해야 한다. 
   a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
   print(a[3])      -> 4 출력됨.
 
   리스트를 초기화해보자.
   n = 10
   a = [0] * n
   print(a)         -> [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 출력됨.

   리스트 컴프리헨션으로 리스트를 초기화해보자.
   array = [i for i in range(10)]
   print(array)     -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 출력됨.

   array2 = [[0] * m for _ in range(n)]
   print(array2)    -> n * m 크기로 0이 채워진 리스트 출력됨.

   ** 언더바 _ 는 무엇일까 ?
    반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할때 사용한다.
    즉, i가 필요없을 때 사용한다.
    for _ in range(5) :
        print('hi')     -> hi가 5번 출력됨.

   리스트 관련 메소드에는
   append(), sort(), reverse(), insert(), count(), remove() 등이 있다.
    
   리스트에서 특정 값을 가지는 원소를 모두 제거해보자.
   a = [1, 2, 3, 4, 5, 5, 5]
   remove_set = {3, 5}
   
   result = [i for i in a if i not in remove_set]
   print(result)        -> 3과 5가 지워진 [1, 2, 4]가 출력됨. 



4) 문자열
 : data = 'Hello World'와 같이 ''나 ""로 초기화한다.
   두 문자열과 +을 사용하면 문자열끼리 연결할수 있고
   하나의 문자열에 *를 사용하면 그 값만큼 여러번 더해진다.
   리스트와 마찬가지로 인덱싱과 슬라이싱을 이용할 수 있지만
   특정 인덱스의 값을 변경할 수는 없다. (Immuatable)
    


5) 튜플
 : 리스트와 유사하지만 한번 선언된 값을 변경할 수 없다.
   ()을 사용하며 리스트에 비해 상대적으로 공간 효율적이다.
   
   튜플의 장점 ?   
   1. 서로 다른 성질의 데이터를 묶어서 관리해야할 때
   2. 데이터의 나열을 해싱의 키 값으로 사용해야할 때
   3. 리스트보다 메모리를 효율적으로 사용해야할 때



6) 딕셔너리
 : 키와 값의 쌍을 데이터로 가지는 자료형이다.(인덱싱 사용불가)
   변경 불가능한 자료형을 키로 사용한다.
   해시 테이블을 이용하므로 O(1)시간에 처리할 수 있다.
   
   data = dict()
   data['사과'] = 'Apple'
   data['바나나'] = 'Banana'
   data['코코넛'] = 'Coconut'
   print(data)   -> {'사과':'Apple', '바나나':'Banana', '코코넛':'Coconut'} 출력됨.
   
   딕셔너리의 메소드 ?
    키 데이터만 추출 : keys()
    값 데이터만 추출 : values() 
   


7) 집합
 : 중복을 허용하지 않고 순서가 없는 자료형이다.(인덱싱 사용불가)
   set()함수나 {}으로 초기화할 수 있다.
   
   집합의 연산을 사용할 수 있다.
   a = set([1, 2, 3, 4, 5])
   b = set([3, 4, 5, 6, 7])
   
   print(a | b) # 합집합
   print(a & b) # 교집합
   print(a - b) # 차집합
   
   add(), update(), remove()함수를 사용할 수 있다.
   




3. 기본 입출력

자주 사용되는 표준 입력 방법
 - list(map(int, input().split()))
 - a, b, c = map(int, input().split())

input보다 빠르게 입력 받으려면 sys.stdin.readline() 메소드를 사용한다.
단, 입력 후 엔터가 줄 바꿈 기호로 입력되므로 rstrip() 메소드를 함께 쓴다.

원래는 문자열과 정수를 함께 출력할 수 없지만 'f'를 붙이면 가능하다.
 ex) answer = 7
     print(f'정답은 {answer}입니다.')
      -> 정답은 7입니다. 출력된다.
      
      
      


4. 조건문
 : if, elif, else로 조건문을 만들 수 있다.
 
   ex) a = 5
       if a >= 0 :
           print('a >= 0')
       elif a >= -10 :
           print('0 > a >= -10')
       else :
           print('-10 > a')



조건문과 반복문을 사용할 때 자주 사용하는 연산자를 알아보자.
 1. 비교 연산자
   : 같다 ==, 다르다 !=, >, <, >=, <=
   
 2. 논리 연산자
    : 논리값(True / False)의 연산에 사용한다. 
      둘 다 참 and, 하나만 참 or, 모두 거짓 not

 3. 기타 연산자
    : 포함한다 in, 포함하지 않는다 not in
 
 4. pass 키워드
    : 아무것도 처리하고 싶지 않을 때 사용한다.





5. 반복문
 : 특정한 소스코드를 반복적으로 실행하고자할 때 사용한다.
   while, for로 만들 수 있다.
   
   ex)
   result = 0
   for i in range(1, 10) :
       result += i
   print(result)   ->   45 출력됨.
   
   continue ?
    - 반복문에서 남은 코드의 실행을 건너뛰고, 다음 반복을 진행하고자할 때 사용.
   break ?
    - 반복문을 즉시 탈출하고자 할 때 사용.





6. 함수와 람다 표현식

1) 함수(Function)
 : 특정한 작업을 하나의 단위로 묶어 놓은 것.
   불필요한 소스코드의 반복을 줄일 수 있다.

1. 내장 함수
 - 파이썬이 기본적으로 제공하는 함수
2. 사용자 정의 함수
 - 개발자가 직접 정의하여 사용하는 함수
 
함수를 정의하려면 매개변수와 반환 값이 필요하다.
def 함수명(매개변수) :
    실행할 소스코드
    return 반환 값         의 형태로 함수를 정의해야 한다.
    
    
    
ex1)
def add(a, b) :
    return a + b
    
print(add(3, 7))  ->  10 출력됨.
a, b = 매개변수  3, 7 = 전달인자(argument)



ex2)
def add2(a, b) :
    print('함수의 결과 :', a + b)    
    
add(3, 7)  ->  10 출력됨.



- 함수와 글로벌 변수를 사용해보자.
a = 0

def func() :
    global a
    a += 1
    
for i in range(10) :
    func()
    
print(a)  ->  10 출력됨.



파이썬에서 함수는 여러 개의 반환 값을 가질 수 있다.
ex)
def operator(a, b) :
    add_var = a + b
    subtract_var = a - b
    multiply_var = a * b
    divide_var = a / b
    return add_var, subtract_var, multiply_var, divide_var

a, b, c, d = operator(7, 3)
print(a, b, c, d)   ->   10 4 21 2.3333333333333335 출력됨.



2) 람다 표현식
 : 람다 표현식을 이용하면 함수를 간단하게 작성할 수 있다.
   def add(a, b) :
       return a + b
   
   print((lambda a, b : a + b)(3, 7))
   두 함수는 똑같은 기능을 한다.
   
ex)
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b : a + b, list1, list2)
print(list(result))  ->  [7, 9, 11, 13, 15] 출력됨.





7. 표준 라이브러리

내장 함수 : 필수적인 기본 함수
           최소값 반환 min(), 최대값 반환 max()
           배열을 오름차순으로 정렬 sorted(), reverse = True 해주면 내림차순.
     
               
itertools : 반복되는 형태의 데이터를 처리하기 위한 기능 제공.
            특히 코테에서는 순열과 조합 라이브러리가 많이 사용된다.
            
            순열 - 서로 다른 n개에서 순서를 고려하여 나열
            ex)
            from itertools import permutations
            data = ['A', 'B', 'C']
            result = list(permutations(data, 3))
            print(result)
             -> [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'),
              ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')] 출력됨.

            조합 - 서로다른 n개에서 순서를 고려하지 않고 나열
            ex)
            from itertools import combinations
            data = ['A', 'B', 'C']
            result = list(combinations(data, 2))
            print(result)
             -> [('A', 'B'), ('A', 'C'), ('B', 'C')] 출력됨.


heapq : 힙 자료구조를 제공한다. 우선순위 큐 기능을 구현할 수 있다.


bisect : 이진 탐색 기능을 제공한다.


collections : 덱(deque), 카운터(Counter) 등의 유용한 자료구조 사용 가능.
              Counter는 리스트에서 요소의 등장 횟수를 세는 기능을 제공한다.
              ex)
              from collections import Counter
              counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
              print(counter['blue'])
              print(counter['green'])
              print(dict(counter))
               -> 3
                  1
                  {'red': 2, 'blue': 3, 'green': 1} 출력된다.


math : 팩토리얼, 제곱근, 최대공약수, pi, 삼각함수 등필수적인 수학적 기능 제공.
       ex) 최대공약수(gcd) 함수를 사용해서 최소공배수(lcm)을 계산해보자.
       import math
       def lcm(a, b) :
           return a * b // math.gcd(a, b)
       a = 21
       b = 14
       print(math.gcd(21, 14))
       print(lcm(21, 14))
        -> 7
           42 출력됨.





"""
