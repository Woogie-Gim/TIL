"""
정렬
선택 삽입 버블 - n ^ 2
계수(counting) - n
힙 합병 퀵 - nlogn
"""

# 합병 정렬 (merge sort)

# 합병 정렬 메인 코드
arr = [2, 3, 5, 6, 1, 2, 5, 9]
result = [0] * 8

start = 0
end = 7
mid = (start + end) // 2

a = start
b = mid + 1

index = 0 # result 배열의 index 역할을 할 것임

while 1:
    if a > mid and b > end:
        break

    if a > mid:
        result[index] = arr[b]
        index += 1
        b += 1
    elif b > end:
        result[index] = arr[a]
        index += 1
        a += 1
    elif arr[a] < arr[b]:
        result[index] = arr[a]
        index += 1
        a += 1
    else:
        result[index] = arr[b]
        index += 1
        b += 1

print(*result)

"""
                        2 7 5 3 1 5 9 2
                 2 7 5 3               1 5 9 2
              2 7       5 3          1 5      9 2
             2   7     5    3       1    5   9     2
             
끝까지 들어갔을 때 왼쪽 갔다가 오른쪽 갔다올 때 정렬
정렬 후 원본 데이터에 그 때 그 때 정렬

                        2 7 3 5 1 5 9 2
                 2 7 5 3               1 5 9 2
              2 7       3 5          1 5      9 2
             2   7     5    3       1    5   9     2
             
                        2 3 5 7 1 5 9 2
                 2 3 5 7               1 5 9 2
              2 7       3 5          1 5      9 2
             2   7     5    3       1    5   9     2
             
             
                        2 3 5 7 1 5 2 9
                 2 3 5 7               1 5 9 2
              2 7       3 5          1 5      2 9
             2   7     5    3       1    5   9     2
             
             
                        2 3 5 7 1 2 5 9
                 2 3 5 7               1 2 5 9
              2 7       3 5          1 5      2 9
             2   7     5    3       1    5   9     2
"""

arr = [2, 7, 5, 3, 1, 5, 9, 2]
result = [0] * 8


def merge(start, end):
    global arr, index, result
    mid = (start + end) // 2

    if start >= end:
        return

    merge(start, mid)
    merge(mid + 1, end)

    a = start
    b = mid + 1
    index = 0

    while 1:
        if a > mid and b > end:
            break
        if a > mid:
            result[index] = arr[b]
            index += 1
            b += 1
        elif b > end:
            result[index] = arr[a]
            index += 1
            a += 1
        elif arr[a] <= arr[b]:
            result[index] = arr[a]
            a += 1
            index += 1
        else:
            result[index] = arr[b]
            b += 1
            index += 1

    for i in range(index):
        arr[start + i] = result[i]

merge(0 ,7)
print(*arr)

# 퀵 정렬

# 4 1 7 9 6 3 3 6

# 퀵 정렬 핵심 코드
arr = list(map(int, input().split()))
pivot = arr[0]

a = 1
b = len(arr) - 1

while 1:
    while a < len(arr) and arr[a] <= pivot:
        a += 1
    while b >= 0 and arr[b] > pivot:
        b -= 1
    if a > b:
        break
    arr[a], arr[b] = arr[b], arr[a]

arr[0], arr[b] = arr[b], arr[0]
print(*arr)

arr = [4, 1, 7, 9, 6, 3, 3, 6]

def quick(start, end):
    if start >= end:
        return

    pivot = start
    a = start + 1
    b = end

    while 1:
        while a <= end and arr[a] <= arr[pivot]:
            a += 1
        while b >= start and arr[b] > arr[pivot]:
            b -= 1
        if a > b:
            break

        arr[a], arr[b] = arr[b], arr[a]

    arr[pivot], arr[b] = arr[b], arr[pivot]

    quick(start, b - 1)
    quick(b + 1, end)

quick(0, 7)
print(*arr)

# 우선순위 q
"""
우선순위 q 모듈
import heapq 좀 더 빠름
from queue import PriorityQueue
"""

import heapq

arr = [] # 함수 사용 시 이 리스트를 인자로 넘긴다!!

