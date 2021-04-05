"""
모두를 위한 컴퓨터 과학(CS50)
2021.04.03

Chapter 6. Data Structures 자료구조
"""


"""
1) malloc과 포인터 복습

- 버그가 있는 코드를 살펴보자.
int main(void)
{
    // 포인터 선언
    int *x;
    int *y;
    // x 에만 4 bytes 메모리를 할당해준다. 
    x = malloc(sizeof(int));
    
    // x의 주소로 가서 42를 저장 y의 주소로 가서 13을 저장.
    *x = 42;
     -> x가 42를 가리키게 된다. (성공)
    *y = 13;
     -> BUT ! y는 선언만 하고 어디를 가리킬지 정의해주지 않았으므로
        없거나 잘못된 주소로 가서 값을 저장하려하면 버그가 발생.
}



- 개선해보자.
int main(void)
{
    int *x;
    int *y;
    x = malloc(sizeof(int));
    
    // x의 주소로 가서 42를 저장(초기화) -> x = y -> 다시 x의 주소로 가서 13을 저장
    // 이렇게 하면 x의 값을 원하는 대로 바꿀 순 있지만 42는 사라진다.
    *x = 42;
    y = x;
    *y = 13;
}





2) 배열의 크기 조정하기

char *arr[3] 문자열에 1 byte를 더 추가하려면 어떻게 해야할까 ?
새로운 메모리 char *arr[4]를 할당받은 뒤 기존 문자열을 복사하고
char 1개를 더 추가한 다음, 원래 있던 메모리는 free해주면 된다.
그러나 이 알고리즘은 모든 문자열 하나하나를 복사해야하기 때문에
O(n)의 시간 복잡도를 가지며 이상적인 접근법은 아니다.



- 정적인 코드로 만들어보자.
#include <stdio.h>

int main(void)
{
    // 고정된 크기 3을 가지는 배열 선언
    int list[3];
    // 하드코딩하여 배열 초기화. 
    list[0] = 1;
    list[1] = 2;
    list[2] = 3;
    // 세 값을 각각 프린트해보자.
    for (int i =0; i < 3; i++)
    {
        printf("%i\n", list[i]);
    }
}



- 동적으로 만들어보자.
#include <stdio.h>

int main(void)
{
    // 포인터에 12바이트로 이루어진 덩어리의 주소를 할당해준다.
    int *list = malloc(3 * sizeof(int));
    if (list == NULL)
    {
        return 1;
    }
    // malloc으로 메모리를 할당한 후 []기호를 사용하면
       컴퓨터가 자동으로 그 메모리 덩어리로 이동하여, 
       지정된 자료형(여기서는 int)를 입력받는다.
    list[0] = 1;
    list[1] = 2;
    list[2] = 3;
    // 세 값을 각각 프린트해보자.
    for (int i =0; i < 3; i++)
    {
        printf("%i\n", list[i]);
    }
}



- 동적으로 배열의 사이즈를 바꾸어보자.
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *list = malloc(3 * sizeof(int));
    if (list == NULL)
    {
        return 1;
    }
    list[0] = 1;
    list[1] = 2;
    list[2] = 3;
    
    // 새로운 배열을 만들고 이전 배열의 정수들을 복사한다.
    int *tmp = malloc(4 * sizeof(int));
    if (tmp == NULL)
    {
        return 1;
    }
    for (int i = 0; i < 3; i ++)
    {
        tmp[i] = list[i];
    }
    // 새로운 배열에 정수를 하나 더 추가한다.
    tmp[3] = 4;
    
    // 이전 배열의 메모리를 풀어준다.
    free(list);
    
    // 새 배열의 이름 변경.
    list = tmp;
    
    for (int i =0; i < 4; i++)
    {
        printf("%i\n", list[i]);
    }
}



- But, 좀 더 간단하게 하는 방법 ? realloc.
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *list = malloc(3 * sizeof(int));
    if (list == NULL)
    {
        return 1;
    }
    list[0] = 1;
    list[1] = 2;
    list[2] = 3;
    
    // realloc을 사용하여 이전 배열을 복사해온다.
    int *tmp = realloc(list, 4 * sizeof(int));
    if (tmp == NULL)
    {
        return 1;
    }
    tmp[3] = 4;
    
    free(list);  
    
    list = tmp;
    for (int i =0; i < 4; i++)
    {
        printf("%i\n", list[i]);
    }
    
    free(list);
}





3) 연결 리스트 : 도입

struct
. : 구조체의 속성값에 접근할 때 사용한다.
* : 메모리 덩어리로 접근할 수 있는 역참조 연산자.

연결 리스트란 ?
 값들의 리스트를 저장하는 방법. 
 배열과 비슷하지만 배열은 고정된 메모리 덩어리로, 크기를 조절하려면 번거로운 과정을 거쳐야한다.
 그러나 배열은 대괄호를 이용하여 쉽게 인덱싱할 수 있고 
 랜덤(임의) 접근으로 어떤 주소로라도 똑같은 시간으로 접근 가능하여 속도가 빠르다는 장점이 있고
 바이너리 검색 등에 이용될 수 있다.
 
 
 
배열 1, 2, 3을 연결 리스트로 저장해보자.
0x123에 1, 다음 바이트에 0x456
0x456에 2, 다음 바이트에 0x789
0x789에 3, 다음 바이트에 배열이 끝났다는 뜻으로 NULL(\n이 아닌 16진법의 널 == 0x0) 저장.

  1                    2         3
0x456                0x789      NULL        처럼 나타낼 수 있다.

number(저장된 숫자) + next(리스트의 다음 요소의 주소)



- 연결 리스트를 코드로 구현해보자.
typedef struct node
{
    int number;
    struct node *next;
}
node;





4) 연결 리스트 : 코딩

- 연결 리스트를 코드로 구현해보자2.
#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
}
node;

int main(void)
{
    // 리스트의 맨 처음을 초기화 _ 아무 것도 없다.
    node *list = NULL;

    // node만큼의 메모리를 임시로 만든 변수 n에 할당.
    node *n = malloc(sizeof(node));
    if (n != NULL) // 에러 체크.
    {
        // node의 number을 2로 초기화.
        n->number = 1;
        // 다음 주소를 할당, but 아직 없으므로 Null.
        n->next = NULL;    
    }
    // 리스트와 노드를 연결한다.
    list = n;

    // 2번째 노드 만들기
    node *n = malloc(sizeof(node));
    if (n != NULL)
    {
        n->number = 2;
        n->next = NULL;
        list->next = n;    
    }
    
    // 3번째 노드 만들기
    node *n = malloc(sizeof(node));
    if (n != NULL)
    {
        n->number = 3;
        n->next = NULL;
        list->next->next = n;    
    }
    
    // 출력하기
    for (node *tmp = list; tmp != NULL; tmp = tmp->next)
    {
        printf("%i\n", tmp->number);
    }
    
    // 메모리 해제
    while (list != NULL)
    {
        node *tmp = list->next;
        free(list);
        list = tmp;
    }
}





"""