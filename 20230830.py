# Union - Find 자료 구조
# 최소 비용
# MST (Minimum Spanning Tree)
# 최소 신장 트리 -> 크루스칼 알고리즘

# Union - Find
# 독립된 data를 그룹화 시켜서 data를 관리하는 자료구조

"""
자료 구조 a b c d e f
arr
0 0 0 0 0 0
a b c d e f

union('a', 'b')
a와 b를 같은 그룹화
이미 같은 그룹이면 그룹화 필요 x
       a가 속한 그룹의 보스는 a
0 a 0 0 0 0
a b c d e f

union('d', 'e')
d와 e를 같은 그룹화
이미 같은 그룹이면 그룹화 필요 x
보스 확인
      d가 속한 그룹의 보스는 d
0 a 0 0 d 0
a b c d e f

union('b', 'e')
b가 속한 그룹과 e가 속한 그룹을 그룹화
b -> a -> 0 보스 a
e -> d -> 0 보스 d
보스가 다르므로 그룹화
e 가 속한 그룹에 b 가 속한 그룹의 보스를 추대

0 a 0 a d 0
a b c d e f

보스 찾기 e -> d -> a -> 0 a 가 보스

union('b', 'd')
보스가 a로 같으므로 그룹화 필요 x

union('e', 'f')

0 a 0 a d a
a b c d e f

-> a c 입력 다른 그룹
-> b f 입력 같은 그룹
"""

# 문자 2개 입력 받은 후 두 문자가 같은 그룹인지 아닌지 출력
arr = [0] * 200

def findboss(member):
    global arr
    if arr[ord(member)] == 0:
        return member

    ret = findboss(arr[ord(member)]) # 0이 나올 때까지 재귀를 타고 들어감
    return ret

def union(a, b):
    global arr
    fa, fb = findboss(a), findboss(b)
    if fa == fb:
        return
    arr[ord(fb)] = fa

union('a', 'b')
union('d', 'e')
union('b', 'e')
union('b', 'd')
union('e', 'f')

y, x = input().split()

# 같은 그룹인지 아닌지 출력
if findboss(y) == findboss(x):
    print('같은 그룹')
else:
    print('다른 그룹')


"""
            A
       B         C
          
          D   E
          
정점을 연결할 수 있는 최소 간선의 개수 (정점의 개수 - 1)

MST 최소 신장트리 : 최소한의 간선으로 연결시킨 그래프프
"""

"""
6 5
A B
B C
D E
A D
C D
        0
        A
       / \
    A  B  \   E 0
        \  \ /    
    A    C -D A
Cycle 발생

5 4
A B
B D
C D
A E
          
          A
        /
       B  E
        \/
    C - D
"""
def findboss(member):
    global arr
    if arr[ord(member)] == 0:
        return member
    ret = findboss(arr[ord(member)])
    return ret


def union(a, b):
    global arr
    fa, fb = findboss(a), findboss(b)
    if fa == fb:
        return 1
    arr[ord(fb)] = fa


n, m = map(int, input().split())
edge = []
for _ in range(m):
    edge.append(input().split())

arr = [0] * 200

answer = 0
for i in range(m):
    a, b = edge[i]
    ret = union(a, b) # 보스가 같으면 1 리턴
    if ret == 1:
        answer = 1
        break

# cycle 발견 출력 또는 cycle 미발견 출력하기
if answer == 1:
    print('cycle 발견')
else:
    print('cycle 미발견')


#리턴 될 때마다 보스 갱신
def findboss(member):
    global arr
    if arr[ord(member)] == 0:
        return member
    ret = findboss(arr[ord(member)])
    arr[ord(member)] = ret # 최고 보스로 갱신해서 찾는 경로를 한번 탐색으로 단축시킬 수 있다
    return ret


def union(a, b):
    global arr
    fa, fb = findboss(a), findboss(b)
    if fa == fb:
        return 1
    arr[ord(fb)] = fa


n, m = map(int, input().split())
edge = []
for _ in range(m):
    edge.append(input().split())

arr = [0] * 200

answer = 0
for i in range(m):
    a, b = edge[i]
    ret = union(a, b) # 보스가 같으면 1 리턴
    if ret == 1:
        answer = 1
        break

if answer == 1:
    print('cycle 발견')
else:
    print('cycle 미발견')

# Kruskal Algorithm

"""
5 8
A B 9 (연결 시키는데 드는 비용)
A C 3
A E 7
A D 20
B C 14
B D 11
C D 1
C E 5
최소 비용으로 섬 연결시키기
크루스칼 / 그리디
1. 최소 비용 나오게끔 sort
2. boss가 같지 않게 / cycle 발생 안하게 체크
3. 최소 비용
4. cnt 를 통해서 노드 - 1 개 최소가 될 때 최소 비용 찾기
"""
def findboss(member):
    if not group[ord(member)]:
        return member

    ret = findboss(group[ord(member)])
    group[ord(member)] = ret
    return ret



def union(x, y, i):
    global group, total, cnt
    x_boss, y_boss = findboss(x), findboss(y)
    if x_boss == y_boss:
        return
    cnt += 1
    total += int(lst[i][2])
    group[ord(y_boss)] = x_boss



n, m = map(int, input().split())
lst = [list(input().split()) for _ in range(m)]
group = [0] * 200
lst.sort(key = lambda x:int(x[2]))

total = 0 # 총 공사비용
cnt = 0 # 연결시킨 선의 개수

for i in range(m):
    if cnt == n - 1:
        print(total)
        break

    union(lst[i][0], lst[i][1], i)