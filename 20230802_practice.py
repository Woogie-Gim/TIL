lst = [4, 3, 5, 1, 7, 5, 6, 8, 1, 6, 9, 5]

# target 이라는 리스트에 0~7 사이의 정수 3개 입력 받기
# n 이라는 변수에 1~5 사이의 정수를 입력받기

# 입력받은 정수로 부터 연속된 n개의 정수의 합이
# 맥스일 때의 정수값과 max값을 출력하시오

# 내 정답

target = list(map(int, input().split()))
n = int(input())

my_dict = {}
max_key = 0
max_sum = 0

for i in range(len(target)):
    Sum = 0
    for j in range(target[i], min(target[i] + n, len(lst))):
        Sum += lst[j]
    my_dict[target[i]] = Sum

    if Sum > max_sum:
        max_sum = Sum
        max_key = target[i]

print(f"{max_key}, {max_sum}")


# 교수님 답

target=list(map(int,input().split()))
n=int(input())

Max=-21e8
answer=0

def getsum(t):
    sum=0
    for i in range(t,t+n):
        sum+=lst[i]
    return sum

for i in range(len(target)):
    ret=getsum(target[i])
    if ret>Max:
        Max=ret
        answer=target[i]
print(answer,Max)

# 연속되는 숫자 3개의 합이 가장 클 때의 값을 출력해주세요

lst = [[4, 5, 2, 6, 7, 3, 1],
       [2, 9, 9, 6, 1, 6, 7]]

Max = -21e8
def getsum(y, x):
    Sum = 0
    for i in range(3):
        Sum += lst[y][x+i]

    return Sum


for i in range(2):
    for j in range(5):
        ret = getsum(i, j)
        if ret > Max:
            Max = ret

print(Max)

# 3 4 5 라는 패턴이 어느 좌표에 있는지 찾기!!

lst = [[1, 2, 3, 4, 5],
       [2, 4, 2, 1, 3],
       [3, 4, 5, 2, 5]]

# 내가 다 못푼 답
"""
def getposition(y, x):
    arr = []
    Pattern = ''
    for i in range(3):
        Pattern + lst[y][x+i]
        arr.append(Pattern)
        for j in range(3):
            if arr[j] == '345':
                return 1
        return 0

dy = 0
dx = 0

for i in range(3):
    for j in range(5):
        ret = getposition(i, j)

        if ret:
            dy, dx = i, j

print(dy, dx)
"""

# 내가 수정한 답
"""
target = [3, 4, 5]

def isPattern(y, x):
    for i in range(3):
        if target[i] != lst[y][x+i]:
            return 0
    return 1

dy = 0
dx = 0
arr = []
for i in range(3):
    for j in range(3):
        ret = isPattern(i, j)
        dy = 0
        dx = 0

        if ret:
            dy, dx = i, j
            arr.append((dy, dx))

print(*arr)
"""

# 교수님 답
target = [3, 4, 5]

def isPattern(y, x):
    for i in range(3):
        if target[i] != lst[y][x+i]:
            return 0
    return 1

for i in range(3):
    for j in range(5):
        ret = isPattern(i, j)
        if ret:
            print(i, j)


# lst 안에서 target 찾기

lst = [[1, 2, 3, 4, 5],
       [2, 4, 2, 1, 3],
       [3, 4, 5, 2, 5]]

target = [[3, 4],
          [2, 1]]

def findpt(a, b):
    for i in range(2):
        for j in range(2):
            if target[i][j] != lst[a+i][b+j]:
                return 0
    return 1


for i in range(2):
    for j in range(4):
        ret = findpt(i, j)
        if ret:
            print(i, j)

# 2 * 3 배열 만큼 땅을 갖을 수 있다고 할 때 가장 큰 값을 구해라

# 내가 푼 답
"""
lst = [[1, 5, 4, 2],
       [1, 3, 4, 2],
       [3, 5, 3, 2],
       [2, 6, 4, 1]]

def findmax(a, b):
    Sum = 0
    arr = []
    for i in range(2):
        Sum = 0
        for j in range(2):
            Sum += lst[a+i][b+j]
            arr.append(Sum)

    return arr


for i in range(2):
    for j in range(3):
        ret = findmax(i, j)

print(max(ret))
"""

# 교수님 답

lst=[[1 ,5 ,4 ,2],
    [1 ,3 ,4 ,2],
    [3 ,5 ,3 ,2],
    [2 ,6 ,4 ,1]]

Max=-21e8
def getsum(a,b):
    sum=0
    for i in range(2):
        for j in range(3):
            sum+=lst[a+i][b+j]
    return sum

for i in range(3):
    for j in range(2):
        ret=getsum(i,j)
        if ret>Max:
            Max=ret

print(Max)

