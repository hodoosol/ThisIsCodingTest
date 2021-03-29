"""
모두를 위한 컴퓨터 과학(CS50)
2021.03.29

Chapter 4. Algorithm
"""


"""
1) 검색 알고리즘

선형탐색 : 처음부터 끝까지 하나하나 탐색하기.
- 선형탐색의 의사코드
For 1 from 0 to n-1
    If i'th element is 50
        Retrum true
Return False


이진탐색 : 만약 배열이 정렬되어 있다면, 중간부터 값을 확인하고
찾고자하는 값과 비교, 큰쪽 or 작은쪽으로 이동, 다시 중간부터 값 확인하는 방법.
- 이진탐색의 의사코드
If no itmes
    Return false
If middle item is 50
    Return true
Else if 50 < middle item
    Search left half
Else if 50 > middle item
    Search right half


만약 탐색할 배열이 정렬되어 있지 않다면 이진탐색보다 선형탐색이 더 효율적이다.





2) 알고리즘 표기법

Big - O
 -  알고리즘의 실행 시간을 나타낸다. 실행 시간의 상한.
O(n^2)
O(n log n)  
O(n)        :  Linear Search
O(log n)    :  Binary Search
O(1)


Omega
 - 실행 시간의 하한을 나타낸다. 운이 좋을 때, 최소한으로 검색을 끝낸 시간.
Omega(n^2)
Omega(n log n)  
Omega(n) 
Omega(log n)
Omega(1)        : Linear Search, Binary Search





3) 선형 검색

- 선형탐색을 코드로 만들어보자.
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int number[6] = {4, 8, 15, 16, 23, 42};
    
    for (int i = 0; i < 6; i++)
    {
        if (numbers[i] == 50)
        {
            printf("Found\n");
        }
    printf("Not found\n");
      -> numbers에는 50이 없기 때문에 Not found가 출력될 것이다. 
}





- 전화번호부에서 DASOL을 찾아보자. _ 잘못된 예시
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string names[4] = {"DASOL", "EMMA", "BRIAN", "DAVID"};
    
    for (int i = 0; i < 4; i++)
    {
        if (numbers[i] == "DASOL") 
        : C언어에서는 문자열을 비교할때 단순히 ==" " 으로 할 수 없다.
          따라서 strcmp() 함수를 사용하여 비교해야 한다.
        {
            printf("Found\n");
        }
    printf("Not found\n");
}



- 전화번호부에서 DASOL을 찾아보자. _ 옳은 예시
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string names[4] = {"DASOL", "EMMA", "BRIAN", "DAVID"};
    
    for (int i = 0; i < 4; i++)
    {
        if (strcmp(numbers[i], "DASOL")) 
         : strcmp()는 두 문자열이 같다면 0을 반환한다.
        {
            printf("Found\n");
            return 0;
             : return을 해주지 않으면 같은 문자열을 찾은지 몰라서
               무조건 Not found를 출력하므로 0을 반환하여 알려줘야 한다.
               
            -> Found 출력됨.
        }
    printf("Not found\n");
    return 1;
}





- C언어로 전화번호부를 만들어보자.
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string names[4] = {"DASOL", "EMMA", "BRIAN", "DAVID"};
    string numbers[4] = {"617-555-0100", "617-555-0101", "617-555-0102", "617-555-0103"};
    
    for (int i = 0; i < 4; i++)
    {
        if (strcmp(numbers[i], "DASOL") == 0) 
        {
            printf("%s\n", numbers[i]);
            return 0;
            -> 617-555-0100 출력됨.
        }
    printf("Not found\n");
    return 1;
}

But, 이름과 전화번호의 순서가 항상 같을 것이라는 보장이 없다 ...
이것을 해결하기 위해 새로운 타입의 자료형을 우리가 만들어보자.





- 새로운 자료형과 전화번호부.
#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct
{
    string name;
    string number;    
}
person;

int main(void)
{
    person people[4];
    
    people[0].name = "DASOL";
    people[0].number = "617-555-0100";
    
    people[1].name = "EMMA";
    people[1].number = "617-555-0101";
    
    people[2].name = "BRIAN";
    people[2].number = "617-555-0102";
    
    people[3].name = "DAVID";
    people[3].number = "617-555-0103";
    
    for (int i = 0; i < 4; i++)
    {
        if (strcmp(people[i].name, "DASOL") == 0) 
        {
            printf("%s\n", people[i].numbers);
            return 0;
            -> 617-555-0100 출력됨.
        }
    printf("Not found\n");
    return 1;
}





4) 버블 정렬


Repeat n-1 times
    For i from 0 to n-2
        If i'th and i+1'th elements out of order
            Swap them


(n-1) * (n-1)
= n^2 - 1n -1n + 1
= n^2 - 2n + 1

따라서 버블 정렬의 실행시간 상한은 O(n^2)이고,
이미 탐색하려는 배열이 정렬되어 있다고 해도
똑같이 루프를 돌며 비교해야 하므로 하한 또한 Omega(n^2)이다.






"""