/*Chapter 02-2 새로운 자료형 bool*/


/*
bool
참과 거짓 선택하는데 있어서 중요한 개념
참이나 거짓을 데이터적으로 표현할 수 있어야 한다.

정수의 경우) 0이 아닌 모든 정수는 참 / 0은 거짓 => 줄여서 1은 참 0은 거짓
#define TRUE 1
#define FALSE 0

while(True)

true -> 참을 의미 / false -> 거짓을 의미

'참'을 의미하는 true와 '거짓'을 의미하는 false

int main(void)
{
	int num=10;
	int i=0;
	cout<<"true: "<<true<<endl;
	cout<<"false: "<<false<<endl;
	while(true)
	{
		cout<<i++<<' ';
		if(i>num)
			break;
	}
	cout<<endl;
	cout<<"sizeof 1: "<<sizeof(1)<<endl;
	cout<<"sizeof 0: "<<sizeof(0)<<endl;
	cout<<"sizeof true: "<<sizeof(true)<<endl;
	cout<<"sizeof false: "<<sizeof(false)<<endl;
	return 0;
}

실행 결과
true: 1
false: 0
0 1 2 3 4 5 6 7 8 9 10
sizeof 1: 4
sizeof 0: 4
sizeof true: 1
sizeof false: 1

'true'는 '참'을 의미하는 1바이트 데이터이고, 'false'는 '거짓'을 의미하는 1바이트 데이터이다.
이 둘은 각각 정수 1과 0이 아니다. 그러나 정수가 와야 할 위치에 오게 되면, 각각 1과 0으로 변환이 된다.

*/
/*
자료형 bool

bool의 이해
-> true와 false는 bool형 데이터이다.
-> true와 false 정보를 저장할 수 있는 변수형 bool형 변수이다.
bool isTrueOne=true;
bool isTrueTwo=false;

int main(void)
{
	bool isPos;
	int num;
	cout<<"Input number: ";
	cin>>num;
	isPos=IsPositive(num);
	if(isPos)
		cout<<"Positive number"<<endl;
	else
		cout<<"Negative number"<<endl;

	return 0;
}

실행 결과
Input number: 12
Positive number
*/
