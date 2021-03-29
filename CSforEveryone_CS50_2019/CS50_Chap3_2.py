"""
모두를 위한 컴퓨터 과학(CS50)
2021.03.26

Chapter 3. Array
"""


"""
5) 배열(2)

- N을 3이라는 상수로 만들고, 전역변수화 하기.
#include <cs50.h>
#include <stdio.h>

const int N = 3;    

int main(void)
{
    int scores[N];
    scores[0] = 72;
    scores[1] = 73;
    scores[2] = 33;
    
    printf('Average : %i\n', (score[0] + score[1] + score[2]) / N);
     -> Average : 59 출력
}





- 동적으로 프로그래밍하기.
#include <cs50.h>
#include <stdio.h>

float average(int length, int array[]);

int main(void)
{
    int n = get_int("Number of scores: ");
    int scores[n];
    for (int i = 0; i < n; i++)
    {   
        scores[i] = get_int("Score %i: ", i + 1);
            -> %i는 int형 출력, %d와 동일하다.
            
    printf("Average: %.1f\n", average(n, scores));
}

float average(int length, int array[])
{
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        sum += array[i];
    }
    return (float) sum / (float) length;
}





6) 문자열과 배열

int형은 4 byte 이므로 하나의 변수당 메모리의 4 바이트를 차지한다.
int형 배열일 때도 비슷하다.

string은 정해진 크기가 없이, 변수에 입력되는 길이 * 1 byte만큼 차지한다.
그렇다면 문자열이 언제 끝나는지를 어떻게 알 수 있을까 ?
 =>  NULL 문자 : \0 로 구분한다.
 
Hi! 는 3 글자이지만 메모리 상에서는 H I ! \0 의 4byte로 저장된다.
 
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string scores[4];
    names[0] = 'DASOL';
    names[1] = 'EMMA';
    names[2] = 'RODRIGO';
    names[3] = 'BRIAN';
    
    printf("%s\n", names[0]);
     -> DASOL 출력
    printf("%c%c%c%c%c", names[0][0], names[0][1], names[0][2], 
    names[0][3], names[0][4]);
     -> DASOL 출력
}

printf("%i", name[0][5]);  ->  0 출력됨.






7) 문자열의 활용

- for문을 사용하여 문자열의 끝이 널문자가 아닐 때까지만 출력하기
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = get_string("Input : ");
    printf("Output : ");

    for (int i = 0 ; s[i] != '\0'; i++)
    {
        printf("%c", s[i]);
    }
    printf("\n);
}





- string.h를 추가하여 strlen() 함수를 사용해보자.
#include <cs50.h>
#include <stdio.h>
#include <string.h>
int main(void)
{
    string s = get_string("Input : ");
    printf("Output : ");
    
    for (int i = 0 ; int n = strlen(s); i < n; i++)
     -> 문자열의 길이를 변수에 저장해두고 그 길이만큼 for문 돌리기.
     -> 변수에 저장해두면 strlen() 함수를 최초 1번만 불러와도 되니 효율이 좋다.
    {
        printf("%c", s[i]);
    }
    printf("\n);
}





- 소문자를 대문자로 바꿔보기.
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Before : ");
    printf("After : ");

    for (int i = 0 ; int n = strlen(s); i < n; i++)
    {
        if (s[i] >= 'a' && s[i] <= 'z')
        {
            // convert to uppercase
            printf("%c", s[i] - 32);
        }
        else
        {
            printf("%c", s[i]);
        }
    }
    printf("\n);
}





- ctype.h 추가, toupper()함수 사용하여 소문자를 대문자로.
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Before : ");
    printf("After : ");

    for (int i = 0 ; int n = strlen(s); i < n; i++)
    {
        pritnf("%c", toupper(s[i]));
    }
    printf("\n);
}





8) 명령행 인자
#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    if (argc == 2)
     ./program dasol 으로 실행시켰을때, 처음에 입력하는 프로그램의 이름이 argc 1,
     dasol이 argc 2이므로 출력또한 두번째 요소 argc[1]로 하면 된다.
    {
        printf("hello, %s\n", argc[1]);
    }
    else
    {
        printf("hello, world\n");
    }
}





"""