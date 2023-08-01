"""
문제 1
flag 변수 응용
flag - 변수 어떠한 변수가 존재하는지 볼 때

arr = [list(map(int, input().split()) for _ in range(3))]

target = int(input())


내 답안

for i in arr:
    for j in i:
        flag = 0
        if target in j:
            print('존재')
        else:
            print('존재하지않음')
        flag = 1
        break

교수님 답안

flag =0
for i in range(3):
    for j in range(4):
        if arr[i][j] == target:
            flag = 1
            break
    if flag == 1:
        break

if flag:
    print('존재함')
else:
    print('없음')
"""


"""
2번 문제

# 4 2 3 5
# 5 7 6 1
# 1 1 2 3

arr = [list(map(int, input().split())) for _ in range(3)]

# 값의 6의 좌표를 출력해 주세요. => for 문 돌려서 6의 위치 찾기

dy = 0
dx = 0

flag = 0
for i in range(3):
    for j in range(4):
        if arr[i][j] == 6:
            dy = i
            dx = j
            flag = 1
            break
    if flag: break

print(dy, dx)
"""

"""
# 3번 문제. 몇 번째 행의 합이 가장 클까요?

arr = [list(map(int, input().split())) for _ in range(3)]

Sum = 0
Max = -21e8
Maxindex = 0
for i in range(3):
    Sum = 0
    for j in range(4):
        Sum += arr[i][j]
        if Sum > Max:
            Max = Sum
            Maxindex = i + 1
print(Maxindex, Max)
"""

"""
# 4번 문제. 몇 번째 열의 합이 가장 작을까요?

arr = [list(map(int, input().split())) for _ in range(3)]

Sum = 0
Min = 21e8
Minindex = 0

for j in range(4):
    Sum = 0
    for i in range(3):
        Sum += arr[i][j]
        if Sum < Min:
            Min = Sum
            Minindex = j + 1

print(Minindex, Min)
"""
"""
# 5번 문제. 리스트에 숫자 6개 입력받고 누적합 구하기

# 내 답안

lst = list(map(int, input().split()))

my_lst = []

a = 0
for i in range(len(lst)):
    a += lst[i]
    my_lst.append(a)

my_lst.sort(reverse = True)

print(*my_lst)

# 교수님 답안

lst = list(map(int, input().split()))

for i in range(1, 6):
    lst[i] += lst[i-1]

for i in range(5, -1, -1):
    print(lst[i], end = ' ')
"""
"""
# 6번 문제. st = 'apple'  입력받은 n 만큼 문자열을 우측으로 회전시킨 후 결과 값 출력하기

st = input()
lst = list(st)
n = int(input())
slen = len(st)

for i in range(n%slen): # n번 회전
    temp = lst[slen - 1] # 마지막 있는 문자 저장
    for j in range(slen-1, 0, -1):
        lst[j] = lst[j-1] # 우측으로 문자 밀기
    lst[0] = temp # 다 밀고 난 후 저장해 놓은 값 0번 인덱스에 넣기

print("".join(lst))

st = 'apple'
n = int(input())
n = n%len(st)
st = st[n-1:]+st[:n-1] 
print(st)
"""

"""
# 7번 문제 target 배열이 lst 배열안에 존재여부 출력 Y / N

lst = [[4, 2, 3, 5],
       [1, 1, 2, 3],
       [4, 7, 6, 4]]
target = [list(map(int, input().split())) for _ in range(2)]


def isExist(value):
    for i in range(3):
        for j in range(4):
            if lst[i][j] == value:
                return 1

        return 0


for i in range(2):
    for j in range(2):
        ret = isExist(target[i][j])
        if ret == 1:
            print('Y', end='')
        else:
            print('N', end='')

        print()
"""
"""
# 8번 문제 target 배열에 있는 수가 lst 배열에 몇개 있는지

lst = [[4, 2, 3, 5],
       [1, 1, 2, 3],
       [4, 7, 6, 4]]

target = [[8, 4],
          [2, 9]]

def isCnt(value):
    count = 0
    for i in range(3):
        for j in range(4):
            if lst[i][j] == value:
                count += 1
    return count

for i in range(2):
    for j in range(2):
        cnt = isCnt(target[i][j])

        print(f'{target[i][j]}:{cnt}')
"""

"""
디버깅 단축키 [파이참]
Ctrl + F8 : Toggle breakpoint
shift + f9 : 디버깅 시작
Ctrl + F2 : 디버깅 종료
F8 : Step over
F7 : Step into
F9 : resume (다음 break point까지 실행)
"""

# 디버깅 debugging
# 버그 찾는 행위

# 가장 먼저 breakpoint를 찍을 예정
# breakpoint 찍기 전까지 디버깅이 실행
# step over : 한줄 씩 실행
# step into : 함수 안으로 진입
# resume : 다음 break point 까지 실행

def abc(y, x):
    z = y + x
    return z

a = 10
b = 20
b = 30
b = 40
b = 50
b = 60
ret = abc(a, b)

print(ret)

lst=[[4,2,3,5],
     [1,1,2,3],
     [4,7,6,4]]

target=[[8,4],
        [2,9]]

def isCnt(value):
    cnt=0
    for i in range(3):
        for j in range(4):
            if lst[i][j]==value:
                cnt+=1
    return cnt

for i in range(2):
    for j in range(2):

        cnt=isCnt(target[i][j])
        print(f'{target[i][j]}:{cnt}')
  
  