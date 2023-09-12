/*Chapter 01-5 이름공간(namespace)에 대한 소개*/

/*
namespace의 필요성
라이브러리를 가져와 개발을 한다고 가정
A라이브러리 ./ B라이브러리 / C라이브러리
모두 func().함수가 존재한다고 가정
호출할 때 어려움이 있음
라이브러리 별로 이름공간을 통해 func를 호출할 수 있다면 이름 충돌을 막을 수 있다

이름공간의 기본원리

namespace BestComImpl
{	BestComImpl 이라는 이름의 공간
	void simpleFunc(void)
	{
		std::cout<<"BestCom이 정의한 함수"<<std::endl;
	}
}

namespace ProgComImpl
{	ProgComImpl이라는 이름의 공간
	void SimpleFunc(void)
	{
		std::cout<<"ProgCom이 정의한 함수"<<std::endl;
	}
}

int main(void)
{	범위 지정 연산자
	BestComImpl::SimpleFunc(); 이름 공간 BestComImpl에 정의된 SimpleFunc의 호출
	ProgComImpl::SimpleFunc(); 이름 공간 ProgComImpl에 정의된 SimpleFunc의 호출
}

존재하는 이름공간이 다르면 동일한 이름의 함수 및 변수를 선언하는 것이 가능하다

프로젝트의 진행에 있어서 발생할 수 있는 이름의 충돌을 막을 목적으로 존재하는 것이 이름공간이다.

동일한 이름공간 내에서의 함수호출
namespace BestComImpl
{
	void SimpleFunc(void);
}

namespace BestComImpl
{
	void PrettFunc(void);
}
선언된 이름공간의 이름이 동일하다면, 이 둘은 동일한 이름공간으로 간주한다.
즉, SimpleFunc와 PretyFunc는 동일한 이름 공간안에 존재하는 상황이다.

void BestComImpl::SimpleFUnc(void)
{
	std::cout<<"BestCom이 정의한 함수"<<std::endl;
	PrettyFunc();	// 동일 이름 공간
	ProgComImpl::SimpleFunc(); // 다른 이름 공간
}

void BestComImpl::PrettyFunc(void)
{
	std::cout<<"So Pretty!!"<<std::endl;
}

이름공간을 명시하지 않고 함수를 호출하면, 함수의 호출문이 존재하는 함수와 동일한 이름공간 안에서
호출할 함수를 찾게 된다.
따라서 SimpleFunc 함수 내에서는 이름공간을 명시하지 않은 상태에서 PrettyFunc함수를 직접호출 할 수 있다.

이름공간의 중첩

이름공간 Parent
namespace Parent
{
	int num=2;
	namespace SubOne	이름공간 Parent::SubOne
	{
		int num=3;
	}

	namespace SubTwo	이름공간 Parent::SubTwo
	{
		int num=4;
	}
}
이름공간은 중첩이 가능하다. 따라서 계층적 구조를 갖게끔 이름공간을 구성할 수 있다.

std::cout, std::cin, std::endl

std::cout -> 이름공간 std에 선언된 cout
std::cin -> 이름공간 std에 선언된 cin
std::endl -> 이름공간 std에 선언된 endl

<iostream>에 선언되어 있는 cout, cin 그리고 endl은 이름공간 std안에 선언되어 있다.
이렇듯 이름 충돌을 막기 위해서 C++ 표준에서 제공하는 다양한 요소들은 이름공간 std에 선언되어 있다.

using을 이용한 이름공간의 명시

#include <iostream>
using namespace std;
int main(void)
{
	int num=20;
	cout<<"Hello World!"<<endl;
	cout<<"Hello "<<"World!"<<endl;
	cout<<num<<' '<<'A';
	cout<<' '<<3.14<<endl;
	return 0;
}
이름 공간 std에 선언된 것은 std라는 이름공간의 선언없이 접근하겠다는 선언
(C++ 표준 라이브러리 안에 std namespace)

너무 빈번한 using namespace의 선언은 이름의 충돌을 막기위한 이름공간의 선언을 의미 없게 만든다.
따라서 제한적으로 사용할 필요가 있다.

이름공간의 별칭 지정과 전역변수의 접근
namespace ABC=AAA::BBB::CCC;
AAA::BBB::CCC에 대해 ABC라는 이름의 별칭 선언 후,

ABC::num1=10;
ABC::num2=20;
위와 같이 하나의 별칭으로 이름공간의 선언을 대신할 수 있다.

int val=100;	//전역변수

int SimpleFunc(void)
{
	int val=20;		//지역변수
	val+=3;		//지역변수 val의 값 3증가
	::val+=7;	//전역변수 val의 값 7 증가
	이름공간이 없는 이름공간의 전역변수에 7을 증가 시켜라
	전역변수로 선언된 val을 의미
}

범위지정 연산자는 지역변수가 아닌 전역변수의 접근에도 사용이 가능하다.
*/