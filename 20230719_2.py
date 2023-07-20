a = 3
b = 5 # 변수의 값을 할당한다

a, b = 3, 5
print(a + b)

# a => 5
# b => 3

# SWAP

temp = a
a = b
b = temp

print(a, b)

# 콜라와 사이다를 서로 옮겨 담고 싶을 때 빈컵 하나 더 갖다놓고 붓고 부으면 서로 컵을 바꿀 수 있음

a, b = 3, 5
a, b = b, a
print(a, b)

# SWAP 함수보다는 직접 입력하는 것이 속도 측면에서도 유리할 수 있음

# boolean
a, b = 0, -1
a = bool(a)
b = bool(b)

print(a, b)
# boolean 타입에선 0은 False, 0 이외의 모든 정수값은 True

a = ''
b = '11'

print(bool(a), bool(b))
# boolean 타입에선 빈 문자열은 False, 어떤 문자가 들어간 문자열은 True

a = 3
print(type(a)) #int

a = 3.14
print(type(a)) #float

# 반올림
print(round(a,1)) # 소수 n번째 자리까지 출력 # round 반올림
# #math 모듈을 불러왔을 때 math.floor 내림 / math.ceil 올림

print(f'{a:.1f}') #f-stirng 이용 몇번째 자리까지 출력할지 적어주면 된다

# 파이썬에서 실수를 다룰 땐 정확한 값을 구할 수 없다
a = 3.15
print(round(a, 1)) # 3.2가 아닌 3.1로 출력됨
# 1. 컴퓨터는 이진수로 연산 -> 고정소수점, 부동소수점 를 통해서 실수 (소수점을 표현)
# 부동소수점을 이용해서 실수를 표현 -> 정확한 계산을 해서 표현하는 것이 아니라 '근사값'을 이용해서 표현 -> 부정확
# floating point error

a = 1.2  - 1.1
print(a) #0.09999999999999987

# 사사오입 (사까지는 죽이고 오부터는 올림)
# 파이썬에선 오사오입

print(round(0.5)) #0
print(round(1.5)) #2
print(round(2.5)) #2
print(round(3.5)) #4
print(round(4.5)) #4
print(round(5.5)) #6
# 실수값을 -> 정수값으로 바꿀시
# 소수점 첫번째 자리 일 때 5 앞에 첫번째 정수가 짝수면 내림, 홀수면 올림 처리 해버림
# 소수점 첫번째 자리가 4이하 일때는 내림
# 소수점 첫번째 자리가 6이상 일때는 반올림(우리의 의도대로 작동)

print(round(0.05, 1)) #0.1
print(round(0.15, 1)) #0.1
print(round(0.25, 1)) #0.2
print(round(0.35, 1)) #0.3
print(round(0.45, 1)) #0.5
print(round(0.55, 1)) #0.6
# 소수 2번째 자리에서 반올림 할 경우 -> 오사오입이 통하지 않음
# 그이유는 파이썬이 부동소수점을 이용을 해서 실수를 표현하는 과정 중에
# 정확한 값이 아니라 '근사값'으로 계산을 하기 때문에 정확한 계산을 못함

print(round(0.50000, 1)) #0.5
print(round(1.50000, 1)) #1.5
print(round(2.50000, 1)) #2.5
print(round(3.50000, 1)) #3.5
print(round(4.50000, 1)) #4.5
print(round(5.50000, 1)) #5.5

# 반올림을 하라고 했을 경우 어떻게 처리를 해야 하는가?
# 1. 전부 0.5를 더하고 내림 처리 하면 원하는 반올림이 이루어진다
import math

print(math.floor(0.5+0.5)) #1
print(math.floor(1.5+0.5)) #2
print(math.floor(2.5+0.5)) #3
print(math.floor(3.5+0.5)) #4
print(math.floor(4.5+0.5)) #5
print(math.floor(5.5+0.5)) #6

