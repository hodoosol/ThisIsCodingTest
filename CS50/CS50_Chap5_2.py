"""
모두를 위한 컴퓨터 과학(CS50)
2021.04.01

Chapter 5. Memory
"""


"""
5) 문자열 복사

- 문자열 s를 t에 복사하고, t를 대문자로 바꾸어보자.
#include <cs50.h>
#include <ctype.h>
#include <stdio.h>

int main(void)
{
    string s = get_string("s: ");
     -> emma 입력
    string t = s;
    
    t[0] = toupper(t[0]);
    
    printf("%s\n", s);
    printf("%s\n", t);
     -> Emma
     -> Emma 출력됨. 왜 s까지 대문자로 바뀌었을까 ?
}

s는 emma라는 문자열을 가리키는 포인터 역할을 하고 있었다.
이 때, t에 s를 복사하면 t또한 emma를 가리키는 포인터가 되기 때문에
s와 t는 둘 다 같은 곳을 가리키므로, 변형된 문자열 또한 그대로 가리키는 것이다.



그렇다면, 서로 다른 메모리 공간에 emma를 복사하려면 어떻게 해야할까 ?

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    char *s = get_string("s: ");
     -> emma 입력
     
    char *t = malloc(strlen(s) + 1);
     -> malloc으로 문자열 s의 길이(+ 널문자)만큼 메모리를 할당하고,
     
    for (int i = 0; n = strlen(s); i < n; i++0)
    {
        t[i] = s[i];
         -> for문으로 s의 문자 하나하나를 t로 복사한다.
    }
    
    printf("%s\n", s);
    printf("%s\n", t);
     -> emma
     -> Emma 출력된다. 성공 !
}



- 코드 개선하기
#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    char *s = get_string("s: ");     
    char *t = malloc(strlen(s) + 1);
    
    strcpy(t, s); 
     -> for문을 대신
    
    printf("%s\n", s);
    printf("%s\n", t);
}





6) 메모리 할당과 해제

malloc 함수를 이용하여 변수에 메모리를 할당한 뒤,
free로 해제해주지 않으면 메모리 누수(memory leaking)가 발생한다.

- 메모리 해제하기.
#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    char *s = get_string("s: ");     
    char *t = malloc(strlen(s) + 1);
    
    strcpy(t, s); 
    
    printf("%s\n", s);
    printf("%s\n", t);
    
    free(t);
}



- malloc을 더 살펴보자.
#include <stdlib.h>

void f(void)
{
    int *x = malloc(10 * sizeof(int));
     -> 포인터 x에 10 * 4 바이트의 메모리를 할당한다.
    x[10] = 0;
     -> 버퍼 오버플로우, x[10]은 존재하지 않는다.
        x[9]까지 있으므로 x[9] = 0;으로 수정해야 한다.
    free(x);
}

int main(void)
{
    f();
    return 0;
}





7) 메모리 교환, 스택, 힙

- a와 b의 값을 서로 바꾸어보자.
#include <stdio.h>

void swap(int a, int b);

int main(void)
{
    int x = 1;
    int y = 2;
    
    printf("x is %i, y is %i\n", x, y);
     -> x is 1, y is 2 가 출력된다.
    swap(x, y);
    printf("x is %i, y is %i\n", x, y);
     -> x is 1, y is 2 가 출력된다. 바뀌지 않았다 ! 왜일까 ?
     -> 함수에 인자를 전달할 때, 그 값을 복사해서 전달하기 때문에
        swap 함수는 x, y가 아닌 x, y의 값을 복사한 복사본 a, b를 바꾸게 된다.
}

void swap(int a, int b)
{
    int tmp = a;
    a = b;
    b = tmp;
}



메모리를 좀 더 자세히 들여다 보자.

machine code  - 0과 1로 컴파일된 코드가 메모리 위쪽에 저장
globals       - 만약 코드에 전역변수가 사용된다면 이 위치에 저장
heap          - 메모리를 할당받을 수 있는 커다란 영역(malloc) 
  ↓   heap은 아래로 커진다.
  
  ↑   stack은 위로 커진다.
stack         - 함수가 호출될 때 지역변수가 쌓이는 공간
                하나씩 위로 올려 쌓은 뒤 맨 위에서부터 차례대로 처리된다.
                
그렇다면, swap 함수를 제대로 구현하기 위해선 어떻게 해야할까 ?
포인터를 이용하면 된다.



- 포인터를 이용하여 swap 함수 구현하기.
#include <stdio.h>

void swap(int a, int b);

int main(void)
{
    int x = 1;
    int y = 2;
    
    printf("x is %i, y is %i\n", x, y);
     -> x is 1 y is 2 출력.
    swap(&x, &y);
     -> x, y의 주소를 전달한다.
    printf("x is %i, y is %i\n", x, y);
     -> x is 2 y is 1이 출력된다. 성공 !
}

void swap(int *a, int *b) -> 정수의 주소를 받아 그것들을 각각 a, b로 부르겠다.
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}





8) 파일 쓰기

heap과 stack이 각각 반대되는 방향에서 점점 커진다면, 언젠가는 충돌할 것이다.
overflow가 발생하면 사진이나 파일이 열리지 않고 화면이 정지하는 등 문제가 생긴다.

heap overflow
ex) malloc을 사용할 때, free해주지 않고 계속해서 메모리를 할당한다.
stack overflow
ex) 재귀함수를 무한으로 출력한다.



- scanf()로 정수를 입력받아 보자.
#include <stdio.h>

int main(void)
{
    int x;
    printf("x : ");
    scanf("%i", &x);
    print("x : %i\n", x);
}



- scanf()로 문자열을 입력받아 보자.
#include <stdio.h>

int main(void)
{
    char s[5];
     -> s가 scanf로 입력받을 문자열(EMMA)를 저장하기 위한
        char 5개의 메모리를 할당해준다.
    printf("s : ");
    scanf("%s", s);
     -> 왜 &s를 하지 않을까 ?
        char *s는 이미 주소이기 때문에 &가 필요없다.
        포인터 변수는 그 자체가 주소로 정의되기 때문이다.
    print("s : %s\n", s);
}



- 전화번호부 파일을 생성하고 이름과 전화번호를 입력받아 저장해보자.
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Open file
    FILE *file = fopen("phonebook.csv", "a");
    
    // Get strings from user
    char *name = get_string("Name : ");
    char *number = get_string("Number : ");
    
    // Print (write) strings to file
    fprintf(file, "%s, %s\n", name, number);
    
    // Close file
    fclose(file);
}





9) 파일 읽기

- 주어진 파일이 jpeg파일인지 아닌지 확인해보자.
#include <stdio.h>

int main(int, argc, char *argv[])
{
    // Ensure user ran program with two words at prompt
    // Error Check - 입력이 없으면 종료한다.
    if (argc != 2)
    {   
        return 1;
    }
    
    // Open file
    // 파일명도 입력하고, 그것의 별명을 r로 지정한다.
    FILE *file = fopen(argc[1], "r");
    // Error Check - 에러가 생기면 1을 반환.
    if (file == NULL)
    {
        return 1;
    }
    
    //Read 3 bytes from file
    // unsigned ? 0 ~ 255 범위의 값(signed = -128 ~ 127)
    unsigned char bytes[3];
    // fread(배열, 읽을 바이트 수, 읽을 회수, 읽을파일);
    fread(bytes, 3, 1, file);
    
    // Check if bytes are 0xff 0xd8 0xff
    if (bytes[0] == 0xff && bytes[1] == 0xd8 && bytes[2] == 0xff)
    {
        printf("Maybe\n");
    }
    else
    {
        printf("No\n");
    }
}






"""