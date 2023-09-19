# Dijkstra algorithm
"""
"""
"""
      B
   3/ 1| \7
  A    E   C
  \9      /1
      D

index A : 0 / B : 1 / C : 2 / D : 3 / E : 4

5 7 (정점 / 간선)
0 1 3 (출발점, 도착점, 비용)
0 4 5
0 3 9
1 4 1
1 2 7
2 3 1
4 2 1
시작점, 도착점 입력 받음

0 A - [1, 3] - [4, 5] - [3, 9]
1 B - [4, 1] - [2, 7]
2 C - [3, 1]
3 D
4 E - [2, 1]

reuslt 배열 만들기
시작점에서의 다른 모든 정점까지의 최소 비용을 갱신해주는 배열

heap 배열 만들기
우선순위 q 활용

0. result inf로 하드코딩
result = [inf, inf, inf, inf, inf]

1. 시작점을 경유지로, 경유지 A
2. heap에 경유지를 등록 (경유지 선택용)
heap (0, 0) [(시작점에서 경유지까지 가는데 드는 비용, 경유지 index)]
3. 시작점 -> 도착점 vs 시작점 -> 경유지 -> 도착점

result = [0, inf, inf, inf, inf]

경유지 A에서 갈 수 있는 정보는 인접 리스트에 다 들어 있음
A -> B inf
A -> A -> B 3
result = [0, 3, inf, inf, inf]
동시에 heap push
heap = [(3, 1)]

A -> E inf
A -> A -> E 5
result = [0, 3, inf, inf, 5]
heap = [(3, 1), (5, 4)]

A -> D inf
A -> A -> D 9
result = [0, 3, inf, 9, 5]
heap = [(3, 1), (5, 4), (4, 3)]

그 다음 경유지 선택 가장 적은 비용을 heappop을 통해서 logN의 속도로 빼올 수 있다

경유지 B
A -> E 5
A -> B -> E  4
result = [0, 3, inf, 9, 4]
heap = [(5, 4), (4, 3), (4, 4)]

A -> C inf
A -> B -> C 10
result = [0, 3, 10, 9, 4]
heap = [(5, 4), (4, 3), (4, 4), (10, 2)]

경유지 E
A -> C  10
A -> E -> C 5
result = [0, 3, 5, 9, 4]
heap = [(5, 4), (4, 3), (10, 2), (5, 2)]

# 튜플 또는 리스트에서 우선순위를 정할 때 0번인덱스 기준으로 우선순위를 잡고 그 다음은 1번인덱스를 기준

경유지 C
A -> D 9
A -> C -> D 6
result = [0, 3, 5, 6, 4]
heap = [(5, 4), (4, 3), (10, 2), (6, 3)]

경유지 E
이미 갱신이 되어 있으므로 continue

경유지 D
갈 수 있는 곳이 없으므로 continue

heap이 다 비어질 때까지 heappop()
"""

# 입력 예제

# 5 7
# 0 1 3
# 0 3 9
# 0 4 5
# 1 2 7
# 1 4 1
# 2 3 1
# 4 2 1
# 0 3

# import heapq
# n, m = map(int, input().split()) # 정점의 개수, 간선의 개수 입력 받기
# arr = [[] for _ in range(n)]    # 인접 리스트 arr 선언
#
# for _ in range(m):              # 간선의 개수 만큼 반복
#     a, b, c = map(int, input().split()) # a에서 b까지 가는데 드는 비용 c 입력받고 저장하기
#     arr[a].append([b, c])
#
# start, end = map(int, input().split())
#
# inf = int(21e8)
# result = [inf] * n
#
# def dijkstra(start):
#     heap = [] # 우선순위큐 이용 시 사용될 리스트(인자값)
#     heapq.heappush(heap, [0, 0]) # 시작점을 경유지로 등록 먼저 해주기 ( 시작점에서 경유지까지 드는 비용, 경유지 index)
#     result[start] = 0 # 시작점을 경유지로 놓았기 때문에 시작점 = 경유지 비용을 0
#
#     while heap:
#         sk, k = heapq.heappop(heap) # sk (시작점에서 경유지까지 비용), k (선택한 경유지)
#
#         if sk > result[k]:
#             continue
#
#         for i in arr[k]: # 경유지에서 갈 수 있는 곳이 -> i (경유지 정보)
#             cost = sk + i[1] # 시작점 -> 경유지 비용 + 경유지 -> 도착점 비용
#             if cost < result[i[0]]:     # 경유지 들렸을 때의 비용으로 갱신이 된다면
#                 result[i[0]] = cost     # result 갱신
#                 heapq.heappush(heap, [cost, i[0]])  # heap 푸쉬
#
#
#
# dijkstra(start) # 시작점 넣기
# print(*result, end = ' ')

# Floydwashall algo
# 모든 정점에서 다른 모든 정점끼리의 최소 비용
# (feat. 다익스트라 => 한점 시작점 -> 다른 모든 정렬)

"""         
시작점 -> 경유지 -> 도착점
시작점 -> 도착점

k = 경유지
s = 시작점
d = 도착점

pseudocode
for k in range() # 경유지
    for s in range() # 시작점
        for d in range() # 도착점
            min(시작점 -> 도착점 vs 시작점 -> 경유지 -> 도착점)
            

        B
   5//7    \9
    A   <-2  C
    8\     3//4
         D
     
index A = 0 / B = 1 / C = 2 / D = 3       

인접행렬 하드 코딩
0 5 inf 8
7 0 9 inf
2 inf 0 4
inf inf 3 0

경유지 A
시작점 B
B -> D inf
B -> A -> D 7 + 8 = 15
15 갱신

0 5 inf 8
7 0 9 15
2 inf 0 4
inf inf 3 0

시작점 C
C -> B inf
C -> A -> B 2 + 5 = 7

0 5 inf 8
7 0 9 15
2 7 0 4
inf inf 3 0

시작점 D
D -> A inf
볼 필요 X

경유지 B
시작점 A
A -> C inf
A -> B -> C 5 + 9 14
0 5 14 8
7 0 9 15
2 7 0 4
inf inf 3 0

시작점 D
D -> B inf 볼 필요 x

경유지 C
A -> C 14

시작점 B
B -> C 9
B -> D 15
B -> C -> D 9 + 4 = 13 
0 5 14 8
7 0 9 15
2 7 0 4
inf inf 3 0

시작점 D
D -> A inf
D -> C -> A 3 + 2 = 5

0 5 14 8
7 0 9 15
2 7 0 4
5 inf 3 0

D -> B inf
D -> C -> B 10

0 5 14 8
7 0 9 15
2 7 0 4
5 10 3 0

경유지 D

시작점 A
A -> C 14 
A -> D -> C 8 + 3 = 11

0 5 11 8
7 0 9 15
2 7 0 4
5 10 3 0
"""

inf = int(21e8)
arr = [
    [0, 5, inf, 8],
    [7, 0, 9, inf],
    [2, inf, 0, 4],
    [inf, inf, 3, 0]]

for ky in range(4):
    for si in range(4):
        for do in range(4):
            if arr[si][do] > arr[si][ky] + arr[ky][do]:
                arr[si][do] = arr[si][ky] + arr[ky][do]

for i in range(4):
    for j in range(4):
        print(arr[i][j], end=' ')
    print()