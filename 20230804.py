# 삼성시 버스노선

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    cnt = [0] * 5001
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B + 1):
            cnt[i] += 1

    P = int(input())
    bus_stop = [int(input()) for _ in range(P)]
    print(f'#{test_case}', end=' ')
    for x in bus_stop:
        print(cnt[x], end=' ')
    print()


# 1979 어디에 단어가 들어갈 수 있을까

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j]:
                cnt += 1
            if j == N - 1 or arr[i][j] == 0:
                if cnt == K:
                    ans += 1
                cnt = 0


# 16268 풍선팡 2

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0

    for i in range(N):
        for j in range(M):
            cnt = arr[i][j] # 터트린 풍선의 꽃가루 수
            for k in range(4): # i, j 인접에 대해
                ni, nj = i+di[k], j+dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    cnt += arr[ni][nj]
            if max_v < cnt:
                max_v = cnt

    print(f'#{tc} {max_v}')