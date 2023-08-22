# Tree의 순회

"""
    A
  B   C
D E  F G

- 전위 순회 pre-order
  A - B - D - E - C - F - G
  출력 하고 탐색
- 후위 순회 post-order'
  D - E - B - F - G - C - A
  왼쪽 오른쪽 모두 탐색하고 출력
- 중위 순회 in order
  D - B - E - A - F - C - G
  왼쪽 보고 나와서 출력하고 오른쪽 들어가고
"""
# 전위 순회
'''
_ A 
자식 인덱스 중 왼쪽 자식은 부모노드 인덱스 *2 한 인덱스에 저장
오른쪽 자식은 부모노드 인덱스 * 2 + 1 한 인덱스에 저장
*2 를 위해서 0번 인덱스 비워두고 루트 노드를 1번인덱스에 저장을 하고 시작
'''
# name = " ABCDEFG" # 한칸 띄고
# def preorder(now):
#
#     if now > len(name) - 1:
#         return
#     print(name[now], end = ' ')
#     preorder(now * 2)
#     preorder(now * 2 + 1)
#
#
# preorder(1)

# 후위 순회
# name = " ABCDEFG" # 한칸 띄고
#
# def postorder(now):
#     if now > len(name) - 1:
#         return
#
#     postorder(now * 2)
#     postorder(now * 2 + 1)
#
#     print(name[now], end = ' ')
#
# postorder(1)

# 중위 순회
# name = " ABCDEFG"
#
# def inorder(now):
#     if now > len(name) - 1:
#         return
#
#     inorder(now * 2)
#     print(name[now], end = ' ')
#     inorder(now * 2 + 1)
#
# inorder(1)

# Binary Search Tree (자료 구조)
# [4, 2, 9, 1, 15, 7] -> Tree 형으로
"""
루트 노드는 1번인덱스
부모보다 작으면 왼쪽(부모 * 2) 부모보다 크면 오른쪽 (부모 * 2 + 1)
        4
      2     9
    1   _ 7   15
    
    
  4 2 9 1   7 15
0 1 2 3 4 5 6 7 8 9

예를 들어 5가 있는지 탐색할 때
루트 노드 4보다 크기 때문에 오른쪽으로
9 번 -> 5가 작기 때문에 왼쪽
7 번 -> 5가 작기 때문에 왼쪽
배열 범위를 벗어나거나 값이 0일 때

탐색 횟수 = 트리의 높이 (O(log(2)n) - 탐색 개수) // BS -> O(n)

예를 들어
1 2 4 7 9 15
의 경우 다 오른쪽으로 입력 높이만 커짐
거의 O(n) 가까운 속도가 날 수 있음

이럴 경우 이진모양으로 바꿔주는 레드 블랙 트리 알고리즘(거의 쓸 일 없음), B - tree (DB에서 인덱스 찾는 알고리즘)

BST
왼쪽 자식노드에는 부모노드 보다 작은 값
오른쪽 자식노드에는 부모노드 보다 큰 값을
저장 함으로써 평균적으로 logN의 속도로 저장하고 써치하는 자료구조
그런데 입력되는 data에 따라 최악의 경우 O(n) 속도가 날 수 있는데
이때에는 Balanced tree로 만들어주는 알고리즘을 사용하면 logN에 가까운 속도로 서치가 가능합니다.
balanced tree로 만들어주는 대표적인 알고리즘으로 red - black tree / b-tree가 있습니다
"""

lst = [4, 2, 9, 1, 15, 3]
arr = [0] * 20

def insert(target):
    now = 1
    while 1:
        if arr[now] == 0:
            arr[now] = target
            return

        if arr[now] < target: # index값 / 전달 받은 값
            now = now * 2 + 1
        elif arr[now] > target:
            now = now * 2


# lst 배열을 tree 형태로 저장
for i in lst:
    insert(i) # 4 2 9 1 15 3


# 숫자 1개 입력받고 입력받은 숫자가 존재하는 지 존재 여부 출력

def Search(target):
    now = 1

    while 1:

        if now >= 20:
            return 0
        if arr[now] == 0:
            return 0
        if arr[now] == target:
            return 1
        if arr[now] > target:
            now = now * 2 + 1
        else:
            now = now * 2


n = int(input())
ans = Search(n)
if ans:
    print('찾음')
else:
    print('없음')

