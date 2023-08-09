# n = int(input())
# arr = [1, 2, 3, 4]
# path = [0] * n
#
# def abc(level):
#     if level == n:
#         for i in range(n):
#             print(path[i], end = ' ')
#         print()
#         return
#
#     for i in range(4):
#         path[level] = arr[i]
#         abc(level + 1)
#
#
# abc(0)

# 순열
"""
한 번 뽑았던 카드는 중복해서 뽑지 않는 경우
뽑았던 카드인지 체크 하면서 재귀를 나아감
used or visited 배열 만들어줌

used Index
0 1 2 3
A B C D

A 를 지났을 때 0번 인덱스에 1 체크를 하고 진행
지나갈 때마다 1 체크
return 될 때 체크 된 곳을 0 으로 다시 바꿔줌
"""


# 중복순열 => 그냥 모든 경우의 수를 다 출력 !!! (주사위 던지기)

# 순열 => 올림픽 금, 은, 동
# n = int(input())
# card = ['A', 'B', 'C', 'D']
# path = [0] * n
# used = [0] * len(card)
#
# def abc(level):
#     if level == n:
#         for i in range(n):
#             print(path[i], end = ' ')
#         print()
#         return
#
#     for i in range(4):
#         if used[i] == 1: # 체크 되어 있는 곳을 들어가는 것을 막음
#             continue
#         path[level] = card[i]
#         used[i] = 1
#         abc(level + 1)
#         used[i] = 0 # 돌아올 때 다시 체크 되어 있는 곳을 0으로 바꿔줌
#
# abc(0)


# 조합 (nCm)

"""
              main
           A              B                C              D
    A    B   C   D  A   B   C   D   A   B    C   D   A  B   C    D
ABCD ABCD ABCDABCD ABCDABCDABCDABCD ABCDABCDABCDABCD ABCDABCDABCDABCD
 
나올 수 있는 조합
ABC
.
.
.
BCD (A에 들어갈 필요가 없음)

그 전에 들어왔던 가지 +1 하면서 탐색
"""

# 중복 순열로 셋팅을 해놓고 코드를 어떻게 추가하면 되는지
# 조합 => 농구팀을 예로 들었음

# 첫번째 방법 : 전 브랜치에서 체크된 level - 1 번 인덱스와 앞으로 들어갈 것을 비교
# n = 3
# path = [''] * n
# card = ['A', 'B', 'C', 'D']
#
# def abc(level):
#     if level == n:
#         for i in range(n):
#             print(path[i], end = ' ')
#         print()
#         return
#
#     for i in range(4):
#         if level > 0 and path[level - 1] >= card[i]:
#             continue
#         # 전 브랜치보다 +1 을 탐색해서 나가기 때문에 level - 1 번 인덱스 보다 card[i]가 작으면 탐색할 필요가 없다
#         path[level] = card[i]
#         abc(level + 1)
#
#
# abc(0)

# 값이 오름차순이 아닌 경우
# 반복문을 돌릴 때 다음 브랜치로 가서 인덱스도 전 인덱스 다음부터 탐색하면 가능

# n = 3
# path = [''] * n
# card = ['A', 'B', 'C', 'D']
#
# def abc(level, start):
#     if level == n:
#         for i in range(n):
#             print(path[i], end = ' ')
#         print()
#         return
#
#     for i in range(start, 4):
#         path[level] = card[i]
#         abc(level + 1, i + 1)
#
#
# abc(0, 0)

# 중복 조합 (112 == 121)
"""
1, 2, 3, 4로 중복 조합 만들기

111
112
113
114
122
123
124
133
134
144
222
.
.
.

들어갔던 가지 '에서' 부터 다시 시작
"""

# n = 3
# path = [''] * n
# card = ['A', 'B', 'C', 'D']
#
# def abc(level, start):
#     if level == n:
#         for i in range(n):
#             print(path[i], end = ' ')
#         print()
#         return
#
#     for i in range(start, 4):
#         path[level] = card[i]
#         abc(level + 1, i)
#
#
# abc(0, 0)

# 중복 순열을 출력하는데 특정 문자로 시작하는 문자는 전부 제외

# n = 3
# path = [''] * n
# card = ['A', 'B', 'C', 'D']
#
# def abc(level, start):
#     if level == 1 and path[level - 1] == 'B': # 진입 후 리턴 하는 코드
#         return
#     if level == n:
#         for i in range(n):
#             print(path[i], end = ' ')
#         print()
#         return
#
#     for i in range(4):
#         # if level == 0 and card[i] == 'B': # 아예 진입을 하지 않는 경우
#         #     continue
#         path[level] = card[i]
#
#         abc(level + 1, i)
#
# abc(0, 0)


# 중복 순열 / 연속해서 같은 카드 뽑지 않는 경우 모두 출력

# n = 3
# path = [''] * n
# card = ['A', 'B', 'C', 'D']
#
# def abc(level, start):
#     if level > 1 and path[level - 1] == path[level - 2]: # 2번 방법 진입 후 리턴하는 경우
#         return # 일단 진입을 했기 때문에 전 배열과 전전배열이 같으면 리턴
#     if level == n:
#         for i in range(n):
#             print(path[i], end = ' ')
#         print()
#         return
#
#     for i in range(4):
#         path[level] = card[i]
#         # if level > 0 and path[level - 1] == card[i]: # 1번 방법 진입을 안하는 경우
#         #     continue
#         abc(level + 1, i)
#
# abc(0, 0)


# 중복 순열 / 뽑았을 때 'C'는 제외 하고 출력

n = 3
path = [''] * n
card = ['A', 'B', 'C', 'D']

def abc(level, start):
    if level > 0 and path[level - 1] == 'C': # 진입 후 리턴 하는 경우
        return
    if level == n:
        for i in range(n):
            print(path[i], end = '')
        print()
        return

    for i in range(4):
        # if card[i] == 'C': # 진입을 안하는 경우
        #     continue
        path[level] = card[i]
        abc(level + 1, i)

abc(0, 0)
