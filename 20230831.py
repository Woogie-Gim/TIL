# 위상 정렬 topolgical sort
# 작업공정의 순서를 정할 때

"""
(0)cs
(1) Language -> (2) datastructure -> (5) coding test -> (6) be a programmer
          \      \                     /                 /
           \       (3) algorithm                        /
                               (4) project

acc
0 0 1 1 1 2 3     => 사전 작업 개수
0 1 2 3 4 5 6

queue = [0, 1 ...] => 작업 가능한 것들 순서대로 들어감
         now
            now
queue = [2, 3, ... ]
         now
            now
queue = [4, 5, ...]
         now
            now

now 이 후에 할 수 있는 일들에 대해 사전 작업 개수를 1씩 감소 시켜 가며 확인
queue 순서 자체가 작업순서
"""

from collections import deque
name = ['cs', 'language', 'datastructure', 'algorithm', 'project', 'codingtest', 'beaprogrammer']

arr = [[0, 0, 0, 0, 0, 0, 1],
       [0, 0, 1, 1, 1, 0, 0],
       [0, 0, 0, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 0, 1],
       [0, 0, 0, 0, 0, 0, 1],
       [0, 0, 0, 0, 0, 0, 0]]

acc = [0] * 7 # 사전 작업 개수

# 사전 작업 개수 등록
for j in range(7):
    for i in range(7):
        if arr[i][j] == 1:
            acc[j] += 1

q = deque()

# 당장 사전작업 없이 착수할 수 있는 것 넣어주기
for i in range(7):
    if acc[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    print(name[now])
    for i in range(7):
        if arr[now][i] == 1: # 작업을 할 수 있을 때
            acc[i] -= 1 # 작업 개수가 1개 남았다면
            if acc[i] == 1: # 작업개수 1빼고
                acc[i] -= 1 #사전작업이 다 없어 졌으므로 큐에 푸쉬
                q.append(i)
            else:
                acc[i] -= 1 # 필요한 작업개수를 1개 감소
