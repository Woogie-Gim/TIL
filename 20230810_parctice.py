# 알고리즘 - 효율적으로 문제를 해결하는 방식
# 저장구조 - data를 저장하거나 관리하는 방식 공부

# 선형 구조 - list(array) / linked list
# list는 값을 추가하거나 제거할 때 공백을 없게 하기 위해 앞뒤로 당기거나 민다 / 자료를 추가 삭제가 잦으면 느리다 불리하다
# linked list 값의 추가 삭제 할 때 링크를 끊거나 새로 연결해서 효율적으로 할 수 있다
# 탐색할 때 for / while 문을 통해서 탐색

# 비선형구조
# graph
# 탐색할 때 DFS / BFS 탐색 방법을 사용하여 탐색

# 데이터를 관리하거나 사용하는 방법으로는 stack 과 queue를 사용

# queue : First In First Out / stack : First In Last Out

# Queue
# 맛집에 줄을 세워서 줄 선 순서대로 입장하고 가장 먼저 들어온 손님부터 음식을 내줌

# Stack
# 뒤로가기 버튼 / 가장 마지막에 봤던 페이지를 렌더 해서 보여줌

# stack
# st = []
# st.append(3)
# st.append(4)
# st.append(5)
# st.append(6)
# print(st)
# st.pop() # 6 추출
# st.pop() # 5 추출
# st.pop() # 4 추출
# st.pop() # 3 추출

# queue

# from collections import deque
# q = deque()
# q.append(4)
# q.append(5)
# q.append(6)
# q.append(7)
# print(q) # deque([4, 5, 6, 7])
# print(*q) # 4 5 6 7
# q.popleft() # 4 추출
# q.popleft() # 5 추출
# q.popleft() # 6 추출
# q.popleft() # 7 추출

"""
graph

        A
    B      C
D     E

트리 모양의 그래프

특징 1) 부모 자식 관계를 갖는다
예) A의 자식은 B와 C / B의 자식은 D와 E
특징 2) 단방향이다
특징 3) cycle이 구조적으로 발생할 수 없다
최상위 부모를 '루트 노드'
나머지 '리프 노드'

트리 모양의 그래프가 아닌 구조는 단방향일 수도 있고 양방향일 수도 있고 (무방향 : 방향 표시 하지 않으면 전부 양방향)


트리 모양의 그래프를 코드로 표현하기
(인접행렬, 인접리스트, 1차원리스트에 이진트리 상태를 저장해서)

0번 인덱스 : A, 1번 인덱스 : B, 2번 인덱스 : C, 3번 인덱스 : D, 4번 인덱스 : E 라고 가정

1) 인접 행렬 (2차원 리스트)
  A B C D E
A 0 1 1 0 0
B 0 0 0 1 1
C 0 0 0 0 0
D 0 0 0 0 0
E 0 0 0 0 0

이동할 수 있는 리스트를 1로 체크

2) 인접 리스트
A 0 - [1, 2]
B 1 - [3, 4]
C 2
D 3
E 4

이동할 수 있는 인덱스를 리스트로 표현

3) 1차원 리스트
항상 루트 노드를 1번 인덱스에 저장
부모의 왼쪽은 부모인덱스 * 2 에 저장 됨 / 오른쪽은 부모인덱스 * 2 + 1 에 저장됨

1 A / 2 B / 3 C / 4 D / 5 E
[_, A, B, C, D, E, _, _, _]


인접행렬과 인접리스트의 차이
1) 모든 노드(data)를 탐색할 때
인접행렬은 2중 for문을 통해서 전부 탐색
인접리스트는 갈 수 있는 곳이 없으면 탐색하지 않음
따라서 인접리스트가 인접행렬보다 빠르게 탐색할 수 있다

2) 특정 노드의 상황을 파악하려 할 때
예) B에서 E 이동 가능?
인접리스트는 n 번 탐색 O(n)의 속도
인접행렬은 (B, E) 위치만 탐색 O(1)의 속도
특정 노드 탐색은 인접행렬이 인접리스트 보다 빠르게 탐색할 수 있다
"""
#
# name = ['Amy', 'Bob', 'Chloe', 'Diane', 'Edger']
#
# # A -> B , A -> D / B -> D / C -> B, C -> D / D -> E / E -> A
# # 0 : A / 1 : B / 2 : C / 3 : D / 4 : E
#
# # 인접 행렬로 표현하기
#
# arr = [[0, 1, 0, 1, 0],
#        [0, 0, 0, 1, 0],
#        [0, 1, 0, 1, 0],
#        [0, 0, 0, 0, 1],
#        [1, 0, 0, 0, 0]]

