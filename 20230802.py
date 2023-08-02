# 배열 2 (Array 2)

# 2차원 배열의 선언
# 1차원 List를 묶어 놓은 list
# 2차원 이상의 다차원 List는 차원에 따라 Index를 선언
# 2차원 List의 선언 : 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 함
# Python에서는 데이터 초기화를 통해 변수 선언과 초기화가 가능함

# arr = [[0, 1, 2, 3], [4, 5, 6, 7]]

#[참고]

# 3
# 1 2 3
# 4 5 6
# 7 8 9
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]

# 배열 순회
# n X m 배열의 n * m개의 모든 원소를 빠짐없이 조사하는 방법

# 행 우선 순회
# i 행의 좌표
# j 열의 좌표
# for i in range(n):
#     for j in range(m):
#         f(arry[i][j]) # 필요한 연산 수행

# 행을 고정하고 열을 바꾸자


# 열 우선 순회

# i 행의 좌표
# j 열의 좌표

# for j in range(m):
#     for i in range(n):
#         f(Array[i][j]) # 필요한 연산 수행

# 열을 고정하고 행을 바꾸자

# 지그재그 순회

# i행의 좌표
# j열의 좌표

# for i in range(n):
#     for j in range(m):
#         f(Array[i][j + (m - 1 - 2 * j) * (i % 2)])
#         필요한 연산 수행

N = 2 # 행의 크기
M = 3 # 열의 크기

arr = [[0, 1, 2, 3], [4, 5, 6, 7]]

for i in range(N):
    for j in range(M):
        print(arr[i][j] + (M-1-2*j) * (i%2))

N = 2 # 행의 크기
M = 3 # 열의 크기

arr = [[0, 1, 2, 3], [4, 5, 6, 7]]

for i in range(N):
    for j in range(M):
        print(arr[i][j])

N = 2 # 행의 크기
M = 4 # 열의 크기

arr = [[0] * M for _ in range(N)]

arr[0][0] = 1

print(arr)

N = 2 # 행의 크기
M = 4 # 열의 크기

arr = [[0, 1, 2, 3], [4, 5, 6, 7]]

max_v = 0

for i in range(N):
    row_total = 0 # 각 행의 합
    for j in range(M):
        row_total += arr[i][j]
    if max_v < row_total:
        max_v = row_total

# 델타를 이용한 2차 배열 탐색
# 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법

"""
arr[0...N-1][0...N-1] # NxM 배열
di[] <- [0, 1, 0, -2]
dj[] <- [1, 0, -1, 0]

for i : 0 -> N-1
    for j : 0 -> N-1
        for k in range(4):
            nj <- i + di[k]
            nj <- j + dj[k]
            
            if 0 <= ni < N and 0 <= nj < N # 유효한 인덱스면
                        f(arr[ni][nj])
"""

# im 평가의 단골문제


"""
3
1 2 3
4 5 6
7 8 9
"""

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

max_v = 0 # 모든 원소가 0 이상이라면
for i in range(N):
    for j in range(N):
        # arr[i][j] 중심으로
        s = arr[i][j]
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N: #배열을 벗어나지 않으면
                s += arr[ni][nj]
        # 여기까지 주변 원소를 포함한 합
        if max_v < s:
            max_v = s


print(max_v)

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

max_v = 0 # 모든 원소가 0 이상이라면
for i in range(N):
    for j in range(N):
        # arr[i][j] 중심으로
        s = arr[i][j]
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N: #배열을 벗어나지 않으면
                s += arr[ni][nj]
        # 여기까지 주변 원소를 포함한 합
        if max_v < s:
            max_v = s

# 전치 행렬
"""
i : 행의 좌표, len(arr)
j : 열의 좌표, len(arr[0])

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # 3 * 3 행렬

for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]            
                0  1       1  0        1  0       0  1
                 2 <-> 4 
"""

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

total1 = 0
total2 = 0
for i in range(N):
    total1 += arr[i][i]