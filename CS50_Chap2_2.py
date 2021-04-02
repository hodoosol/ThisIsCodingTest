"""
모두를 위한 컴퓨터 과학(CS50)
2021.03.24

Chapter 2. C
"""


"""
4) 자료형, 형식 지정자, 연산자
bool
char     %c
double   %f
float    %f
int      %d
long     %li
string   %s



 - 정수 나이 입력 받아 출력하기
#include <cs50.h>
#include <stdio.h>

int main(void){
    int age = get_int("What's your age ?\n");
    printf("You are at least %i days old.\n", age * 365);
}



 - 실수 가격 입력 받아 출력하기
#include <cs50.h>
#include <stdio.h>

int main(void){
    float price = get_float("What's the pirce?\n");
    printf("Your total is %.2f.\n", price * 1.0625);
}

%f 에 .2 등을 지정해주지 않으면 소수점 아래 6자리까지 출력된다.
%.3f 는 소수점 아래 3자리까지 출력한다.



 - 짝수일까 홀수일까 ?
#include <cs50.h>
#include <stdio.h>

int main(void){
    // 숫자 입력받기
    int n = get_int("n : ");
    // 그 숫자가 만약 2로 나누어 떨어진다면 : 짝수
    if (n % 2 == 0){
        printf("even\n");
    }
    // 아니라면 : 홀수
    else{
        printf("odd\n");
    }
}



- 동의하십니까 ?
#include <cs50.h>
#include <stdio.h>

int main(void){
    char c = get_char("Do you agree? \n");

    if (c == 'Y' || c == 'y'){
        printf("Agreed.\n");
    }
    else if (c == 'N' || c == 'n'){
        printf("Not agreed.\n");
    }
}

|| 는 or을 의미하는 연산자이다.





5) 사용자 정의 함수, 중첩 루프
- cough를 3번 연속 출력해보자.
#include <cs50.h>
#include <stdio.h>

int main(void){
    printf("cough\n");
    printf("cough\n");
    printf("cough\n");

    for (int i = 0; i < 3; i++){
        printf("cough\n");
    }
}



- cough 함수를 만들어서 출력해보자.
#include <cs50.h>
#include <stdio.h>

void cough(void);          // main함수를 맨 위로 올리기 위해, 
                           // 미리 내가 만들 cough 함수를 선언해야한다.

int main(void){
    for (int i = 0; i < 3; i++){
        cough();
    }
}
void cough(void){
    printf("cough\n");
}



- 정수 n을 인자로 받아(n = 3) cough를 3번 연속 출력해보자.
#include <stdio.h>

void cough(int n);

int main(void){
    cough(3);
}
void cough(int n){
    for (int i = 0; i < n ; i ++){
        printf("cough\n");
    }
}



- do while문을 이용해, 양수를 입력받아 출력해보자.
#include <cs50.h>
#include <stdio.h>

int get_positive_int(void);

int main(void){
    int i = get_positive_int();
    printf("%i\n", i);
}
int get_positive_int(void){
    int n ;
    do{
        n = get_int("Positive Integer : ");
    }
    while (n < 1);
    return n;
}



- n개의 물음표를 출력해보자.
#include <cs50.h>
#include <stdio.h>

int main(void){
    int n;
    do{
        n = get_int("Width : ");
    }
    while (n < 1);

    for (int i = 0; i < n; i ++){
        printf("?");
    }
    printf("\n"); 
}



- # 으로 이루어진 n * n 행렬을 출력해보자.
#include <cs50.h>
#include <stdio.h>

int main(void){
    int n;
    do{
        n = get_int("Size : ");
    }
    while (n < 1);

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            printf("#");
        }
        printf("\n"); 
    } 
}





6) 하드웨어의 한계
RAM의 저장공간은 유한하므로 컴퓨터가 저장 가능한 숫자 역시 유한하다.

#include <cs50.h>
#include <stdio.h>

int main(void){
    float x = get_float("x : ");
    float y = get_float("y : ");

    printf("x / y = %.1f\n", x / y);
}

이 코드로 x / y 의 값을 구한다면
%.1f ... %f 의 값은 정상적으로 나오지만
%.10f, %.50f 등은 정확한 값이 나오지 않는다.
이는 메모리 저장공간이 유한하기 때문이며, 특정 지점에서 컴퓨터가 한계에 부딪힌 것이다.



- 2의 제곱수 출력하기
#include <stdio.h>
#include <unistd.h>

int main(void){
    for (int i = 1; ; i *= 2){
        printf("%i\n", i);
        sleep(1);
    }
}

1, 2, 4, 8, 16, 32, 64 ... 계속해서 출력되다가 10억 이상으로 커지면
overflow가 발생하고 이후부터는 0만 출력된다.





"""
