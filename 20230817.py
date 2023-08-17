# BFS 복습

"""
B -> A, B -> C / A <-> C, A -> D / C <-> A, C -> D, C -> E / D -> E, D -> F
1번 index 부터 BFS 탐색
탐색 순서 출력하기
"""
from collections import deque

name = list(input().split())  # A B C D E F

arr = [[0, 0, 1, 1, 0, 0],
       [1, 0, 1, 0, 0, 1],
       [1, 0, 0, 1, 1, 0],
       [0, 0, 0, 0, 1, 1],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0]]

used = [0] * 6
used[1] = 1
q = deque()
q.append(1)

while q:
    now = q.popleft()
    print(name[now], end=' ')
    for i in range(6):
        if arr[now][i] == 1 and used[i] == 0:
            used[i] = 1
            q.append(i)

# Flood Fill 복습

# 4 * 4 맵에서 1일차 - (2, 1) 좌표에 꽃핌
# 입력받은 좌표가 몇일 차에 꽃이 필지

from collections import deque

endy, endx = map(int, input().split())
arr = [[0] * 4 for _ in range(4)]

arr[2][1] = 1
q = deque()
q.append((2, 1, 1))
ans = 0
directy = [0, 0, -1, 1]
directx = [-1, 1, 0, 0]

while q:

    y, x, level = q.popleft()

    for i in range(4):
        dy = y + directy[i]
        dx = x + directx[i]

        if 0 <= dy < 4 and 0 <= dx < 4: # 배열 범위 안이라면
            if arr[dy][dx] == 0: # 이미 방문한 곳이 아니라면
                arr[dy][dx] = arr[y][x] + 1 # 배열에 현재 일차 + 1 값을 적어주기
                q.append((dy, dx, level + 1))
                if dy == endy and dx == endx:
                    ans = level + 1
for i in range(4):
    print(arr[i])

print(ans)

from collections import deque

n = int(input())
arr = [[0] * n for _ in range(n)]
starty, startx = map(int, input().split())
endy, endx = map(int, input().split())
ans = 0
directy = [-1, 1, 0, 0]
directx = [0, 0, -1, 1]
arr[starty][startx] = 1

q = deque()
q.append((starty, startx, 1))

while q:
    y, x, level = q.popleft()

    for i in range(4):
        dy = y + directy[i]
        dx = x + directx[i]

        if 0 <= dy < 4 and 0 <= dx < 4:
            if arr[dy][dx] == 0:
                arr[dy][dx] = arr[y][x] + 1
                q.append((dy, dx, level + 1))

                if dy == endy and dx == endx:
                    ans = level + 1

print(ans)

# n 입력
# n * n size 배열 생성
# 좌표값을 입력 받아서 두 군데에 꽃을 심을 예정
# 위 아래 좌우 기준으로 꽃이핌 (+ 1)
# 확인하고 싶은 좌표값을 입력받을 예정
# 좌표값이 몇일 후에 꽃이 피는지

from collections import deque

n = int(input())
flower = list(map(int, input().split()))

endy, endx = map(int, input().split())

y1, x1 = flower[0], flower[1]
y2, x2 = flower[2], flower[3]
arr = [[0] * n for _ in range(n)]


directy = [0, 0, -1, 1]
directx = [-1, 1, 0, 0]

flower = [(y1, x1, 1), (y2, x2, 1)]

def bfs(flower):
    global arr, n
    q = deque(flower)
    arr[y1][x1] = 1
    arr[y2][x2] = 1

    while q:
        nowy, nowx, level = q.popleft()

        for i in range(4):

            dy = nowy + directy[i]
            dx = nowx + directx[i]

            if dy < 0 or dx < 0 or dy > n - 1 or dx > n - 1:
                continue
            if arr[dy][dx] != 0:
                continue
            arr[dy][dx] = arr[nowy][nowx] + 1
            q.append((dy, dx, level + 1))


bfs(flower)

print(arr[endy][endx])

# 쥐가 치즈를 먹고 여자친구한테 가는데 최소 이동거리
# 시작 좌표 (0, 0) 여자친구 좌표 (3, 4)
# 치즈 좌표 (3, 0)

from collections import deque

arr = [[0, 0, 0, 0, 0],
       [1, 0, 0, 1, 0],
       [1, 0, 0, 1, 0],
       [0, 0, 0, 0, 0]]

directy = [-1, 1, 0, 0]
directx = [0, 0, -1, 1]

answer = 0

def bfs(sty, stx, edy, edx):
    q = deque()
    q.append([sty, stx, 0])

    used = [[0] * 5 for _ in range(4)]
    used[sty][stx] = 1

    while q:
        now = q.popleft()
        yy, xx, level = now

        if yy == edy and xx == edx:
            return level

        for i in range(4):
            dy = yy + directy[i]
            dx = xx + directx[i]

            if dy < 0 or dx < 0 or dy > 3 or dx > 4:
                continue
            if used[dy][dx] == 1: # 중복체크
                continue
            if arr[dy][dx] == 1:
                continue
            used[dy][dx] = 1 # 중복 체크 배열에 1 체크하기
            q.append([dy, dx, level + 1])


answer += bfs(0, 0, 3, 0)
answer += bfs(3, 0, 3, 4)
print(answer)

"""
내 코드

from collections import deque

arr = [[0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0],
       [0, 1, 1, 1, 0],
       [0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0]]

ans = []

q = deque()
q.append((0, 0))

directy = [-1, 1, 0, 0]
directx = [0, 0, -1, 1]
visited = [[0] * 5 for _ in range(5)]


while q:
    y, x = q.popleft()

    if arr[y][x] == 1:
        ans.append((y, x))

    for i in range(4):
        dy = y + directy[i]
        dx = x + directx[i]

        if dy < 0 or dx < 0 or dy > 4 or dx > 4:
            continue
        if visited[dy][dx] == 1:
            continue
        visited[dy][dx] = 1
        q.append((dy, dx))

print(len(ans))
"""

# 교수님 코드
# 1의 개수 구하기

from collections import deque

arr = [[0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0],
       [0, 1, 1, 1, 0],
       [0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0]]


directy = [-1, 1, 0, 0]
directx = [0, 0, -1, 1]

def bfs(y, x):
    q = deque()
    q.append([y, x])
    size = 1
    arr[y][x] = 0

    while q:
        y, x = q.popleft()
        for i in range(4):
            dy = y + directy[i]
            dx = x + directx[i]

            if dy < 0 or dy > 4 or dx < 0 or dx > 4:
                continue
            if arr[dy][dx] == 1:
                q.append([dy, dx])
                arr[dy][dx] = 0
                size += 1

    return size


for y in range(5):
    for x in range(5):
        if arr[y][x] == 1:
            print(bfs(y, x))


# 총 섬의 개수를 출력 / 가장 큰 섬 size / 가장 작은 섬 size를 출력

from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

directy = [-1, 1, 0, 0]
directx = [0, 0, -1, 1]

def bfs(y, x):
    q = deque()
    q.append((y, x))
    size = 1
    arr[y][x] = 0

    while q:
        y, x = q.popleft()
        for i in range(4):
            dy = y + directy[i]
            dx = x + directx[i]

            if dy < 0 or dx < 0 or dy > n - 1 or dx > n - 1:
                continue
            if arr[dy][dx] == 1:
                q.append((dy, dx))
                arr[dy][dx] = 0
                size += 1

    return size

ans = []

for y in range(n):
    for x in range(n):
        if arr[y][x] == 1:
            ans.append(bfs(y, x))

print(len(ans), max(ans), min(ans))