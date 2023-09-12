/* Chapter 02-3 참조자의 이해 */

/*
int num=10;
	변수
num이라는 메모리 공간에 10을 저장한다.

reference : 변수에 이름 하나를 더 붙여주는 개념

int ref=num
=> ref라는 변수가 새로 할당된다

int &ret=num
=> 메모리 공간이 새로 생기지 않고 num메모리 공간이 ref라는 이름도 존재하게 된다.
참조자 선언

참조한다는 것은 메모리 공간에 접근한다는 것!

ref++;

cout<<num;
11 출력

int num1=2010;
변수의 선언으로 인해서 num1이라는 이름으로 메모리 공간이 할당된다.

int &num2=num1;
참조자의 선언으로 인해서 num1의 메모리 공간에 num2라는 이름이 추가로 붙게 된다.

참조자는 기존에 변수에 붙이는 '별칭'이다. 그리고 이렇게 참조자가 만들어지면 이는 변수의 이름과 사실상 차이가 없다.
*/

/*
참조자 관련 예제와 참조자의 선언

int main(void)
{
	int num1=1020;
	int &num2=num1; 
	numn2는 num1의 참조자이다. 따라서 이후부터는 num1으로 하는 모든 연산은 num2로
	하는 것과 동일한 결고라르 보인다.
	num2=3047;
	cout<<"VAL: "<<num1<<endl;
	cout<<"REF: "<<num2<<endl;
	cout<<"VAL: "<<&num1<<endl;
	cout<<"REF: "<<&num2<<endl;
	return 0;
}

실행결과
VAL: 3047
REF: 3047
VAL: 0012FF60
REF: 0012FF60

int num1=2759;
int &num2=num1;
int &num3=num2;
int &num4=num3;
참조자의 수에는 제한이 없으며, 참조자를 대상으로 참조자를 선언하는 것도 가능하다
*/

/*
참조자의 선언 가능 범위

불가능한 참조자의 선언의 예
int &ref=20; (x)
상수 대상으로의 참조자 선언은 불가능하다.

int &ref; (x)
참조자는 생성과 동시에 누군가를 참조해야 한다.

int &ref=NULL; (x)
포인터처럼 NULL로 초기화 하는 것도 불가능하다.

정리하면, 참조자는 선언과 동시에 누군가를 참조해야 하는데, 그 참조의 대상은 기본적으로 변수가
되어야 한다. 그리고 참조자는 참조의 대상을 변경할 수 없다.

int main(void)
{
	int arr[3]={1, 3, 5};
	int &ref1=arr[0];
	int &ref2=arr[1];
	int &ref3=arr[2];
	변수의 성향을 지니는 대상이라면 참조자의 선언이 가능하다.
	배열의 요소 역시 변수의 성향을 지니기 때문에 참조자의 선언이 가능하다.
	cout<<ref1<<endl;
	cout<<ref2<<endl;
	cout<<ref3<<endl;
	return 0;
}

실행결과
1
3
5
*/

/*
포인터 변수 대상의 참조자 선언

int main(void)
{
	int num=12;
	int *ptr=&num;
	int **dptr=&ptr;

	int &ref=num;
	int *(&pref)=ptr;
	int **(&dpref)=dptr;
	ptr과 dptr 역시 변수이다. 다만 주소값을 저장하는 포인터 변수일 뿐이다.
	따라서 이렇듯 참조자의 선언이 가능하다.
	
	cout<<ref<<endl;
	cout<<*pref<<endl;
	cout<<**dpref<<endl;
	return 0;
}

실행결과
12
12
12
*/