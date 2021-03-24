"""
모두를 위한 컴퓨터 과학(CS50)
2021.03.23

Chapter 2. C
"""



"""
1) C 기초
#include <stdio.h>      -> 컴퓨터에게 아래의 코드를 이해하려면 stdio.h 파일을 봐봐. 라고 명령.

int main(void)
{
    printf("hello, world\n");
}

이러한 소스코드를 컴퓨터에게 보내서 이해하게 하려면 머신코드로 번역해야 한다.
이를 우리는 컴파일러라고 부르고, 소스코드를 컴파일하면 0과 1로 이루어진 머신코드로 번역된다.





2) 문자열
- 이름 물어보기
#include <stdio.h>
#include <cs50.h>    -> 컴퓨터에게 'string'이 뭔지 알려주기위해 불러옴

int main(void)
{
    string answer = get_string("What's your name?\n");
    printf("hello, %s\n", answer);
}



- 좋아하는 동물 물어보기
#include <stdio.h>
#include <cs50.h>

int main(void){
    string animal = get_string("좋아하는 동물을 알려주세요\n");
    printf("내가 좋아하는 동물은 %s\n",animal);
}



** clang 파일명.c : 컴파일
   clang -o 별명 파일명.c : 별명 붙이기
   clang -o 별명 파일명.c -lcs50 : cs50과 link 해주기
   make 파일명 : 복잡한 컴파일 명령 대신, 컴퓨터가 알아서 컴파일
   ./파일명 : 컴파일 뒤 만들어진 머신코드 실행하기
    




3) 조건문과 루프
- for과 while을 이용하여 loop문을 만들 수 있다.
- 코드를 작성할 때, 얼마나 효율적인지 혹은 얼마나 적은 메모리나 CPU를 사용하는지 따져보는 것 중요.
#include <stdio.h>
#include <cs50.h>

int main(void){
    for (int i=0; i<11; i++){
        printf("개발공부는 재미있다! for loop\n");
    }

    int j = 0;
    while (j < 11){
        printf("개발공부는 재미있다! while loop\n");
        j ++;
    }
}





"""