# heap / heap sort / priority queue
# 항상 완벽한 이진 Tree 형태로 저장이 된다
# heap sort를 통해서 자료를 출력할 때도 안정적으로 logN 의 속도를 유지
# 개발자가 우선순위를 두고 우선순위에 맞게 값을 출력
# 우선순위가 높은 것은 부모노드에 와 있어야만 하고 우선순위가 낮은 것은 자식 노드에 와 있어야만 한다
# 무조건 트리의 끝에 붙인 후 부모와 자식을 비교하여 우선순위에 따라 스왑

# heap sort
# 우선 순위가 가장 높은 것 부터 뽑아서 출력을 하는 방법
# 트리 끝에 있는 걸 가장 위에 올리고 부모 자식 간을 비교 하여 다시 스왑 해 가면서
# 우선순위가 가장 높은 요소가 루트 노드에 왔을 때 pop


# max heap
arr = [6, 4, 1, 2, 6, 4, 8, 43]
heap = [0] * 30
hindex = 1  # 1번 인덱스 부터 값 넣기


def insert(value):
    global hindex
    heap[hindex] = value
    now = hindex
    hindex += 1

    while 1:
        p = now // 2  # 부모 인덱스 구하기
        if p == 0: break  # 루트노드
        if heap[p] >= heap[now]: break  # 부모값이 방금 들어오 값보다 크면 break
        heap[p], heap[now] = heap[now], heap[p]  # 부모가 방금 들어오 값보다 작으면 swap
        now = p  # 그다음 부모가 now가 됨 (부모의 부모랑 비교)


def top():
    return heap[1]


def pop():
    global hindex
    hindex -= 1
    heap[1] = heap[hindex]
    heap[hindex] = 0

    now = 1
    while 1:
        son = now * 2
        rson = son + 1

        if rson <= hindex and heap[son] < heap[rson]: son = rson
        if son > hindex or heap[now] > heap[son]: break
        heap[now], heap[son] = heap[son], heap[now]
        now = son


for i in range(len(arr)):  # 이진 트리 만들기
    insert(arr[i])

for i in range(len(arr)):
    print(top(), end=' ')  # 우선순위가 가장 높은것은 출력하는 함수
    pop()  # 출력후 빼오기

def insert(value):
    global hindex
    heap[hindex] = value  # 전달받은 값을 트리의 맨 뒤에 넣기
    now = hindex
    hindex += 1

    while 1:
        p = now // 2  # 부모 인덱스 구하기
        if p == 0: break  # 루트노드
        if heap[p] >= heap[now]: break  # 부모값이 방금 들어오 값보다 크면 break
        heap[p], heap[now] = heap[now], heap[p]  # 부모가 방금 들어오 값보다 작으면 swap
        now = p  # 그다음 부모가 now가 되어 (부모의 부모랑 비교)
        # 트리의 위로 올라가면서 부모가 더 작으면 swap 계속 진행


def top():
    return heap[1]  # 우선순위가 가장높은 1번 인덱스의 값 출력


def pop():
    global hindex
    hindex -= 1
    heap[1] = heap[hindex]  # 트리의 가장 마지막에 있는 값을 트리의 루트로 올리기
    heap[hindex] = 0  # 맨 마지막에 있던 값을 0으로 지우기

    now = 1
    while 1:
        son = now * 2  # 왼쪽자식
        rson = son + 1  # 오른쪽자식

        # 오른쪽에 자식이 있고 그리고 오른쪽 자식이 왼쪽 자식보다 크다면
        # 오른쪽 자식을 부모랑 비교하는 비교대상으로 놓겠다.
        # 왼쪽 자식만 있거나 왼쪽자식이 오른쪽자식보다 크다면 비교대상은 왼쪽 자식이다.
        if rson <= hindex and heap[son] < heap[rson]: son = rson

        # 왼쪽자식(or오른쪽자식)이 없거나 자식이 부모가 자식보다 크다면 break
        if son > hindex or heap[now] > heap[son]: break
        heap[now], heap[son] = heap[son], heap[now]
        now = son  # 트리의 밑으로 내려가면서 자식이 더 밑에있는 자식과 비교해서 더 큰지를 확인을 계속함


for i in range(len(arr)):  # heap 이진 트리 만들기
    insert(arr[i])

for i in range(len(arr)):
    print(top(), end=' ')  # 우선순위가 가장 높은것은 출력하는 함수
    pop()  # 출력후 빼오기