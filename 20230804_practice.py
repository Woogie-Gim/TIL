# BS : Binary Search
# 빠른 검색 / 탐색 방법
# Binary Search Tree : Binary Search를 통해 Tree 라는 구조에 저장하는 방식 / 자료 구조

# 이진 탐색
# up down 게임 진행 방식과 같다
# 중앙값 부터 검색을 시작하는 것이 가장 유리 / 이진 검색도 같다

"""
정수 n개 입력
target 변수가 정수 n개 안에 있는지 없는지 찾는다

4   7   9   11  13  15  19
start       mid         end

(start + end) // 2
mid < target
start = mid + 1

mid > target:
end = mid - 1

mid == target ?

O(logn) 의 속도로 탐색

데이터 값을 정렬 후에 진행을 해야한다

-----------------------------------------

Binary Search 이진 탐색
(단, 정렬이 되어 있는 상태의 data)
원하는 값을 찾을 때 for문 돌려서 O(n)의 속도가 아닌 O(logn)의 속도로
원하는 값을 탐색 할 수 있게 하는 알고리즘(탐색 기법)

정렬이 되어 있는 data 의 mid 값을 찾은 후 target과 비교 후
mid > target:
end = mid - 1 로 줄이고

mid < target:
start = mid + 1로 늘려가며 원하는 값을 찾아가는 방식
"""

# n 입력
# n개의 정수를 입력
# 찾고자 하는 target 1개 입력

# n = int(input())
# arr = list(map(int, input().split()))
# target = int(input())
#
# def binary_search(start, end, target):
#
#     while 1:
#         mid = (start + end) // 2
#         if arr[mid] == target:
#             return 1
#         elif arr[mid] > target:
#             end = mid - 1
#         elif arr[mid] < target:
#             start = mid + 1
#
#         if start > end:
#             return 0
#
# arr.sort()
#
# ans = binary_search(0, n - 1, target) # 0은 시작 인덱스, n-1은 arr 배열의 마지막 인덱스
#
# if ans:
#     print('찾음')
# else:
#     print('못찾음')


# Parametric search


"""
battery = str(input())
arr = list(battery)
target = str(input())


def parameteric_search(start, end):
    cnt = 0
    while start < end:
        mid = (start + end) // 2
        if arr[mid] == target:
            cnt += 1
            start = mid + 1
        elif arr[mid] != target:
            end = mid - 1
        if start > end:
            break

    return cnt + 1

ans = parameteric_search(0, len(arr) - 1)


print(f'{ans  * 10}%')
"""

"""
battery = "**********"
def parametric_search(start,end,target):
    MAX=0
    while True:
        mid = (start + end) // 2
        if battery[mid] != target:
            end = mid-1
        elif battery[mid] ==target:
            start = mid+1
            MAX = (mid+1)*10

        if start>end:
            break
    return MAX


print(parametric_search(0,9,'*'))
"""


# battery = '##########'
#
# def parameteric_search(st, ed):
#     Max = -1
#     while 1:
#         mid = (st + ed) //2
#         if battery[mid] == '_':
#             ed = mid - 1
#         elif battery[mid] == '#':
#             Max = mid
#             st = mid + 1
#
#         if st > ed:
#             break
#     return Max + 1
#
# ans = parameteric_search(0, 9)
#
# print(f'{ans * 10}%')

"""
내 코드 / 좌표값으로 풀기
curser = [
    '##########',
    '##########',
    '###_______',
    '__________',
    '__________'
]

def parameteric_search(sty, stx, edy, edx):
    Max = -1
    while 1:
        dy = 0
        dx = 0
        midy = (sty + edy) // 2
        midx = (stx + edx) // 2
        if curser[midy][midx] == '_':
            edy = midy - 1
            edx = midx - 1
            dy = edy
            dx = edx
        elif curser[midy][midx] == '#':
            sty = midy + 1
            stx = midx + 1
            dy = sty
            dx = stx

        if sty > edy and stx > edx:
            break
        return dy + 1, dx

ans = parameteric_search(0, 0, 4, 9)

print(ans)
"""

# 교수님 코드

curser = [
    '##########',
    '##########',
    '###_______',
    '__________',
    '__________'
]

# y axis parameteric_search 1번 / x axis parameteric_search 2번

def binary_search(start, end):
    Max = -1
    while 1:
        mid = (start + end) // 2
        if curser[mid][0] == '_':
            end = mid -1
        elif curser[mid][0] == '#':
            Max = mid
            start = mid + 1

        if start > end:
            break

    return Max + 1


def binary_search2(start, end, yy):
    Max = -1
    while 1:
        mid = (start + end) // 2
        if curser[yy][mid] == '_':
            end = mid - 1
        elif curser[yy][mid] == '#':
            Max = mid
            start = mid + 1

        if start > end:
            break

    return Max + 1

yaxis = binary_search(0, 5)
yaxis -= 1

xaxis = binary_search2(0, 9, yaxis)

print(f'({yaxis}, {xaxis})')

# O(nlogn)