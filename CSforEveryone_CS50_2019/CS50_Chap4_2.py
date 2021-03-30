"""
모두를 위한 컴퓨터 과학(CS50)
2021.03.30

Chapter 4. Algorithm
"""


"""
5) 선택 정렬

For i from 0 to n-1
    Find smallest item between i'th item and last item
    Swap smallest item with i'th item
    
가장 작은 아이템을 찾아서, 자리를 바꿔 정렬하고
그 다음 작은 아이템을 찾아서, 자리를 바꿔 정렬하고 ... 반복한다.

선택 정렬 알고리즘의 상한 소요시간은
n + n-1 + n-2 + ... + 1 = n(n+1)/2 = O(n^2) 으로
버블 정렬과 같이 O(n^2)인 알고리즘이고,
최선의 상황에서도 모든 수를 비교해야 하기때문에
하한 소요시간 또한 Omega(n^2) 이다.





6) 정렬 알고리즘의 실행시간

Repeat n-1 times
    For i from 0 to n-2
        If i'th and i+i'th element out of order
            Swap them
버블 정렬을 할 때, 이미 모든 수가 정렬된 상황에서도
알고리즘의 지시사항을 모두 다 따르는 것은 비효율적일 것이다.

따라서, 
Repeat until no swaps
    For i from 0 to n-2
        If i'th and i+i'th element out of order
            Swap them
아무 것도 바뀌지 않을 때까지 반복하라는 조건문으로 수정한다면
버블정렬의 하한 소요시간은 Omega(n^2)에서 Omega(n)으로 바뀔 것이다.
ex) 1 2 3 4 5 6 7 8 로 정렬된 최선의 케이스를 만났을 때,
8번만 값을 비교하면 되기때문에 Omega(n)이다.





7) 재귀

- 전화번호부의 가운데를 펼쳐서 원하는 번호 찾기
Pick up phone book
Open to middle of phone book
Look at page
If Dasol is on page
    Call Dasol
Else if Dasol is earlier in book
    Open to middle of left half of book
    Go back to line 3
Else if Dasol is later in book
    Open to middle of right half of book
    Go back to line 3
Else
    Quit





- 좀 더 간단히
Pick up phone book
Open to middle of phone book
Look at page
If Dasol is on page
    Call Dasol
Else if Dasol is earlier in book
    Search lefh half of book
Else if Dasol is later in book
    Search right half of book
Else
    Quit



재귀 함수는 자기 자신을 호출한다.



- iteration(반복) _ 마리오 피라미드 만들어보기.
#include <cs50.h>
#include <stdio.h>

void draw(int n);

int main(void)
{
    int height = get_int("Height : ");
    
    draw(height);
}

void draw(int n)
{
    for (int i = 1; i <= h; i++)
    {
        for (int j = 1;  j <= i; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}  





- recursion(재귀)
#include <cs50.h>
#include <stdio.h>

void draw(int h);

int main(void)
{
    int height = get_int("Height : ");
    draw(height);
}

void draw(int h)
{
    if (h == 0)
    {
        return;
    }
    
    draw(h - 1);
    
    for (int i = 0; i < h; i++)
    {
        printf("#");
    }
    printf("\n");
}  





8) 병합 정렬

If only one item
    Return

Else
    Sort left half of items
    Sort right half of items
    Merge sorted halves

왼쪽 정렬하고, 오른쪽 정렬하고 두개를 병합한다.

병합 정렬의 상한 소요시간은 O(n log n)이고
하한 소요시간 또한 Omega(n log n)이다.

어떤 알고리즘의 소요시간의 상한과 하한이 같을 때,
Theta(n log n)으로 표현할 수 있다.
Theta(n^2)인 알고리즘은 선택정렬이 있다.






"""