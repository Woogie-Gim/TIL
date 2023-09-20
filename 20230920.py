"""
"""
# Greedy
# 상황이 주어졌을 때 내가 당장 이득이 되는 것을 선택함

# 백준 11399

n = int(input())
time_wait = list(map(int, input().split()))

time_wait.sort(reverse = True)
answer = 0
for i in range(1, n + 1):
    answer += (i * time_wait[i - 1])

print(answer)

# 백준 1931 회의실 배정

arr = []
n = int(input())

for _ in range(n):
    arr.append((list(map(int, input().split()))))

# 파티가 끝나는 시간 기준으로 sort
arr.sort(key = lambda x : (x[1], x[0]))

endtime = 0
answer = 0

for i in range(len(arr)):
    if endtime <= arr[i][0]:
        endtime = arr[i][1]
        answer += 1

print(answer)


# DP (Dynamic Programming) : 동적 계획법
# 계획이 동적이다
# TopDown - 재귀를 이용하여 한번 했던 연산을 반복하지 않도록
# BottomUp - 작은 문제를 해결하면서 결국 큰 문제까지 해결하는 방식

arr = [0, 7, -3, -5, -4, -2, 6, 5, -9, -1, 0]

dp = [0] * len(arr)
for i in range(1, len(arr)):
    jp1 = dp[i - 1]
    jp2 = dp[i - 2]
    jp3 = dp[i // 2]
    dp[i] = jp1 + arr[i]
    if dp[i] < jp2 + arr[i]:
        dp[i] = jp2 + arr[i]
    if i % 2 == 0 and dp[i] < jp3 + arr[i]:
        dp[i] = jp3 + arr[i]

print(dp[-1])

# (0, 0) 좌표에서 (3, 3) 까지 갔을 때 땅을 밟았을 때 유류비가 든다 최단 거리로 최소 비용
# bfs dfs 시간초과 가정

# ver1.
arr=[[0,1,2,2],
    [1,3,4,1],
    [5,8,1,4],
    [9,1,78,0]]

accu = [[0] * 4 for _ in range(4)]

def sett():
    for i in range(2,-1,-1):
        accu[i][3]=accu[i+1][3]+arr[i][3]
        accu[3][i]=accu[3][i+1]+arr[3][i]

sett()
for i in range(2,-1,-1):
    for j in range(2,-1,-1):
        down=accu[i+1][j]
        right=accu[i][j+1]

        if down>right:
            value=right
        else: value=down

        accu[i][j]=value+arr[i][j]
print(accu[0][0])

# ver2
arr=[[0,1,2,2],
    [1,3,4,1],
    [5,8,1,4],
    [9,1,78,0]]


dp = [[0] * 4 for _ in range(4)]

for i in range(1,4):
    dp[0][i] = dp[0][i - 1] + arr[0][i]
    dp[i][0] = dp[i - 1][0] + arr[i][0]

for i in range(1,len(arr)):
    for j in range(1,len(arr)):
        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + arr[i][j]

print(dp[3][3])

# 12865 배낭

n, k = map(int, input().split())
knapsack = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

item = [[0, 0]]
for i in range(1, n + 1):  # 아이템 입력
    item.append(list(map(int, input().split())))

for i in range(1, n + 1):  # 아이템의 개수 만큼 반복
    for j in range(1, k + 1):  # 최대 무게까지 반복
        w = item[i][0]
        value = item[i][1]
        if j < w:  # 가방에 넣을 수 없다면..
            knapsack[i][j] = knapsack[i - 1][j]
        else:  # 가방에 넣을 수 있다면..
            knapsack[i][j] = max(knapsack[i - 1][j], value + knapsack[i - 1][j - w])
            # 위에값     vs   현재아이템 가치+전 단계에서 구한 남은 무게 가치

print(knapsack[n][k])

# 백준 2294

n, k = map(int, input().split())
coin = [0]
for i in range(n):
    don = int(input())
    coin.append(don)

arr = [[10001] * (k + 1) for _ in range(n + 1)]

arr[0][0] = 0
coin.sort()

for i in range(1, n + 1):
    for j in range(1, k + 1):
        mok = j // coin[i]
        if j % coin[i] == 0:
            arr[i][j] = mok
        else:
            if mok == 0:
                arr[i][j] = arr[i - 1][j]
            else:
                arr[i][j] = min(arr[i - 1][j], arr[i][j - coin[i]] + 1)

if arr[n][k] >= 10001:
    print(-1)
else:
    print(arr[n][k])