# 2. 부동소수점의 버그를 활용한 '꼼수' : 임의의 작은수를 더해서 원하는 반올림을 이끌어냄
print(round(0.05 + 0.00001, 1)) #0.1
print(round(0.15 + 0.00001, 1)) #0.2
print(round(0.25 + 0.00001, 1)) #0.3
print(round(0.35 + 0.00001, 1)) #0.4
print(round(0.45 + 0.00001, 1)) #0.5
print(round(0.55 + 0.00001, 1)) #0.6

# 지수표기법 활용
print(round(0.05 + 1e-10, 1)) #0.1
print(round(0.15 + 1e-10, 1)) #0.2
print(round(0.25 + 1e-10, 1)) #0.3
print(round(0.35 + 1e-10, 1)) #0.4
print(round(0.45 + 1e-10, 1)) #0.5
print(round(0.55 + 1e-10, 1)) #0.6

# 3. decimal 모듈을 사용하는 방법 : 파이썬에서 가장 정확하게 실수를 표현하는 방법
# 속도가 상당히 느림

# 문자열

# "순서" 개념이 있는 자료형 -> 문자열 list tuple range
# index가 존재한다
print('오늘은 컨디션이 "100%" 입니다.')
print('오늘은 컨디션이 \"100%\" 입니다.')

s = "abcdefg"
print(s[:3]) #abc / 3전까지
print(s[3:]) #defg / 3부터 끝까지
print(s[2:5]) #cde / 2부터 5번전까지
print(s[5:2:-1]) #fed /5번부터 2번전까지 1씩 감소
print(s[2:5:2]) #ce /2번부터 5번전까지 2씩 증가
print(s[::-1]) #gfedcba #역순으로 슬라이싱해서 출력
print(s[-2]) #f #-2 인덱스

st ='abcdefg'
print(st + 'asdf')

# 문자열에 인덱스라는 개념이 적용되지만 바꿀 수 없다고 일반적으로 통용

ret = st.replace('d', 'ddddddddd')
print(ret)

# 리스트
lst = [1, 2, 3, 4]
print(type(lst))
print(lst)
print(len(lst))
print(lst * 3) #리스트 연산도 가능

lst = [1, 2, 3, 4, [5, 6, 7], 8]

print(lst[4][0]) #5
print(lst[-2][-3]) #5

print(list(range(3))) #[0, 1, 2]
print(list(range(3, 6))) #[3, 4, 5]
print(list(range(3, 8, 2))) #[3, 5, 7]

# tuple
tp = (1, 2, 3, 4, 5)
print(tp)
print(type(tp))
print(tp[1])
print(len(tp))
print(tp[-1])
# 튜플 -> 값 변경 불가 !!!

# dictonary
di = {1: 3, 2: {4: 5}, '학': 6, '교': [7, 8, 9]}
print(di)
print(type(di))

print(di[1])
print(di[2][4])
di[1] = 5 # value 바꾸기
print(di)
di[111] = di.pop(1) #key 바꾸기 # di 라는 dictonary에 1 키값을 제거함과 동시에 111 키값을 다시 채워 넣음

# key: value 를 한쌍으로 자료를 저장하는 dictonary
# hash


# 순서의 개념이 무색한 자료형 -> set dictonary
# index가 존재하지 않음

# set
s = {1, 2, 3, 4, 5, 6}
print(s)
print(type(s))

# set -> 순서없음, 중복을 제거할 때 사용하기 좋은 자료형
lst = [1, 1, 2, 2, 1, 1, 5, 4, 3, 3, 3, 4, 6, 3, 1, 2]
lst = list(set(lst))
print(lst)

s = {1, 2, 3}
s2 = {3, 4, 5}
print(s | s2) # 합집합
#C나 자바 같은 경우 or을 |(파이프 라인) 을 사용

print(s - s2) # 차집합

print(s & s2) # 교집합

# 논리연산
a = True
b = False
c = True
d = False
print(a and b) # and 앞과 뒤 모두 참일 경우 참 / and 연산자는 둘 다 조건을 만족해야한다
print(a and c)
print(a or b) # or 둘 중 하나만 참이여도 참 / or 연산자는 둘 중 하나만 조건을 만족해도 된다