# 문제가 주어졌을 땐 인접행렬만 탐색해서 표현

"""
내 코드
result = []
for i in range(5):
    Sum = 0
    for j in range(5):
        Sum += arr[j][i]
    result.append(Sum)

Index = result.index(max(result))
print(name[Index])
"""

# 교수님 코드
# sum = 0
# Max = -21e8
# Maxindex = 0
#
# for j in range(5):
#     sum = 0
#     for i in range(5):
#         if arr[i][j] == 1:
#             sum += 1
#     if sum > Max:
#         Max = sum
#         Maxindex = j
#
# print(name[Maxindex])

# A -> B, A -> C / B -> D, B -> E / C -> F
# 0 : A / 1 : B / 2 : C / 3 : D / 4 : E / 5 : F
# 문자 1개를 입력 / 입력받은 문자의 형재노드 출력 if 형제가 없다면 형제 없음 이라고 출력
"""
내 코드

lst = ['A', 'B', 'C', 'D', 'E', 'F']

arr = [[0, 1, 1, 0, 0, 0],
       [0, 0, 0, 1, 1, 0],
       [0, 0, 0, 0, 0, 1],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0]]

strr = input()

Index = lst.index(strr)
parents_index = 0
brother_index = 0

for i in range(6):
    if Index == 0:
        break
    if arr[i][Index] == 1:
        parents_index = i

for k in range(6):
    if Index == 0:
        break
    if k != Index and arr[parents_index][k] == 1:
        brother_index = k

if brother_index > 0:
    print(lst[brother_index])
else:
    print('형제없음')
"""

# 교수님 코드
# lst = ['A', 'B', 'C', 'D', 'E', 'F']
#
# arr = [[0, 1, 1, 0, 0, 0],
#        [0, 0, 0, 1, 1, 0],
#        [0, 0, 0, 0, 0, 1],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0]]
#
# ch = input()
# idx = ord(ch) - 65
#
# parents = -1
# bro = -1
#
# # 부모노드가 없다면 -> 루트노드 -> 형제 없음
#
# for i in range(6):
#     if arr[i][idx] == 1:
#         parents = i
#         break
#
# if parents == -1:
#     print('형제없음')
# else:
#     # 부모 인덱스를 탐색하며 형제 출력하기
#     for i in range(6):
#         if arr[parents][i] == 1 and i != idx:
#             bro = i
#             break
#
#     if bro == -1:
#         print('형제없음')
#     else:
#         print(chr(i + ord('A')))




# DFS = Depth First Search (깊이 우선 탐색)
# 재귀함수와 탐색 순서가 유사
# A -> B, A -> C / B -> D, B -> E / C -> F
# 0 : A / 1 : B / 2 : C / 3 : D / 4 : E / 5 : F
# A -> B -> D return -> B -> E return -> B return -> A -> C -> F return -> C return -> A

# A부터 탐색을 시작해서 탐색하는 순서 출력
# A 부터 탐색하다가 첫번째 1을 발견하면 첫번째 1로 이동
# 계속해서 탐색하다가 갈 곳이 없다면 함수 호출 된 곳으로 return

# name = ['A', 'B', 'C', 'D', 'E', 'F']
#
# arr = [[0, 1, 1, 0, 0, 0],
#        [0, 0, 0, 1, 1, 0],
#        [0, 0, 0, 0, 0, 1],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0]]
#
# def dfs(now):
#     print(name[now], end = ' ')
#     for i in range(6):
#         if arr[now][i] == 1:
#             dfs(i)
#
# dfs(0) # 시작인덱스

# B -> K, B -> T, B -> G / T -> M, T -> C
# 0 : K, 1 : B, 2 : G, 3 : T, 4 : M, 5 : C
# 인덱스는 상관 없이 시작만 루트노드에서 시작하면 탐색 노선 출력 가능

# name = ['K', 'B', 'G', 'T', 'M', 'C']
#
# arr = [[0, 0, 0, 0, 0, 0],
#        [1, 0, 1, 1, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 1, 1],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0]]
#
# def dfs(now):
#     print(name[now], end = ' ')
#     for i in range(6):
#         if arr[now][i] == 1:
#             dfs(i)
#
# dfs(1)

