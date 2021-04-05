"""
모두를 위한 컴퓨터 과학(CS50)
2021.03.31

Chapter 5. Memory
"""


"""
1) 메모리 주소

16진법(Hexadecimal)
 : 1 2 3 4 5 6 7 8 9 a b c d e f 으로 10진수의 1부터 15를 표현하고,
   10진수의 16은 16진수의 10이 된다.
   4 bits씩 16진수로 변환하고 0x를 붙이면 된다.
   
   2진수인 숫자 4개를 16진수 숫자 1개로 나타낼 수 있다.
   ex) 2진수 11111111 -> 16진수 0xff
   
   2개의 16진수는 1 byte의 2진수로 변환되므로
   컴퓨터의 비트, 바이트 정보를 표현하기 유용하다.
   




- 컴퓨터의 메모리에서 무슨 일이 일어나는지 살펴보자.
#include <stdio.h>

int main(void)
{
    int n = 50;
    printf("%i\n", n);
     -> 50이 출력된다.
}



- &n을 사용하여 n의 주소를 출력해보자.
#include <stdio.h>

int main(void)
{
    int n = 50;
    printf("%p\n", &n);
     -> 0x7ffe00b3abdc 출력됨. (주소의 예시)
}



&가 주소를 출력한다면 *은 그 주소에 있는 값을 출력한다.



- *&n을 사용하여 n의 값을 출력해보자.
#include <stdio.h>

int main(void)
{
    int n = 50;
    printf("%i\n", *&n);
     -> 50 출력됨.
}





2) 포인터

- n의 주소를 따로 변수에 저장하여 다뤄보기.
#include <stdio.h>

int main(void)
{
    int n = 50;
    int *p = &n;
    printf("%p\n", p);
     -> 0x7fff397762c 출력됨. (주소의 예시)
}



- n의 주소를 저장한 p가 가리키고 있는 값 출력하기(결국 n의 값)
#include <stdio.h>

int main(void)
{
    int n = 50;
    int *p = &n;
    printf("%i\n", *p);
     -> 50 출력됨.
}



int n = 50;
int *p = &n; 이며, 각각의 n과 p가 우체통이라고 가정해보자.
n 우체통에는 n 우체통의 주소(ex. 123)가 적혀있고
우체통의 안에는 변수 n의 값인 50이 들어있을 것이다.

n 우체통을 가리키고 있는 p 우체통에는 
p 우체통의 주소(ex. 456)가 적혀있긴 하겠지만 중요하지 않을 것이고
p 우체통의 안에는 변수 n의 주소인 123이 들어있을 것이다.
 

포인터는 8 byte를 차지한다.





3) 문자열

문자열이라는 자료는 사실 존재하지 않는다 ?
string s = "DASOL"; 이라고 할 때,
D는 0x123
A는 0x124
S는 0x125 
O는 0x126
L는 0x127
\0는 0x128 로 char 타입으로서 1 바이트의 주소 하나씩을 갖고있을 것이다.

char *s = "EMMA";

여기서 문자열 s는 포인터와 비슷한 기능을 하고 있다.
문자열의 처음 시작하는 글자 'D'의 주소를 저장하면 널문자를 만날 때까지
나머지 문자들을 같은 문자열로 인식한다.
따라서 결국 문자열은 문자 배열의 첫 번째 바이트 주소가 된다.



- 문자열과 주소를 출력해보자.
#include <stdio.h>

int main(void)
{
    char *s = "DASOL";
    printf("%s\n", s);
     -> DASOL 출력된다.
    printf("%p\n", s);
     -> 0x42a9f2 출력(주소의 예시)
     
    ### 문자열의 첫번째 글자의 주소를 출력하려면 어떻게 해야할까?
    printf("%p\n", &s[0]);
     -> 0x42a9f2(주소의 예시), 문자열 전체의 주소와 똑같은 주소가 출력된다.
    문자열 s의 주소는 사실상 첫번째 문자의 주소와 같다는 것을 알 수 있다.
}



- 나머지 문자열의 주소들을 출력해보자.
#include <stdio.h>

int main(void)
{
    char *s = "DASOL";
    
    printf("%p\n", s);
    printf("%p\n", &s[0]);
    printf("%p\n", &s[1]);
    printf("%p\n", &s[2]);
    printf("%p\n", &s[3]);
    printf("%p\n", &s[4]);
    
    -> 0x42ab52
    -> 0x42ab52
    -> 0x42ab53
    -> 0x42ab54
    -> 0x42ab55
    -> 0x42ab56 출력된다.
}





4) 문자열 비교

- 문자열의 주소가 가리키고 있는 값 출력하기
#include <stdio.h>

int main(void)
{
    char *s = "DASOL";
    printf("%c\n", *s);
     -> D 출력된다.
    printf("%c\n", *(s + 1));
    printf("%c\n", *(s + 2));
    printf("%c\n", *(s + 3));
    printf("%c\n", *(s + 4));
     -> A
     -> S
     -> O
     -> L 출력.
}



- 두 정수를 비교하는 프로그램을 만들어보자.
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int i = get_int("i : ");
    int j = get_int("j : ");
    
    if (i == j)
    {
        printf("Same\n");
    }
    else
    {
        printf("Different\n");
    }
}


---> 잘 작동한다.



- 문자열 비교하는 프로그램을 만들어보자.
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = get_string("s : ");
    string t = get_string("t : ");
    
    if (s == t)
    {
        printf("Same\n");
    }
    else
    {
        printf("Different\n");
    }
}


---> 잘 작동하지 않는다. 왜일까 ?
s와 t는 각각 다른 주소에 저장되기 때문이다.



- s와 t의 주소를 출력해보자.
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    char *s = get_string("s : ");
    char *t = get_string("t : ");
    
    printf("%p\n", s);
    printf("%p\n", t);
     -> 0xed76a0(주소의 예시)
     -> 0xed76e0(주소의 예시) 출력된다.
     s와 t는 몇 바이트 떨어져있는 것을 알 수있다.
}





"""