# DAT
"""
a = [8, 3, 5, 2, 5, 7, 2, 4]

# 4
# 1 2 3 4
# 1 : 0 개 존재 2 : 2개 존재 3 : 1개 존재 4 : 1개 존재

n = int(input())

b = list(map(int, input().split()))

for i in range(len(b)):
    cnt = 0
    for j in range(len(a)):
        if b[i] == a[j]:
            cnt += 1

    print(f'{b[i]}:{cnt}개 존재')
"""


# a 까지 입력 받는다고 생각한다면 시간 복잡도는 O(n ** 2)

# direct address table을 사용한다면 O(n)

# DAT
# Direct address table
# 빠른 검색을 위해서 사용하는 자료구조

# DAT : 배열의 값을 다른 배열의 index로 활용하는



# bucket 이라는 리스트에 전부 0값으로 초기화
# 찾는 숫자에 맞는 인덱스 위치에 1씩 증가시켜 개수를 찾는다
# 8이 존재하기 때문에 인덱스 8번에 1 증가
# bucket의 값은 a 배열에 해당 인덱스가 몇 개씩 존재하는지 적혀져 있음

a = [8, 3, 5, 2, 5, 7, 2, 4]

n = int(input())
b = list(map(int, input().split()))

bucket = [0] * 10
# bucket 등록

for i in range(len(a)):
    bucket[a[i]] += 1
    # index = a[i]
    # bucket[index] += 1
# n 번 탐색

for i in range(len(b)):
    print(f'{b[i]}:{bucket[b[i]]}개')
# m 번 탐색

# O(n + m) => O(n) 의 속도

# n 개의 정수 입력
# 어떤 값이 몇개 입력이 됐는지 출력

n = int(input())
a = list(map(int, input().split()))

bucket = [0] * 10

for i in range(len(a)):
    bucket[a[i]] += 1

for i in range(len(bucket)):
    if bucket[i] != 0:
        print(f'{i} : {bucket[i]}개 있음')


# DAT 를 이용해서 문자열 입력받아 어떤 알파벳이 몇개 사용이 되었는지 출력 해보기
# apple / a : 1개 p : 2개 l : 1개 e : 1개
# 몇 종류의 알파벳을 사용했는가? 4종류

# 문자열 -> 리스트화
# ['a', 'p', 'p', 'l', 'e']
# 소문자 a의 아스키코드값을 이용
# 200개짜리 bucket 을 만들어 index 활용 하면 메모리를 너무 많이 사용
# a : 97 -> a - a : 0번 인덱스 / 26칸 짜리 버켓 배열만 필요

# lst = list(input())
# bucket = [0] * 26
#
# for i in range(len(lst)):
#     index = ord(lst[i]) - ord('a')
#     bucket[index] += 1
#
# cnt = 0
# for i in range(26):
#     if bucket[i] > 0:
#         cnt += 1 # 몇 종류의 알파벳이 사용되었는가
#
# print(cnt)
#
# for i in range(26):
#     if bucket[i] > 0:
#         alpha = chr(i+ord('a'))
#         print(f'{alpha}가 {bucket[i]}개 사용 됨')

"""
4 7 1 4 2 4 3
counting sort
계수 정렬
O(n)
1. DAT bucket 등록
2. 누적합 구하기
3. 값 넣기

10 칸짜리 bucket 만들기

bucket = [0] * 10

각 수에 해당하는 인덱스에 해당하는 곳에 1씩 증가

증가된 값의 누적 합 구하기
0 : 0 / 1 : 1 / 2 : 1 / 3 : 1 / 4 : 3 / 5 : 0 / 6 : 0 / 7 : 1 / 8 : 0 / 9 :0
0 1 2 3 6 6 6 7 7 7 

값 넣기
-1 씩 해서 맞는 인덱스에 다시 넣어주기
4 의 누적합은 6 / 3개가 있으니 5 -> 4 -> 3

O(3n) -> O(n)

누적합이 의미하는 것은 해당 인덱스보다 작은 게 몇개 있는지 표시가 됨

그 값보다 앞에 몇개가 있는지 알기 때문에 -1 한 값이 자연스럽게 인덱스가 됨

counting sort 끝
"""

n = int(input())
a = list(map(int, input().split()))

bucket = [0] * 11
# 버켓 등록
for i in a:
    bucket[i] += 1

# 누적합 구하기
for i in range(1, len(bucket)):
    bucket[i] += bucket[i-1]

# 값넣기
result = [0] * n
for i in range(n):
    bucket[a[i]] -= 1
    index = bucket[a[i]]
    result[index] = a[i]

# 출력하기
print(*result)

"""
DAT 라는 자료구조는 빠른 검색을 위한 자료구조
100개 짜리 리스트에서 30개 짜리 리스트 값들이 존재하는 지 볼 때
2중 for 문을 사용하면 3000번 탐색

bucket 리스트를 사용하면 130번 탐색

"""