heapq.heappush(arr, 4)
heapq.heappush(arr, 7)
heapq.heappush(arr, 1)
heapq.heappush(arr, 2)
heapq.heappush(arr, 87)
heapq.heappush(arr, 23)
print(arr) # [1, 2, 4, 7, 87, 23]
# 우선순위 q 에서 default 값은 min heap 이다 0번 인덱스에만 큰 의미가 있다
print(heapq.heappop(arr)) # 1
print(heapq.heappop(arr)) # 2
print(heapq.heappop(arr)) # 4
print(heapq.heappop(arr)) # 7
print(heapq.heappop(arr)) # 23
print(heapq.heappop(arr)) # 87

for i in range(len(arr)):
    print(heapq.heappop(arr), end = ' ')

while arr:
    node = heapq.heappop(arr)
    print(node, end = ' ')


# 오름차순으로 출력하기 (우선순위큐 사용)
import heapq

arr = [234, 56, 234, 1, 45, 456, 23]
heap = []
for i in range(len(arr)):
    heapq.heappush(heap, arr[i])

for i in range(len(arr)):
    print(heapq.heappop(heap), end = ' ')

import heapq
arr = [234, 56, 234, 1, 45, 456, 23]
heapq.heapify(arr) #heapify를 이용해서 heap의 자료형으로 바꾸기

for i in range(len(arr)):
    print(heapq.heappop(arr), end = ' ')

# Max heap 으로 바꾸기 방법1

import heapq
arr =[34, 213, 57, 1, 2, 54, 2, 65]
heap = []

for i in range(len(arr)):
    heapq.heappush(heap, -arr[i])

for i in range(len(arr)):
    # print(heapq.heapop(heap) * -1)
    print(-heapq.heapop(heap))

# Max heap으로 바꾸기 방법 1-1
import heapq
arr = [34, 213, 57, 1, 2, 54, 2, 65]
heap = []
for i in range(len(arr)):
    heapq.heappush(heap, (-arr[i], arr[i]))

for i in range(len(arr)):
    print(heapq.heappop(heap)[1])

# Max heap으로 바꾸기 방법 2 [추천]
import heapq
arr=[34,213,57,1,2,54,2,65]

heap=list(map(lambda x:-x,arr))
heapq.heapify(heap)

for i in range(len(arr)):
    print(-heapq.heappop(heap),end=' ')

"""
카드 정렬하기

정렬된 두 묶음의 숫자 카드가 있다고 하자. 각 묶음의 카드의 수를 A, B라 하면 보통 두 묶음을 합쳐서 하나로 만드는 데에는 A+B 번의 비교를 해야 한다. 이를테면, 20장의 숫자 카드 묶음과 30장의 숫자 카드 묶음을 합치려면 50번의 비교가 필요하다.

매우 많은 숫자 카드 묶음이 책상 위에 놓여 있다. 이들을 두 묶음씩 골라 서로 합쳐나간다면, 고르는 순서에 따라서 비교 횟수가 매우 달라진다. 예를 들어 10장, 20장, 40장의 묶음이 있다면 10장과 20장을 합친 뒤, 합친 30장 묶음과 40장을 합친다면 (10 + 20) + (30 + 40) = 100번의 비교가 필요하다. 그러나 10장과 40장을 합친 뒤, 합친 50장 묶음과 20장을 합친다면 (10 + 40) + (50 + 20) = 120 번의 비교가 필요하므로 덜 효율적인 방법이다.

N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한지를 구하는 프로그램을 작성하시오.


입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100,000) 이어서 N개의 줄에 걸쳐 숫자 카드 묶음의 각각의 크기가 주어진다. 숫자 카드 묶음의 크기는 1,000보다 작거나 같은 양의 정수이다.


출력
첫째 줄에 최소 비교 횟수를 출력한다.

입력
4
50
20
70
30

출력
320


입력
3
10
20
40

출력
100
"""

import heapq

n = int(input())
card = []

for i in range(n):
    heapq.heappush(card, int(input()))

answer = 0
while len(card) > 1:
    temp1 = heapq.heappop(card)
    temp2 = heapq.heappop(card)

    answer += (temp1 + temp2)
    heapq.heappush(card, temp1 + temp2)

print(answer)

