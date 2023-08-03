# delta 배열 / 방향 배열 / direct 배열

"""
[[3, 5, 4],
 [1, 1, 2],
 [1, 3, 9]]

입력 받은 좌표 기준으로 위 아래 좌우의 합을 구한다고 가정

(1, 1) -> 5 + 3 + 1 + 2
(0, 0) -> 1 + 5

일단은 배열의 범위를 벗어났다고 생각하지 말고
"""

# arr = [[3, 5, 4],
#        [1, 1, 2],
#        [1, 3, 9]]

# 1, 1 기준으로 위 아래 좌 우측에 있는 값들의 합을 구해서 출력하기

"""
1, 1 기준으로   y x
위 : 0, 1     -1 0
아래 : 2, 1    1 0
좌 : 1, 0      0 -1
우 : 1, 2      0  1
"""

# y, x = map(int, input().split())
#
# directy = [-1, 1, 0, 0]
# directx = [0, 0, -1, 1]
#
# Sum = 0
# for i in range(4):
#     dy = y + directy[i]
#     dx = x + directx[i]
#     if dy < 0 or dy > 2 or dx < 0 or dx >2: # 배열의 범위를 벗어날 경우
#         continue # continue 밑에 코드가 실행되지 않고 반복문 맨  위로 올라간다
#     Sum += arr[dy][dx]
#
# print(Sum)

# 파이썬스러운 코드
#
# arr = [[3, 5, 4],
#        [1, 1, 2],
#        [1, 3, 9]]
#
# y, x = map(int, input().split())
#
# ans = 0
# for i, j in (-1, 0), (1, 0), (0, -1), (0, 1):
#     dy, dx = y + i, x + j
#     if 0 <= dy < 3 and 0 <= dx < 3:
#         ans += arr[dy][dx]
#
# print(ans)


# arr = [[3, 5, 4, 5, 6],
#        [1, 1, 2, 7, 8],
#        [1, 2, 9, 1, 2],
#        [3, 5, 4, 5, 6],
#        [1, 1, 2, 7, 8]]
#
# y, x = map(int, input().split())
#
# directy = [-1, -1, 1, 1]
# directx = [-1, 1, -1, 1]
#
# Gop = 1
# for i in range(4):
#     dy = y + directy[i]
#     dx = x + directx[i]
#     if dy < 0 or dy > 4 or dx < 0 or dx > 4:
#         continue
#     Gop *= arr[dy][dx]
#
# print(Gop)

"""
내 코드

arr = [[3, 5, 4, 5, 6],
       [1, 1, 2, 7, 8],
       [1, 2, 9, 1, 2],
       [3, 5, 4, 5, 6],
       [1, 1, 2, 7, 8]]

y, x = map(int, input().split())

directy = [-1, -2, -3, 1, 2, 3, 0, 0, 0, 0, 0, 0]
directx = [0, 0, 0, 0, 0, 0, -1, -2, -3, 1, 2, 3]

Sum = 0
for i in range(12):
    dy = y + directy[i]
    dx = x + directx[i]
    if dy < 0 or dy > 4 or dx < 0 or dx > 4:
        continue
    Sum += arr[dy][dx]

print(Sum)
"""

# 교수님 코드
# arr = [[3, 5, 4, 5, 6],
#        [1, 1, 2, 7, 8],
#        [1, 2, 9, 1, 2],
#        [3, 5, 4, 5, 6],
#        [1, 1, 2, 7, 8]]
#
# y, x = map(int, input().split())
#
# directy = [0, 0, -1, 1]
# directx = [1, -1, 0, 0]
#
# ans = 0
#
# for i in range(4):
#     for j in range(1, 4):
#         dy = y + directy[i] * j
#         dx = x + directx[i] * j
#     if dy < 0 or dx < 0 or dy > 4 or dx > 4:
#         continue
#     ans += arr[dy][dx]
#
# print(ans)

"""
내 코드
arr= [[1, 2, 3, 4],
      [1, 2, 9, 4],
      [1, 9, 3, 9],
      [1, 2, 9, 4]]

directy = [0, 0, -1, 1]
directx = [1, -1, 0, 0]

ans = 0
a = 0
b = 0
max_ans = -21e8

for y in range(4):
    for x in range(4):
        for i in range(4):
            dy = y + directy[i]
            dx = x + directx[i]
            if dy < 0 or dy > 3 or dx < 0 or dx > 3:
                continue
            ans += arr[dy][dx]
            if max_ans < ans:
                max_ans = ans
                a, b = dy, dx

print(a, b)
"""

# 교수님 코드

# arr=[[1,2,3,4],
#      [1,2,9,4],
#      [1,9,3,9],
#      [1,2,9,4]]
#
#
# def isSum(y,x):
#     directy=[0,0,-1,1]
#     directx=[-1,1,0,0]
#     sum=0
#     for i in range(4):
#         dy=directy[i]+y
#         dx=directx[i]+x
#         if dy<0 or dx<0 or dy>3 or dx>3: continue
#         sum+=arr[dy][dx]
#     return sum
#
# Max=-21e8
# Max_i=0
# Max_j=0
# for i in range(4):
#     for j in range(4):
#         ret=isSum(i,j)
#         if ret>Max:
#             Max=ret
#             Max_i=i
#             Max_j=j
# print(Max,Max_i,Max_j)


# 4*4 배열안의 값의 합을 구할 것입니다.
# for문으로 구한 후 출력해 주세요.

# sum1= 1+1+2+3+4+5 를 하면 출력은 16이 출력이 될 것이고
# sum2= 5+4+5+2+7+1 를 하면 출력은 24가 출력이 될 것입니다.

