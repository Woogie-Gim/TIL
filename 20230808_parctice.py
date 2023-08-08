# def abc(level):
#     if level == 2:
#         return
#
#     for i in range(3):
#         abc(level + 1)
#
#     # abc(level + 1)
#     # abc(level + 1)
#     # abc(level + 1)


# def abc(level):
#     print('#', end=' ')
#     if level == 2:
#         return
#
#     for i in range(2):
#         abc(level + 1)
#     print('#', end=' ')
#
# abc(0)


# 누적합
# 재귀로 구현하기


# # 방법 1) sum을 매개변수로 놓고 누적합 출력하기
# def abc(level, sum):
#     print(sum, end = ' ')
#     if level == 5:
#         return
#     abc(level + 1, sum + arr[level + 1])
#     # abc(level + 1, sum += arr[level + 1]) -> 3이 7로 바뀐 다음에 함수에 들어감 3출력 불가
#
#
# arr = [3, 4, 5, 1, 6, 9]
#       #0  1  2  3  4  5
#
# abc(0, arr[0]) # level sum
#
# # 방법 2) sum 전역변수
#
# sum = arr[0]
# def abc(level):
#     global sum
#     print(sum, end = ' ') # 들어가면서 누적합 출력
#     if level == 5:
#         return
#     sum += arr[level + 1]
#     abc(level + 1)
#
#
# abc(0) # level


# 누적합 거꾸로 출력하기
# 방법 1)

# def abc(level, sum):
#     if level == 5:
#         print(sum, end=' ')
#         return
#     abc(level + 1, sum + arr[level + 1])
#     print(sum, end = ' ')
#
#
# arr = [3, 4, 5, 1, 6, 9]
#       #0  1  2  3  4  5
#
# abc(0, arr[0]) # level sum


# 방법 2)

# arr = [3, 4, 5, 1, 6, 9]
# sum = arr[0]
# def abc(level):
#     global sum
#     if level == 5:
#         print(sum, end = ' ')
#         return
#     sum += arr[level + 1] # sum 값이 함수에 들어갈 때 더해진 채로 들어감 level1 일 때 7로 들어감
#     abc(level + 1)
#     sum -= arr[level + 1]
#     print(sum, end = ' ')
#
#
# abc(0) # level


# 3 7 1 2로 이루어진 무작위 카드 뭉치 3개에서 각 묶음 에서 한장씩 뽑았을 때 합이 10장이 되는 경우의 수

#                             O
#                         3  7  1  2
#                      3712 3712 3712 3712
#                            ....


# Sum 을 매개변수로 놓았을 때
# cnt = 0
# def abc(level, Sum):
#     global cnt
#     if level == 3:
#         if Sum == 10:
#             cnt += 1
#         return
#
#     for i in range(4):
#         abc(level + 1, Sum + (card[i]))
#
#
# card = [3, 7, 1, 2]
# abc(0, 0) # level, Sum
# print(cnt)

# Sum을 전역변수로 놓았을 때

# arr = [3, 7, 1, 2]
# cnt = 0
# Sum = 0
#
# def abc(level):
#     global cnt, Sum
#
#     if level == 3:
#         if Sum == 10:
#             cnt += 1
#         return
#
#     for i in range(4):
#         Sum += arr[i]
#         abc(level + 1)
#         Sum -= arr[i]
#
# abc(0) #level
# print(cnt)

# 3, 4, 1, 7, 6 숫자가 섞여 있는 n개의 카드 묶음에서 카드를
# 각각 1장씩 뽑아서 더했을 때 합이 10 이하로 나오는 경우는 몇가지 일까요?

# branch 는 배열의 개수 / level 이 n

# arr = [3, 4, 1, 7, 6]
# cnt = 0
# n = int(input())
#
# def abc(level, Sum):
#     global cnt, n
#     if Sum > 10:
#         return
#     if level == n:
#         if Sum <= 10:
#             cnt += 1
#         return
#
#     for i in range(5):
#         abc(level + 1, Sum + arr[i])
#
# abc(0, 0)
# print(cnt)


"""
재귀 함수가 다녀간 경로 출력하기

A B C D
로 섞인 카드 뭉치 3개에서 무작위로 카드를 뽑는다

AAA
AAB
AAC
.
.
.
DDD

path 배열마다 재귀 경로를 지나갈 때마다 추가
"""

# arr = ['A', 'B', 'C', 'D']
# path = [''] * 3
#
# def abc(level):
#     if level == 3:
#         for i in range(level):
#             print(path[i], end = ' ')
#         print()
#         return
#     for i in range(4):
#         path[level] = arr[i]
#         abc(level + 1)
#
# abc(0)

# n개의 주사위를 던졌을 때 나올 수 있는 모든 경우의 수


"""
내 코드
n = int(input())
arr = [1, 2, 3, 4, 5, 6]
path = [0] * n

def abc(level):
    global n
    if level == n:
        for i in range(level):
            print(path[i], end = ' ')
        print()
        return

    for i in range(6):
        path[level] = arr[i]
        abc(level + 1)

abc(0)
"""

# 교수님 코드

# level = n / branch = 6
# 경로 출력

n = int(input())
path = [0] * n

def abc(level):
    if level == n:
        for i in range(n):
            print(path[i], end = ' ')
        print()
        return
    for i in range(6):
        path[level] = i + 1
        abc(level + 1)

abc(0)