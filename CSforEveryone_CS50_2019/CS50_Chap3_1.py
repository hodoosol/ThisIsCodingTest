"""
모두를 위한 컴퓨터 과학(CS50)
2021.03.25

Chapter 3. Array
"""


"""
1) 컴파일링

printf()를 사용하기 위해서는 #include <stdio.h>라는 헤더파일을 불러야 함.
get_string()을 사용하기 위해서는 #include <cs50.h>라는 헤더파일 사용.

컴파일링 ? : 4단계를 거친다.
    1. 전처리 preprocessing 
    2. 프로그래밍 언어를 어셈블리어로 변환 compling
    3. 어셈블리어를 머신코드로 변환 assembling
    4. 모든 파일 하나로 합치기 linking 
    




2) 디버깅
ctrl + l : clear the terminal
한 줄씩 직접 확인하며 오류 찾기 or 디버거 이용

3) 코드의 디자인
코드의 가독성이 좋은지, 심미적으로 잘 작성되어 있는지 항상 고려해야 한다.





4) 배열(1)

   type   byte
--------------------   
   bool     1
   char     1
   int      4
   float    4
   long     8
   double   8
   string   ?


RAM에서는 어떻게 정보를 저장할까 ?
정보의 크기만큼 메모리(byte)를 할당해준다.


- char와 ASCII 코드
#include <stdio.h>

int main(void)
{
    char c1 = 'H';
    char c2 = 'I';
    char c3 = '!';
    
    printf('%c %c %c\n', c1, c2, c3);
     -> H I ! 로 출력됨
    printf('%i %i %i\n', (int) c1, (int) c2, (int) c3);
     -> 72 73 33 으로 출력됨 (ASCII 코드)
}




- 평균 점수 출력해보기
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int score1 = 72;
    int score2 = 73; 
    int score3 = 33;
    
    printf('Average : %i\n', (score1 + score2 + score3) / 3);
     -> Average : 59 출력, but 이 코드는 개선될 여지가 있다.
}




- 평균 점수 출력해보기 _ 개선된 ver.
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int scores[3];
    scores[0] = 72;
    scores[1] = 73;
    scores[2] = 33;
    
    printf('Average : %i\n', (score[0] + score[1] + score[2]) / 3);
     -> Average : 59 출력
}






"""