"""
내 코드
arr = [[3, 5, 4, 5],
       [1, 1, 2, 7],
       [1, 2, 9, 1],
       [3, 5, 4, 5]]

directy1 = [-1, 0, 1, 1, 1]
directx1 = [-1, -1, -1, 0, 1]

sum1 = 0
for i in range(4):
    dy = 2 + directy1[i]
    dx = 1 + directx1[i]
    if dy < 0 or dx < 0 or dy > 3 or dx > 3:
        continue
    sum1 += arr[dy][dx]
    summ1 = sum1 + arr[2][1]

print(summ1)

directy2 = [-1, -1, -1, 0, -1]
directx2 = [-1, 0, 1, 1, 1]

sum2 = 0
for i in range(4):
    dy = 1 + directy2[i]
    dx = 2 + directx2[i]
    if dy < 0 or dx < 0 or dy > 3 or dx > 3:
        continue
    sum2 += arr[dy][dx]
    summ2 = sum2 + arr[1][2]

print(summ2)
"""
# arr = [[3, 5, 4, 5],
#        [1, 1, 2, 7],
#        [1, 2, 9, 1],
#        [3, 5, 4, 5]]
#
# sum1 = 0
# sum2 = 0
#
# for i in range(4):
#     for j in range(4):
#         if i > j:
#             sum1 += arr[i][j]
#         if i < j:
#             sum2 += arr[i][j]
#
# print(sum1, sum2)


# arr = [[3, 5, 4, 5],
#        [1, 1, 2, 7],
#        [1, 2, 9, 1],
#        [3, 5, 4, 5]]
# # sum3= 3+1+9+5 를 하면 출력은 18이 출력이 될 것이고
# # sum4= 5+2+2+3 를 하면 출력은 12가 출력이 될 것입니다.
#
# sum3 = 0
# sum4 = 0
#
# for i in range(4):
#     sum3 += arr[i][i]
#     sum4 += arr[i][3-i]
#
# print(sum3, sum4)



# sum5 에는 1시에서 7시 방향 (대각선)으로 합을 구할 시 출력 결과 : 3, 6, 6, 12, 21, 5, 5


arr = [[3, 5, 4, 5],
       [1, 1, 2, 7],
       [1, 2, 9, 1],
       [3, 5, 4, 5]]

def isSum(y, x):
    sum5 = []
    Sum = 0
    for i in range(4):
        dy = y + i
        dx = x - i
        if dy < 0 or dx < 0 or dy > 3 or dx > 3:
            continue
        Sum += arr[dy][dx]
        sum5.append(Sum)
    return sum5

for i in range(4):
    for j in range(4):
        ret = isSum(i, j)

print(*ret)

# 교수님 코드
# arr = [[3, 5, 4, 5],
#        [1, 1, 2, 7],
#        [1, 2, 9, 1],
#        [3, 5, 4, 5]]
#
# n = 4
# sum5 = [0] * (2 * n - 1)
#
# for i in range(4):
#     for j in range(4):
#         sum5[i + j] += arr[i][j]
#
# print(*sum5)

"""
알고리즘 풀이 프로세스
(대부분 대기업들 코딩테스트 3 ~ 4문제, SQL 1 ~ 2 문제)

1문제 당 40분이 걸린다고 가정

1. 문제 읽기 (8 ~ 10분)
- 제한시간과 n or m 값의 범위 먼저 확인 (시간 복잡도 계산)

- 1중 for 문 인지 다중 for 문 인지 확인 후에 맞춤형 문제 풀이 예상

- 처음에는 그냥 술술 읽기 (정독 X)

- 내가 생각한 문제와 그림이 맞는지 확인

- 문제가 익숙해졌을 때 문제를 '정독' 하기 시작

- 문제 읽을 때 주의 해야 할 워딩 '단' '~해야 한다' (이 문구 때문에 continue 등을 사용하는 등 조건이 바뀜)

- 그림이나 예제가 있으면 100% 이해 하면서 천천히 읽음

- 시험장 나왔을 때 어떤 문제 였는지 이야기를 할 수 있을 정도로 문제를 정확히 파악해야 한다

2. 설계 (12 ~ 15분)
- 무작정 코드 먼저 적는 것이 아닌 내 코드가 어떻게 될지 머리 속으로 미리 그려내야 함

- 예를 들어
(금융권에서 항상 나오는 유효성 검사 : 카드 유효 기간이 얼마까지 인데 유효한 카드인지 검사)
어떤 함수를 사용할 지 전부 설계 (생년월일 검사, 유효 기간 검사 등)

- 주석 표시로 작전(계획)을 전부 적어 놓기

- 설계가 끝났을 때 '이 문제 풀었다 혹은 이 문제 풀 수 있겠다' 라는 생각이 들어야 함

- 설계가 끝났을 때 '이 문제 풀 수 있을까' 라는 생각이 들면 70 ~ 80 %는 못품

- 옆에 신경쓰지 말고 나만의 페이스대로 설계까지 완벽히 끝내기

- 복잡한 for 문일 경우 설계 단계에서 index 계산까지 대략적으로 해놔서 구현을 해야한다

3. 구현 (5 ~ 10분)

- 설계가 꼼꼼히 됐다면 구현 하다가 멈추는 경우는 없어야 함

- 입력 받는 게 어색하다면 차라리 처음 부터 프린트나 디버깅으로 확인 후 시작

- 설계 대로 구현 하면서 파트 별로 디버깅 해가면서 제대로 적혔는지 끊임없이 확인 하면서 코드 작성
(전부 작성하고 디버깅 하려면 어디서 디버깅을 해야할지 감을 못잡음)

4. 디버깅

- 디버깅 환경은 매 시험 / 회사 마다 다르기 때문에 (복붙, IDE 사용해서 코드 옮겨 적어도 되는지, 디버깅 가능한지)
미리 체크해야 한다
"""