a = bool('0') #문자열
print(a)

# 논리연산

# 논리연산의 단축평가
print('a' and 'b') #b 둘다 확인 후 마지막에 참이였던 b를 출력
print('' and 'b') #빈칸 앞이 False 였기 때문에 뒤를 보지도 않고 빈문자열을 출력함
print(0 and 1) #0 0이 False 였기 때문에 뒤도 보지도 않고 0 출력

vowels = 'aeiou'

print(('a' and 'b') in vowels) #False / b가 출력되었지만 vowels 안에 없기 때문에 False
print(('b' and 'a') in vowels) #True / 둘다 참이여서 a가 출력

print(5 or 3) # 앞이 참이여서 5 출력

# 연산자 우선순위
result = 10 % 3 + 2 ** 2
print(result)

# = : 할당 연산자 / >= <= 크거나 같다 작거나 같다

result = -3 ** 2
print(result)

# 객체 비교하는 is
a = 2
b = 2
if a is b:
    print('정답')
else:
    print('오답')

a = 2
b = 2.0
if a is b:
    print('정답')
else:
    print('오답')

# is 가 곧 '=='는 아니다
# is는 객체 (주소값)를 비교 해준다

# 함수
# 기능을 수행하는 코드들의 묶음

# 두수의 합을 출력하는 함수

def getsum(a, b):    #Parameter 매개변수
    return a + b #반환

ret = getsum(3, 5) #함수를 호출할 때 값까지 같이 보냄 argument(인자값)
# getsum 함수를 호출하고 값을 반환 받음
print(ret) # main 함수에서 출력이 됨

def getsum2(a, b):
    return a + b
    return a * b #첫번째 반환이 된 순간 함수가 종료되어 곱은 출력이 되지 않는다

ret2 = getsum2(3, 5)
print(ret2)

def getsum3(a, b):
    return a + b, a * b #파이썬의 경우에만 가능 / 하나의 튜플로 묶여 출력이 됨
ret3 = getsum3(3, 5)

print(ret3)
print(type(ret3))

def getsum4(a, b):
    return #None이 입력됨

ret4 = getsum4(3, 5)
print(ret4)

def getsum5(a, b, c = 20):   #default parameter 보통 사용할 때 일반 매개변수보다 맨 뒤에 사용
    return a + b + c

ret5 = getsum5(3, 5)
print(ret5)

# 패킹
num = [1, 2, 3, 4, 5] # 하나의 변수에 값을 여러개 할당하는 것을 패킹
num2 = (1, 2, 3, 4, 5)
print(num, num2)

# 언패킹
a, b, c, d, e = num # 묶여 있는 것을 푸는 것
print(a, c, d)
# 언패킹 하고 남는 값은 * 를 이용해서 리스트에 담을 수 있다.
# * : astrisk / astral

a, b, *c = num
print(a, b, c)  #astrisk 된 리스트 까지 출력 1 2 [3, 4, 5]

a, *b, c = num
print(a, b, c) # 1 [2, 3, 4] 5

# 튜플로 해도 잘 작동된다

# 인자값과 매개변수 값의 개수가 맞지 않은 경우
def getsum6(*a): #type(a) : <class 'tuple'>
    return a[0] + a[1] + a[2]

ret6 = getsum6(3, 5, 1)
print(ret6)

# 딕셔너리 사용
di = {'kevin': 1, 'bob': 2, 'john': 3}

def print_info(**args):
    print(args)
    print(type(args))
    for i, j in args.items(): #items라는 method를 사용하면 딕셔너리의 key와 value를 모두 반환
        print(i, j)

print_info(kevin = 1, bob = 2, john = 3) #key = value 로 인자값을 보낼 수도 있음

print_info(**di)

# 변수 scope (범위) : 변수가 작동하는 유효한 범위가 있다
# 지역변수 / 전역변수

# 지역변수