# Dijkstra 다익스트라 (데이크스트라)
# 최단거리 구할 때 사용
# Dijkstra Belmanford 알고리즘 -> 한 정점 (정점 1개) 에서부터 다른 모든 정점까지 최단거리
# Dijkstra 음수 가중치 없음을 가정
# Belmanford 음의 가중치가 존재할 수도 있음
# Floyd warshall -> 모든 정점에서 다른 모든 정점까지 최단 거리 (시작점 not Fixed) / 음의 가중치가 존재할 수 있음
# 단 Belmanford / Floyd warshall은 음수 사이클을 처리해줘야 한다


"""
      B
   3/ 1| \7
  A    E   C
  \9      /1    
      D
      
A : start
index A : 0 / B : 1 / C : 2 / D : 3 / E : 4
n ^ 2
priority queue -> nlogn 

result = [] => 시작점 A부터 다른 정렬까지 최소비용을 갱신해주는
used = [] => 경유지 선택을 check 해줄 배열

못 가는 경우 infinity 아주 큰 값으로 표시
0 3 inf 9 5
inf 0 7 inf 1
inf inf 0 1 inf
inf inf inf 0 inf
inf inf 1 inf 0

result = [0, 3, inf, 9, 5]
used = [1, 0, 0, 0, 0]

시작점에서 바로 가는 것 (result에 기록)과 시작점에서 경유지를 거쳐서 가는 것 중 적은 값을 갱신

시작점 A
경유지 선택하는 기준 : 시작점에서 가는 최소 비용인 경유지 먼저 선택
B 먼저 선택
used = [1, 1, 0, 0, 0]

시작점 -> 도착점
A -> B 3
시작점 -> 경유지 -> 도착점
A -> B -> B
3 + 0 = 3
갱신 X

시작점 -> 도착점
A -> C inf
시작점 -> 경유지 -> 도착점
A -> B -> C
3 + 7 = 10
10으로 갱신
result = [0, 3, 10, 9, 5]

시작점 -> 도착점
A -> D 9
시작점 -> 경유지 -> 도착점
A -> B -> D inf

시작점 -> 도착점
A -> E 5
시작점 -> 경유지 -> 도착점
A -> B -> E
3 + 1 = 4
[0, 3, 10, 9, 4]

다음 경유지 E
used = [1, 1, 0, 0, 1]
시작점 -> 도착점
A -> E 4
시작점 -> 경유지 -> 도착점
A -> E -> B inf

시작점 -> 도착점
A -> C 10
시작점 -> 경유지 -> 도착점
A -> E -> C 
4 + 1 = 5
5 갱신
result = [0, 3, 5, 9, 4]

시작점 -> 도착점
A -> D 9
시작점 -> 경유지 -> 도착점
A -> E -> D
inf

다음 경유지 C
used = [1, 1, 1, 0, 1]
시작점 -> 도착점
A -> B 3
시작점 -> 경유지 -> 도착점
A -> C -> B inf

시작점 -> 도착점
A -> D 9
시작점 -> 경유지 -> 도착점
A -> C -> D
5 + 1 = 6
6 갱신
result = [0, 3, 5, 6, 4]

다음 경유지 D
전부 7보다 작기 때문에 볼 필요 X but 인접 행렬에선 코드는 돌아감
"""

# 인접행렬 Dijkstra

name = "ABCDE"
inf = int(21e8)

arr = [
    [0, 3, inf, 9, 5],
    [inf, 0, 7, inf, 1],
    [inf, inf, 0, 1, inf],
    [inf, inf, inf, 0, inf],
    [inf, inf, 1, inf, 0]
]

used = [0] * 5
used[0] = 1 # 시작점은 경유지로 선택 안할 것임
result = [0, 3, inf, 9, 5] # 시작점 A에서 다른 모든 정점까지의 최소비용을 갱신 할 것임

def select_ky():
    Min = int(21e8)
    Minindex = 0
    for i in range(5):
        if used[i] == 0 and result[i] < Min:
            Min = result[i]
            Minindex = i

    return Minindex

def dijkstra():
    # 경유지 선택
    for i in range(4):
        via = select_ky()
        used[via] = 1

    # 시 -> 도 vs 시 -> 경 -> 도 비교 후 최소비용을 result에 갱신
        for j in range(5):
            baro = result[j] # 시작점에서 도착점 까지 바로 가는 비용
            kyung = result[via] + arr[via][j] # 시작점에서 경유지 / 경유지에서 도착점 까지 가는 비용

            if baro > kyung:
                result[j] = kyung

dijkstra()
print(*result)