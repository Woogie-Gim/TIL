// Chapter 01-2. 함수 오버로딩(Function Overloading)

/*
int Myfunc()
{
}

int Myfunc()
{
}

Myfunc();

동일한 함수 두개가 존재하기 때문에 어떤 함수를 불러 올지 모른다
C언어는 호출할 함수를 결정할 때에 순전히 이름에만 의존한다
Myfunc() Myfunc(5) 5라는 인자를 받을 수 있는 함수는 하나이기 때문에 받을 수 있다.
이름 + 인자를 조합하다면 함수 호출할 수 있다 => 함수 오버로딩(Function Overloading)

C++은 함수 호출 시 '함수의 이름'과 '전달되는 인자의 정보'를 동시에 참조하여 호출할 함수를 결정한다.
따라서 이렇듯 매개변수의 선언이 다르다면 동일한 이름의 함수도 정의 가능하다.
그리고 이러한 형태의 함수 정의를 가리켜 '함수 오버로딩(Function Overloading')이라 한다.

int MyFunc(char c) {...}
int MyFunc(int n) {...}
매개변수의 자료형이 달라도 함수 오버로딩 성립

int MyFunc(int n) {...}
int MyFunc(int n1, int n2) {...}
매개변수의 수가 달라도 함수 오버로딩 성립

void MyFunc(int n) {...}
int MyFunc(int n) {...}
반환형의 차이는 함수 오버로딩의 조건을 만족시키지 않는다. => compile error

*/