def abc():
    aa=3
    bb=5
    print(aa, bb) #aa, bb는 abc() 함수에서만 유효한 변수

abc()
# print(aa, bb) #aa, bb라는 변수는 존재하지 않음

aa = 6
def abc():
    aa=3
    bb=5
    print(aa, bb)

abc()
print(aa) #main 함수에서의 aa 이기 떄문에 6 출력
# 함수 안의 aa와 main 함수의 aa는 별개의 변수

aa = 6
def abc():
    global aa #전역변수 선언
    aa=3 #main 함수의 aa와 같은 변수가 되었기 때문에 aa 는 3으로 변환
    bb=5
    print(aa)

abc()
print(aa)

def kfc():
    global aa, bb
    print(aa, bb) #전역변수를 선언하지 않는다면 kfc() 함수 안에선 aa, bb의 변수가 정의가 안되었기 때문에 버그 발생
    aa+=1
    bb+=1
    print(aa, bb)

def test():
    global aa, bb
    aa = 3
    bb = 5
    print(aa, bb) #3, 5

test()
kfc()

#직접 정의 -> 호출 : 사용자 정의 함수

# 내장함수 map() zip() filter() lambda()

# map - 리스트나 튜플과 같이 순회 가능한 데이터 값에 함수를 일괄적으로 적용
#     - 적용 후 map이라는 객체를 반환한다

num = ['1', '2', '3']
lst = []

for i in num:
    lst.append(int(i))

print(lst)

lst2 = map(int, num)
print(list(lst2))

# a, b, c =map(int, input().split())
# print(a, b, c)

# zip - 순회 가능한 객체를 인자로 받고
#     - 각각의 값을 잘라서 튜플을 원소로 하는 객체 반환

a = '12345'
b = 'qwert'

ret = zip(a, b)
print(ret)
print(list(ret)) #[('1', 'q'), ('2', 'w'), ('3', 'e'), ('4', 'r'), ('5', 't')]

a = '12345'
b = 'qwert'
c = 'asdfq'

for i in zip(a, b, c):
    print(i)

for i in zip(a, b, c):
    print(list(i))

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in zip(arr[0], arr[1], arr[2]):
    print(list(i))

# filter
# 리스트나 튜플 같이 순회 가능한 데이터값들에 함수를 적용
# 적용 후 True 인 값만 반환하는 함수

num = [1, 2, 3, 4, 5, 6, 7, 8]
# 짝수만 리스트에 담아서 출력
def get_even(value):
    if value % 2 == 0: return True
    else: return False
    #return True if value % 2 == 0 else False

ret = filter(get_even, num)
print(list(ret))

# lambda (익명 함수) : 말그대로 함수 이름이 없는 함수

def Sum(a, b):
    return a + b

result = Sum(3, 5)
print(result)

result = (lambda a, b: a + b)(3, 5)
print(result)
# 일회성으로 쓰고 버릴 함수들을 lambda로 표현

lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 10]

# var 1 - for문 이용
lst3 = [0] * 5
for i in range(5):
    lst3 = lst1[i] + lst2[i]
print(lst3)

# var 2 - lambda 함수 이용

result = (lambda x, y : x + y)
lst3 = map(result, lst1, lst2)
print(lst3)

lst3 = map(lambda x, y : x + y, lst1, lst2)
print(lst3)

# 재귀 함수 (재귀 호출) : 함수 자기 자신이 계속 자기 자신을 호출

# main 함수에서 abc함수 호출 abc 함수에서 abc 함수 호출
# 항상 함수가 return 됐을 때 호출된 함수로 돌아간다

def abc(level):
    if level == 2:
        return
    print(level, end=" ")
    abc(level + 1)
    print(level, end=" ")

abc(0)


# 1개의 주사위를 던졌다 1~6 중 하나 출력
# for i in range(6):
#     print(i+1)
#
# # 2개의 주사위를 던졌다
# for i in range(1, 7):
#     for j in range(1, 7):
#         print(i, j)

# n개의 주사위를 던졌다 