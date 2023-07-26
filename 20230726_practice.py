# 객체 지향 프로그래밍이란?         /  절차 지향 프로그램 -> 객체의 개념 x 한줄한줄씩 실행을 하면서 프로그램이 작동되는
# OOP 기초 (Object Oriented Programming)
# 객체 / 인스턴스/ 메서드 / 속성 / 클래스 / 생성자함수 (init)
# 속성 : 클래스변수 / 인스턴스변수
# 메서드 : 인스턴스메서드 / 클래스메서드 / 정적메서드

# 객체지향 프로그래밍이란? object oriented programming

# 객체?

# lol 게임 하나를 개발한다고 가정
# 게임 - 게임 캐릭터 (아리, 올라프, 빅토르...)
# 각 캐릭터 별로 hp mp 스킬 ...

"""
이름 : 올라프
hp : 100
mp : 50
스킬
q = 도끼던지기()
w = 공격력강화()
e = 도끼로 상대편 머리 찍기()


이름 : 아리
hp : 50
mp : 100
스킬
q = 구슬던지기()
w = 이동속도 빨라지기()
e = 상대방 유혹하기()

<class>
이름 : (올라프, 아리) 등은 객체 -> 게임 캐릭터라는 class의 인스턴스
hp :
mp :
스킬
q =
w = 
e =

위에 보이는 이러한 틀을 클래스라고 하고
클래스를 통해서 만든 게임 캐릭터 -> 객체 라고 하는데
이 객체를 또 다른 말로 클래스의 인스턴스라고 표현한다.

이처럼 틀을 만들어서 개발을 하면 빠른 속도로 개발이 가능하다. 재사용성이 좋다.

절차지향 프로그래밍 vs 객체지향 프로그래밍

인스턴스 커피를 3명이 타 먹는다고 가정
절차 : 직접 타먹는 아놀로그 방식
한명이 뜨거운물을 붓고 있으면
변수가 데이터를 접근할 때 기다리지 않고 메모리에 바로 접근

객체지향 : 커피 자판기
변수가 데이터를 접근할 떄 순서를 기다려야함
단점 : 개발속도는 빠르지만 개발한 프로그래밍 실행속도는 느리다
장점 : 재사용성, 확장성이 좋다, 유지보수가 편하다

lol -> 클래스를 lol2로 이식
lol2 -> 게임캐릭터 // 맵 // 아이템
"""

class Calculator():
    numberofCalcul = 0 #속성 / 클래스 변수 / 전역변수 느낌
                       # 클래스 안에 있는 함수들을 method __init__() / getsum()
    def __init__(self):         # __init__ 생성자 함수 내가 instance 하나를 만들면 자동으로 실행되는
        #self 클래스를 사용하고 있는 인스턴스를 의미
        self.result = 0 #속성 / 인스턴스 변수 / 지역변수 느낌
        Calculator.numberofCalcul += 1
        #인스턴스 생성될 때마다 변수값 1 증가 -> 클래스 안에 인스턴스가 총 몇개 존재하는지를 암시

    def getsum(self, value):
        self.result += value
        return self.result

cal1 = Calculator() # Calculator 라는 클래스의 인스턴스


print(cal1.getsum(3)) # 3
print(cal1.getsum(4)) # 7
print(cal1.getsum(5)) # 12
# 인스턴스변수 - 인스턴스 개인이 개별적으로 가지고 있는 속성

cal2 = Calculator() # 클래스 변수는 공유하지만 / 인스턴스 변수는 독립적인 존재
print(cal2.getsum(6)) # 6
print(cal2.getsum(7)) # 13
print(cal2.getsum(8)) # 21

# 클래스변수 - 한 클래스안의 모든 인스턴스가 공유하는 속성(변수)
print(Calculator.numberofCalcul)

# 클래스 변수 사용 시 주의점!!
# 클래스 변수값을 변경할 때에는 반드시 항상 !!! 클래스명.클래스변수 형식으로 접근해야한다.

Calculator.numberofCalcul = 6
print(cal1.numberofCalcul) # 6 각각의 인스턴스 변수로 클래스변수에 접근할 수 있음
print(cal2.numberofCalcul) # 6

# 잘못된 예시 / 클래스 변수에 접근 시 인스턴스를 이용해서 접근하면 안됨!!!
cal1.numberofCalcul = 10 
# 인스턴수변수를 통해 클래스변수에 접근해서 바꿀 경우 새로운 인스턴스 변수가 생성 된 것 같은
print(cal1.numberofCalcul) # 10 
print(cal2.numberofCalcul) # 6

Calculator.numberofCalcul = 3
print(cal1.numberofCalcul) # 10
print(cal2.numberofCalcul) # 3

# 결론 : 
# 클래스 변수 : 모든 인스턴스가 공유 / 인스턴스 전체가 사용해야 하는 값을 저장할 때 사용 / 인스턴스로 접근 금지
# 인스턴스 변수 : 각 인스턴스별로 독립되어 있음 / 각 인스턴스가 따로 값을 저장해야 할 때 사용

# 메서드

# 인스턴스 메서드 : 우리가 평소에 많이 쓰던 메서드
# 정적메서드 : 클래스변수나 인스턴스 변수를 사용하지 않을 때 사용
# 클래스메서드 : 데코레이터를 사용해서 정의, 호출 시 첫번째 인자로 cls(클래스)가 사용됨

