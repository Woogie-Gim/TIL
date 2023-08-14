# BFS
# breadth First Search

# M -> B, M -> I / B -> K, B -> T / I -> S
# M / B I / K T S 탐색

# 현재 위치에서 갈 수 있는 곳을 queue에 다 적기

# [[0, 1, 1, 0, 0, 0],
#  [0, 0, 0, 1, 1, 0],
#  [0, 0, 0, 0, 0, 1],
#  [0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0]]

# head = now / tail
# M 에서 이동 할 수 있는 곳을 queue에 전부 적기
# [M, B, I ...
#  h
# 다 적고 난 후
# B 로 head 이동
# [M, B, I, K, T ...
# I 로 head 이동
# [M, B, I, K, T, S ...
# head와 tail 이 만났다면 while 문 종료

# q
# 시작 인덱스 queue 에 넣기
# 0
# 탐색 시작 인덱스를 queue에 넣고 시작
# .popleft() now를 0번 인덱스로 만들기
# 인접행렬을 탐색하여 인접한 인덱스들을 모두 queue에 append
# .popleft()
# now 를 이동시켜 가면서

from collections import deque

name = list(input().split()) # M B I K T S

arr = [[0, 1, 1, 0, 0, 0],
       [0, 0, 0, 1, 1, 0],
       [0, 0, 0, 0, 0, 1],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0]]

def bfs(now):
    q = deque()
    q.append(now)
    while q:
        now = q.popleft() # 현재 위치를 알려주는 위치 popleft를 통해서 now 위치를 이동 시켜줌
        print(name[now], end = ' ') # 0번 인덱스 M 부터 출력

        for i in range(6):
            if arr[now][i] == 1:
                q.append(i)
        # now 값에 들어갔던 순서가 탐색 순서


bfs(0) # 탐색 시작 인덱스


from collections import deque

name="BQKFCM"
arr=[[0,1,1,1,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,1,1],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]]

answer=[]

def bfs(now):
    global answer
    q=deque()
    q.append(now)

    while q:
        now=q.popleft()
        answer.append(name[now])
        for i in range(6):
            if arr[now][i]==1:
                q.append(i)

bfs(0)
print(*answer)


"""
A -> B, A -> C / B <-> C / C <-> B, C -> D
A 부터 graph 너비우선 1번씩만 탐색
q = [A,
popleft()
now -> A
q = [B, C, ...
popleft()
now -> B
q = [C, C ...
따라서 used 필요
"""
# A 부터 모든 정점을 1번씩 탐색

from collections import deque

name = 'ABCD'

arr = [[0, 1, 1, 0],
       [0, 0, 1, 1],
       [0, 1, 0, 1],
       [0, 0, 0, 0]]

used = [0] * 4
ans = []

def bfs(start):
    global ans
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()
        ans.append(name[now])
        for i in range(4):
            if arr[now][i] == 1 and used[i] == 0:
                used[i] = 1
                q.append(i)


used[0] = 1 # 탐색 시작 인덱스에 해당하는 used에 1 체크
bfs(0)
print(*ans)


# A 부터 D 까지 갈 수 있는 경로가 몇가지 인가요?
# A -> B, A -> C / B <-> C / C <-> B, C -> D
# DFS 의 경우 used 1 켰다가 나올 때 0
# BFS 의 경우 방문할 때마다의 used 배열을 각각 따로 만들어 주어야 함
"""
          A               B              C                 C              D               B
    [1, 0, 0, 0]    [1, 1, 0, 0]    [1, 1, 1, 0]     [1, 1, 1, 0]    [1, 1, 0, 1]    [1, 1, 1, 0]
         D               D               D
    [1, 1, 1, 1]    [1, 1, 1, 1]    [1, 1, 1, 1]  
각각의 경로에 따라서 used 배열을 따로 관리를 해주어야함
"""

# BFS 경로 탐색 (그닥 추천하지 않음)
# 0번 인덱스 A 에서 3번 인덱스 D 까지 갈 수 있는 경로가 총 몇 가지?

from collections import deque
import copy

name = 'ABCD'

arr = [[0, 1, 1, 0],
       [0, 0, 1, 1],
       [0, 1, 0, 1],
       [0, 0, 0, 0]]

cnt = 0
def bfs(start):
    global cnt
    q = deque()
    used = [0] * 4
    used[start] = 1
    q.append((start, used)) #[(0, [1, 0, 0, 0])]

    while q:
        now = q.popleft()
        if now[0] == 3:
            cnt += 1

        for i in range(4):
            if arr[now[0]][i] == 1 and now[1][i] == 0:
                used = copy.deepcopy(now[1])
                used[i] = 1
                q.append((i, used))


bfs(0)
print(cnt)

# Flood Fill 유형 / bloom / virus

# 5 * 5 배열에서 3, 3 위치에 꽃이 폈다고 가정
# 상하좌우로 갈 수 있는 모든 경우의 수를 q 에 체크
# popleft() 바뀐 now 기준으로 상하좌우 체크
# 배열 범위 체크 / 이미 적힌 곳 x
# arr 배열에 체크해주고 queue에 append

from collections import deque
n = int(input()) # arr 배열 (맵사이즈 입력)
arr = [[0] * n for _ in range(n)]

y, x = map(int, input().split()) # 바이러스 시작 좌표 입력

arr[y][x] = 1
q = deque()
q.append([y, x])

while q:
    now = q.popleft()
    y, x = now # 현재 기준 좌표
    directy = [0, 0, -1, 1]
    directx = [1, -1, 0, 0]

    for i in range(4): # 4 방향
        dy = directy[i] + y
        dx = directx[i] + x

        if dy < 0 or dx < 0 or dy >= n or dx >= n: # 배열 범위
            continue
        if arr[dy][dx] != 0: # 이미 방문한 곳 (중복 체크)
            continue

        arr[dy][dx] = arr[y][x] + 1 # 기준 좌표값 +1 한 값을 map에 적어주기
        q.append([dy, dx]) # q에 푸쉬

for i in arr:
    print(*i)


# N 입력받은 후 N x N 사이즈의 맵에 바이러스를 투입해 보자고 합니다.
# 바이러스를 최초로 투입 할 좌표를 입력 받습니다.
# 0,1 좌표에는 몇일날 바이러스가 도착 할까요?

from collections import deque

n = int(input())
arr = [[0] * n for _ in range(n)]
y, x = map(int, input().split())

arr[y][x] = 1
q = deque()
q.append((y, x, 1))

ans = 0
while q:
    y, x, level = q.popleft()

    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]

    for i in range(4):
        dy = directy[i] + y
        dx = directx[i] + x

        if dy < 0 or dx < 0 or dy >= n or dx >= n:
            continue
        if arr[dy][dx] != 0:
            continue

        arr[dy][dx] = arr[y][x] + 1
        q.append((dy, dx, level + 1))
        if dy == 0 and dx == 1:
            ans = level + 1
            break

print(f'{ans}일차')
