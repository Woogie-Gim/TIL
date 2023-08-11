# DFS 인접 리스트 연습
def dfs(now):
    print(name[now], end = ' ')
    for i in lst[now]:
        dfs(i)


name = 'ABCDEF'
n, m = map(int, input().split())
lst = [[] for _ in range(n)]

for i in range(m):
    s, e = map(int, input().split())
    lst[s].append(e)

dfs(0)

"""
0 : A, 1 : B, 2 : C, 3 :D
무방향 그래프

간선 정보
A <-> B 3 / B <-> D 9 / A <-> C 8 / B <-> C 1 / C <-> D 2

입력 정보
4 5 / 정점 개수, 간선(정보) 개수
0 1 3 / 시작점 ,도착점, 비용
0 2 8
1 2 1
1 3 9
2 3 2

시작점 A에서 D까지 최소비용 출력하기
"""

n, m = map(int, input().split())
lst = [[] for _ in range(n)]
used = [0] * n

for i in range(m):
    s, e, cost = map(int, input().split())
    lst[s].append((e, cost))
    lst[e].append((s, cost))

#   e, cost e, cost   e, cost e, cost  e, cost  e, cost e, cost e, cost   e, cost  e, cost
# [[(1, 3), (2, 8)], [(0, 3), (2, 1), (3, 9)], [(0, 8), (1, 1), (3, 2)], [(1, 9), (2, 2)]]
#        시작점                 시작점                    시작점                  시작점
"""
0  - (1, 3) - (2, 8)
1 - (0, 3) - (2, 1) - (3, 9)
2 - (0, 8) - (1, 1) - (3, 2)
3 - (1, 9) - (2, 2)
"""

Min = 21e8

def dfs(now, Sum):
    global Min
    if now == 3 and Sum < Min:
        Min = Sum
    for i in lst[now]:
        if used[i[0]] == 1:
            continue
        used[i[0]] = 1
        dfs(i[0], Sum + i[1])
        used[i[0]] = 0


used[0] = 1
dfs(0, 0)
print(Min)

"""
최종 코드
n, m = map(int, input().split())
lst = [[] for _ in range(n)]
used = [0] * n

for i in range(m):
    s, e, cost = map(int, input().split())
    lst[s].append((e, cost))
    lst[e].append((s, cost))
    
Min = 21e8

def dfs(now, Sum):
    global Min
    if now == 3 and Sum < Min:
        Min = Sum
    for i in lst[now]:
        if used[i[0]] == 1:
            continue
        used[i[0]] = 1
        dfs(i[0], Sum + i[1])
        used[i[0]] = 0


used[0] = 1
dfs(0, 0)
print(Min)
"""

# DFS 연습

arr = [[3, 5, 9, 6],   # 5층
       [7, -8, 1, 6],  # 4층
       [-10, 2, 3, 9], # 3층
       [5, 1, 2, 8],   # 2층
       [4, 7, 1, 8]]   # 1층

# 각 층에서 숫자 1개씩 택하여 계단을 내려 옵니다
# 술취한 아저씨가 7시 6시 5시 방향으로만 움직일 수 있습니다. 1층에 내려왔을 때 각 층의 선택한 수의 합이
# 30 이상인 경우는 몇 가지 일까요?

cnt = 0
def dfs(now, level, sum):
    global cnt
    if level == 4:
        if sum >= 30:
            cnt += 1
        return

    for i in range(3):
        direct = [-1, 0, 1]
        dy = level + 1 # 행
        dx = now + direct[i] # 열
        if dx < 0 or dx > 3:
            continue
        dfs(dx, level + 1, sum + arr[dy][dx])



for i in range(4):
    dfs(i, 0, arr[0][i]) # now, level, sum

print(cnt)

# 미로 찾기 문제

# 갈 수 있는 길은 0 / 벽은 1로 표현
# 예시) 4 * 4 미로에서 (0, 0) -> (3, 3) 좌표까지 갈 수 있는지 없는지 출력 (끝에서 끝으로)
# 이동은 위 아래 좌 우로 이동할 수 있음
# direct // 배열 범위 체크 // 벽 이동 금지 / 중복 체크를 통해서 cycle 방지
# 바닥조건으로 끝내기 flag 1 키고 끝내기

arr = [[0, 0, 0, 0],
       [1, 0, 1, 0],
       [1, 0, 1, 0],
       [0, 0, 0, 0]]

directy = [0, 0, -1, 1]
directx = [1, -1 ,0, 0]

visited = [[0] * 4 for _ in range(4)]
flag = 0

def dfs(y, x):
    global flag
    if y == 3 and x == 3:
        flag = 1
        return

    for i in range(4):
        dy = y + directy[i]
        dx = x + directx[i]
        if dy < 0 or dx < 0 or dy > 3 or dx > 3:
            continue
        if visited[dy][dx] == 1:
            continue
        if arr[dy][dx] == 1:
            continue
        visited[dy][dx] = 1
        dfs(dy, dx)
        if flag == 1:
            return # 경로 단축

dfs(0, 0) # 시작 좌표
if flag:
    print('찾았음')
else:
    print('없음')