# 1. 인스턴스 메서드

class Plus_minus:
    # def data(self, first, second): #data라는 함수를 호출해야만 작동
    #     self.first = first
    #     self.second = second

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def plus(self):
        result = self.first + self.second
        return result
    
    def minus(self):
        result = self.first - self.second
        return result

    
# a = Plus_minus()
# a.data(3, 5) # self = a / a.first = 3 / a.second = 5 / data 함수를 호출 해야만 함
# b = Plus_minus()
# b.data(2, 7)
# print(a.first, b.second) # 3 7

# print(a.plus()) # a.first + a.second = 8
# print(b.minus()) # b.first - b.second = -5

a = Plus_minus(3, 5) #init 이라는 생성자 함수가 인스턴스 생성 시 자동 실행
print(a.plus())
print(a.minus())

# 매직 메서드 - 파이썬에서 함수를 만들어서 코드를 "커스터마이징" 하고 싶을 때 사용하는 메서드
# init add str 많이 사용.. 그 외에도 많이 사용 

class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __add__(self, another):
        return self.price + another.price

kia = Car('k8', 500)
bmw = Car('M5', 1000)

print(kia.price + bmw.price) # 1500
print(kia + bmw) # 1500 / add라는 매직메서드 덕에 인스턴스만 이용을 해서 두 차의 가격의 합이 출력이 가능
# 커스터마이징

# 인스턴스 삭제 !!
del bmw

# 데코레이터
# 장식한다는 의미 / 함수를 꾸밀 때 사용하는 문법

# def call_name(name):
#     print('뉴진스'*5)
#     print(name)
#     print('하입보이'*3)

# def call_age(age):
#     print('뉴진스'*5)
#     print(age)
#     print('하입보이'*3)

# call_name('김선욱')
# call_age(28)

def deco(fnc):
    def wrapper(value):
        print('뉴진스'*3)
        fnc(value)
        print('하입보이'*3)
    return wrapper

@deco
def call_name(name):
    print(name)

@deco
def call_age(age):
    print(age)

call_name('김선욱')
call_age(28)

# 정적메소드 (static)

class Car:

    @staticmethod
    def add_price(one, another):
        print(one+another)

Car.add_price(400, 800)

# 정적 메서드에는 @staticmethod 가 붙습니다.
# 그리고 인스턴스 메소드와 달리 self가 없다. 정적 메서드 사용 시 self 사용하지 않습니다.

# 정적 메서드 호출할 때는 클래스에서 바로 메서드를 호출하면 됨
# 인스턴스 없어도 문제 될 것이 없음

# self를 사용하지 않는다 !!! -> self와 같은 속성을 다루지 않고
# 함수의 행동 (기능)만 단순하게 정의하고 사용하고 싶을 때 이용하는 메서드
# 그래서 호출할 때 인스턴스 없이! 클래스명을 사용해서 호출 예시 > Car.add_price(400, 800)

# 인스턴스 있어도 접근 다 가능 (파이썬에서만)
# 실효성이 적음

a7 = Car()
a7.add_price(500, 600) # 1100

# 클래스의 인스턴스에 아무런 변화를 일으키지 않는 함수라는 것을 의미!

# 클래스 메서드

class Make_pie:
    cnt = 0
    def __init__(self, name):
        self.name = name
        Make_pie.cnt += 1

    @classmethod
    def number_of_pies(cls): #클래스 메서드에선 매개변수를 cls를 사용 / cls는 Make_pie라는 클래스를 의미
        print(f'파이를 {cls.cnt}명이 만들고 있습니다.')

a = Make_pie('Kevin')
b = Make_pie('Bob')
c = Make_pie('Kate')

Make_pie.number_of_pies()
a.number_of_pies() # 이렇게 사용하는 것을 추천하지 않습니다 / 단 작동은 된다

# 정적메서드 클래스 메서드 둘다 -> self 없음 -> 인스턴스 없이도 호출한다!
# 클래스메서드는 클래스메서드를 이용을 해서 "인스턴스 없이" 클래스 변수의 값을 바꾸고 싶을 때 사용


# 정리

"""
속성 : 클래스 송성 / 인스턴스 속성
메서드 : 인스턴스 메서드 / 정적메서드 / 클래스메서드

클래스 속성(변수)
모든 인스턴스가 공유하는 변수로써 인스턴스 모두가 사용해야 하는 값을 저장할 때 사용하는 변수
접근 시 반드시 클래스를 통해서 접근을 해야 한다. (인스턴스를 이용해서 접근하는 것은 금지!

인스턴스 속성
클래스 인스턴스가 각각 값을 따로 저장할 때 사용

인스턴스 메서드 : self를 첫번째 매개변수로 사용 (self -> 해당 클래스의 인스턴스를 의미)
정적 메서드 : 매개변수에 self 없음 / 인스턴스 없이 메서드의 순수한 기능 또는 동작만 사용하고 싶을 때 사용하는 메서드
클래스 메서드 : 매개변수에 self 없고 cls 사용 / cls를 통해서 클래스 변수의 값을 바꾸고 싶을 때 사용하는 메서드
"""