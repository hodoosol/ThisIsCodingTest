/*
2021.04.01
Codecademy_Full-Stack Engineer Career Path
Chap1.


*/



/*
이 단원의 목표는 세가지이다.

웹 개발에 JavaScript가 사용되는 방법을 이해한다.
입문 JavaScript 구문을 이해한다.
JavaScript 구문을 연습한다.
1970 년대에 인터넷 붐이 일어났을 때,
IT 기업들은 시장에서 가장 강력하고 효율적인 웹 브라우저를 구축하기 위해 "브라우저 전쟁"을 벌였고
더 쉽고 가벼운 스크립트 언어를 개발하기 위해 노력했다.
이를 위해 1995년, NetScape의 Brendan Eich라는 직원이
10일 동안 JavaScript를 만들어 브라우저 전쟁에서 승리하게 된다.
2021년 현재까지도 JS가 가진 여러가지 장점들로 인해 필수 웹 기술로 사용되고 있다.

코드카데미는 이 과정에서 Jon Duckett의 저서 JavaScript and JQuery, Introduction을 추천하고 있다.
웹 개발에 대한 더 많은 정보는 MDN(developer.mozilla.org/en-US/) 에서 얻을 수 있다.
*/





/*

1. Console
console.log(); 를 사용하여 괄호 안에 넣은 내용을 콘솔에 출력할 수 있다.

console.log(26);

출력 :
26





2. 주석 처리

// 나 /* */

/*기호를 사용하면 결과에는 영향을 주지 않고 원하는 텍스트를 입력할 수 있다.
이 부분은 C언어와 똑같군.





3. Data Type
JavaScript의 데이터 타입에는 7가지가 있다.


Number : int, float
String
Boolean : true, false
Null
Undefined
Symbol
Object


console.log('JavaScript')
console.log(2011)
console.log('Woohoo! I love to code! #codecademy')
console.log(20.49)

출력 :
JavaScript
2011
Woohoo! I love to code! #codecademy
20.49





4. 산술 연산자(Arithmetic Operators)
더하기 Add : +
빼기 Subtract : -
곱하기 Multiply : *
나누기 Divide : /
나머지 연산 Remainder : %

console.log(26 + 3.5)
console.log(2021 - 1969)
console.log(65 / 240)
console.log(0.2708 * 100)

출력 :
29.5
52
0.2708333333333333
27.08






5.  문자열 연결(String Concatenation)
더하기 연산자 + 를 문자열에 적용하면 두 문자열을 하나로 합칠 수 있다.

이 프로세스를 concatenation이라고 한다.

문자열에 포함되어 있는 기호와 띄어쓰기까지 정확하게 결합하므로 원하는 결과를 얻으려면 잘 살펴야 한다.

console.log('Hello' + 'World')
console.log('Hello ' + 'World')

출력 :
HelloWorld
Hello World






6. 속성(Properties)
모든 문자열은 그 문자열의 길이를 저장하고 있는 length 속성을 갖고있다.

문자열에 도트 연산자라 불리는 . 과 속성 이름 length를 추가하면 검색할 수 있다.

console.log('Teaching the world how to code'.length)

출력 :
30






7. Methods
JavaScript는 다양한 문자열 메소드를 제공한다.

메소드를 부르거나 사용하기 위해서는 다음과 같은 것들이 필요하다.

'example string'.methodName().
마침표 . (도트 연산자)
메소드의 이름
여는 괄호와 닫는 괄호


메소드의 예시를 살펴보자.

toUpperCase() : 소문자 문자열을 대문자로 바꾸어 준다.
startsWith() : 문자열이 전달한 매개변수로 시작하는지 확인하여 불린값을 리턴한다.
trim() : 문자열의 공백을 없애준다.

console.log('hello'.toUpperCase());
console.log('Hey'.startsWith('H'));

출력 :
HELLO
true
console.log('Codecademy'.toUpperCase());
console.log('    Remove whitespace   '.trim());

출력 :
CODECADEMY
Remove whitespace




8. 내장 객체 Built-in Objects
이외에도 JavaScript에는 여러 내장 객체들이 있다. Math나 Number 등으로 사용 가능하다.


Math.random() : 0 에서 1 사이의 난수를 생성한다.

Math.floor() : 전달된 매개변수를 가장 가까운 정수로 내림한다.

// 0과 1 사이의 난수를 생성해보자.
console.log(Math.random());

// 0과 50 사이의 난수를 생성해보자.
console.log(Math.random() * 50);

// 생성된 난수를 가장 가까운 정수로 내림해보자.
console.log(Math.floor(Math.random() * 50));


출력 : (예시)
0.40021375819808447
20.010687909904224
20
Math.ceil() : 전달된 매개변수보다 크거나 같은 가장 작은 정수를 출력한다.

Number.isInteger() : 전달된 매개변수가 정수인지 아닌지 판별하여 불린값을 리턴한다.

// 같거나 큰 가장 작은 정수 출력하기.
console.log(Math.ceil(43.8));
// 입력된 매개변수가 정수인지 아닌지 판별하기
console.log(Number.isInteger(2017));


출력 :
44
true




*/
