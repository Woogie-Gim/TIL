/*Chapter 01-3. 매개변수의 디폴트 값*/

/*
int MyFunc(int num=10) {}
아무 매개변수도 들어오지 않는다면 인자값으로 10을 전달을 한다
=> 매개변수의 디폴트 값
MyFunc(10); 이랑 같은 의미

디폴트 값은 둘 이상의 매개변수에 각각 지정해줄 수 있다
int MyFunc(int num1=1, int num2=2) {}
인자값을 전달하지 않고 num1에 1이 num2에 2가 전달 되는 것으로 간주된다.
MyFunc(1,2); 와 같은 의미

MyFunc(3);
전달 되는 인자는 왼쪽에서 부터 전달됨
따라서 num1 = 3 / num2 에는 디폴트 값인 2가 전달이 된 것으로 간주


#include<iostream>
int Adder(int num1=1, int num=2);

int main(void)
{
	std::cout<<Adder()<<std::endl;
	std::cout<<Adder(5)<<std::endl;
	std::cout<<Adder(3,5)<<sted::endl;
	return 0;
}

int Adder(int num1, int num2)
{
	return num1+num2;
}

디폴트 값은 함수의 선언에만 위치
함수의 선언을 별도로 둘 때에는 디폴트 값의 선언을 함수의 선언부에 위치시켜야 한다.
그 이유는 컴파일러의 컴파일 특성에서 찾을 수 있다.

컴파일러는 함수의 디폴트 값의 지정여부를 알아야 함수의 호출 문장을 적절히 컴파일 할 수 있다.

부분적 디폴트 값 설정
매개 변수의 일부에만 디폴트 값을 지정하고, 채위지지 않은 매개변수에만 인자를 전달하는 것이 가능하다.

전달되는 인자가 왼쪽에서부터 채워지므로, 디폴트 값은 오른쪽에서부터 채워져야 한다.

int WrongFunc(int num1=10, int num2, int num3) {}
int WrongFunc(int num1=10, int num2=20, int num3) {}

WrongFunc(5,7) num1에 먼저 전달이 된다.

전달되는 인자가 왼쪽에서부터 채워지므로, 오른쪽이 빈 상태로 왼쪽의 매개변수에만 일부 채워진
디폴트 값은 의미를 갖지 못한다. 따라서 컴파일 에러를 일으킨다.
*/