# 트리 모양이 아닌 그림을 dfs로 탐색
# A -> B , A <-> C / B <-> C, B -> D / C <-> A, C <-> B, C -> D
# 0 : A / 1 : B / 2 : C / 3 : D
# A 부터 탐색

# 양방향 존재 -> cycle 발생 -> 무한 루프 발생
# cycle을 방지하는 코드가 필요
# used or visit 배열을 만들어서 체크하면서

"""
used
[0, 0, 0, 0]
[A, B, C, D]

방문한 곳을 1로 체크
"""

# name = ['A', 'B', 'C', 'D']
#
# arr = [[0, 1, 1, 0],
#        [0, 0, 1, 1],
#        [1, 1, 0, 1],
#        [0, 0, 0, 0]]
# used = [0] * 4
#
# def dfs(now):
#     print(name[now], end = ' ')
#     for i in range(4):
#         if arr[now][i] == 1 and used[i] == 0:
#             used[i] = 1
#             dfs(i)
#
#
# used[0] = 1 # 탐색 시작 인덱스에 해당하는 used 배열 값을 1체크하고
# dfs(0) # 0번 인덱스 부터 탐색 시작

# A -> B, A -> C  / B <-> C, B -> D / C <-> B, C -> D

# 모든 경로 체크
# 경로 체크 이기 때문에 들어갈 때 1 체크해서 cycle을 방지하고 return 될 때 0으로 돌려서 모든 경로 탐색

# name = ['A', 'B', 'C', 'D']
#
# arr = [[0, 1, 1, 0],
#        [0, 0, 1, 1],
#        [0, 1, 0, 1],
#        [0, 0, 0, 0]]
# visited = [0] * 4
#
# cnt = 0
# def dfs(now):
#     global cnt
#     if name[now] == 'D':
#         cnt += 1
#     for i in range(4):
#         if arr[now][i] == 1 and visited[i] == 0:
#             visited[i] = 1
#             dfs(i)
#             visited[i] = 0
#
#
# visited[0] = 1
# dfs(0)
# print(cnt)

# 최소 비용 구하기
# A -비용 : 4> B, A -비용 : 8> C / B <비용 : 1 - > C, B - 비용 : 7> D / C <비용 : 1 - > B, C - 비용 : 3> D

# name = ['A', 'B', 'C', 'D']
#
# arr = [[0, 4, 8, 0],
#        [0, 0, 1, 7],
#        [0, 1, 0, 3],
#        [0, 0, 0, 0]]
# used = [0] * 4
# Min = 21e8
#
# def dfs(now, sum):
#     global Min
#     if name[now] == 'D':
#         if sum < Min:
#             Min = sum
#     for i in range(4):
#         if arr[now][i] > 0 and used[i] == 0:
#             used[i] = 1
#             dfs(i, sum + arr[now][i])
#             used[i] = 0
#
#
# used[0] = 1
# dfs(0, 0) #탐색 시작 인덱스 0, Sum 0
# print(Min)


# dfs 인접 리스트로 탐색
# n - 정점 개수 / m - 간선의 개수
# A -> B, A -> C / B -> D, B -> E / C -> F
# 0 : A / 1 : B / 2 : C / 3 : D / 4 : E / 5 : F

"""

입력 예시
n - 정점 개수 / m - 간선의 개수
6              5
시작점 도착점
0       1
0       2
1       3
1       4
2       5
  
0 - 1, 2
1 - 3, 4
2 - 5
3 -
4 -
5 -

0 - [1, 2]
1 - [3, 4]
2 - [5]
3 - []
4 - []
5 - []
"""

name = 'ABCDEF'

n, m = map(int, input().split())
lst = [[] for _ in range(n)] # 정점의 개수 만큼
for i in range(m): #간선의 개수 만큼
    s, e = map(int, input().split())
    lst[s].append(e)

def dfs(now):
    print(name[now], end = ' ')
    for i in lst[now]:
        dfs(i)

dfs(0)

# BFS = Breadth First Search (너비 우선 탐색)
# A -> B, A -> C / B -> D, B -> E / C -> F
# 0 : A / 1 : B / 2 : C / 3 : D / 4 : E / 5 : F
# A -> B -> C -> D -> E -> F

