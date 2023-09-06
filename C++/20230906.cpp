// Chator 01. printf와 scanf를 대신하는 입출력 방식

/* C++ 버전의 Hello Wolrd 출력 프로그램
헤더파일의 선언 #include<iostream>
-> iostream 헤더파일은 최신형 버전
출력의 기본구성 std::cout<<'출력대상1'<<'출력대상2'<<'출력대상3';
문자열은 "" 큰따옴표로 구성되어야 한다
개생의 진행 std::endl을 출렿마녀 개행이 이뤄진다.*/

#include<iostream>
//iostream 표준 라이브러리 헤더 파일
using namespace std;
int main(void)
{
	int num = 20;
	cout << "Hello World!" << std::endl;
	cout << "Hello " << "World!" << std::endl;
	cout << num << ' ' << 'A';
	cout << ' ' << 3.24 << std::endl;

	return 0;
}
/* C언어에서는 출력의 대상에 따라 서식지정을 달리했지만, C++에서는 그러한 과정이 불필요하다.*/

// scanf를 대신하는 데이터의 입력

/*예제를 통해서 확인할 사실 몇 가지
입력의 기본구성 std::cin>>'변수'
>> 반대 방향
변수의 선언위치 함수의 중간 부분에서도 변수의 선언이 가능하다.*/

#include<iostream>
using namespace std; //std를 미리 설정하여 std::cout 이런 식으로 적을 필요 없어진다.
int main(void)
{
	int val1;
	cout << "첫 번째 숫자입력: ";
	cin >> val1;
	//console in
	int val2;
	cout << "두 번째 숫자입력: ";
	cin >> val2;
	int result = val1 + val2;
	cout << "덧셈결과: " << result << std::endl;
	return 0;
}
/*출력에서와 마찬가지로 입력에서도 별도의 서식 지정이 불필요하다.*/

// C++의 지역변수 선언
#include<iostream>
using namespace std;
int main(void)
{
	int val1, val2;
	int result = 0;
	cout << "두 개의 숫자입력: ";
	cin >> val1 >> val2;
	// 이렇듯 연이은 데이터의 입력을 명령할 수 있다.
	// cin에서 가까운 변수부터 채워라 라는 의미를 갖는다.
	if (val1 < val2)
	{
		for (int i = val1 + 1; i < val2; i++)
			result += i;
	}
	// for문 안에서도 변수의 선언이 가능하다. / 지역변수 선언
	else
	{
		for (int i = val2 + 1; i < val1; i++)
			result += i;
	}
	cout << "두 수 사이의 정수 합: " << result << endl;
	return 0;
}
// cin을 통해서 입력되는 데이터의 구분은 스페이스 바, 엔터, 탭과 같은 공백을 통해서 이뤄진다.

//배열 기반의 문자열 입출력
#include<iostream>
using namespace std;
int main(void)
{
	char name[100];
	// 문자열의 입력방식도 다른 데이터의 입력방식과 큰 차이가 나지 않는다.
	char lang[200];
	cout << "이름은 무엇입니까? ";
	cin >> name;
	cout << "좋아하는 프로그래밍 언어는 무엇인가요? ";
	cin >>lang;
	cout << "내 이름은 " << name << "입니다.\n";
	cout << "제일 좋아하는 언어는 " << lang << "입니다." << endl;
	return 0;
}