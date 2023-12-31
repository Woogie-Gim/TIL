# 2798 블랙잭
# N개에서 몇개 고르는 전형적인 문제
# 백트래킹 / 라이브러리 가능하지만 IM 수준에선 그냥 구현 가능
# IM 수준에선 보통 그냥 전체 순화
# 1. N 개 중 2개 뽑는 모든 조합 뽑기로 먼저 살펴 보기
"""
N = 5
1st
5 6 7 8 9
0 1 2 3 4
i j
i 를 하나 선택해서 뽑는 모든 경우의 수
i 를 옆으로 옮겨가면서 중복 없이 뽑아가는 과정

for i in range(0, N -1) # 인덱스 에러 방지
    for j in range(i + 1, N) # i 옆에서 시작
"""

"""
3장을 뽑는 경우

0 1 2 3 4 5
i j k

i, j 를 고정한 상태에서 k를 이동시키면서 탐색

j 1칸씩 이동 j가 끝까지 갔을 때
i 1칸 이동

최종적으로 i = 3 j = 4 k = 5 일 때 종료

ans = 0
for i in range(0, N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if ans < lst[i] + lst[j] + lst [k] <= M:
                ans 갱신            
"""

# 정답 코드
# N, M = map(int, input().split())
# lst = list(map(int, input().split()))
#
# ans = 0 # 변수를 생성할 때는 위치 / 초기값 고민후 작성
# for i in range(N - 2):
#     for j in range(i + 1, N - 1):
#         for k in range(j + 1, N):
#             if ans < lst[i] + lst[j] + lst[k] <= M:
#                 ans = lst[i] + lst[j] + lst[k]
#
# print(ans)


# 2309 일곱난쟁이
# 예를 들어 9명의 합이 132 라면 7명의 합이 100 이기 때문에 (예외 케이스 없음)
# 난쟁이가 아닌 2명의 합이 32 이기 때문에 2명의 합이 32 찾기
# 원하는 코드를 짜고 함수를 짠다
# def solve():
#     N = 9
#     num = sum(arr) - 100 # 찾아야할 숫자를
#     for i in range(N - 1):
#         for j in range(i + 1, N):
#             if arr[i] + arr[j] == num:
#                 return arr[i], arr[j]
#
#
# arr = [int(input()) for _ in range(9)]
# n, m = solve() # 7명에 포함되지 않는 2명 찾기
#
# for i in sorted(arr):
#     if i != n and i != m:
#         print(i)

# 2567 색종이 2
# flood fill 먼저 생각 X 단순 loop 순환 먼저 생각
# 1) arr[] -> 1로 색종이 표시
# -> 전체 순회 하면서 1 주변에 상하좌우의 0과 만나는 개수의 합
# 2) 0에서 1로 바뀌는 부분 부터 1에서 0으로 변하는 부분 열 / 행 모두 탐색
"""
cnt = 0
for lst in arr:
    for i in range(1, len(lst))
        if lst[i - 1] != lst[i]:
            cnt += 1
    return cnt
"""
# def count(arr):
#     cnt = 0
#     for lst in arr:
#         for i in range(1, len(lst)):
#             if lst[i - 1] != lst[i]:
#                 cnt += 1
#     return cnt
#
# N = int(input())
# arr = [[0] * 102 for _ in range(102)]
#
# for _ in range(N):
#     sj, si = map(int, input().split())
#     for i in range(si, si + 10):
#         for j in range(sj, sj + 10):
#             arr[i][j] = 1
#
# arr_t = list(zip(*arr)) # 전치 행렬 : 수정 필요시 list(map(list, zip(*arr)) / 튜플 형태 이기 때문
# ans = count(arr) + count(arr_t)


# 10163 색종이
# [1] 색종이 번호를 arr에 기록
# 제일 오래 걸리는 방법
"""
1) 찾기
for n (1, N + 1)

cnt = 0
for lst in arr;
cnt += ls.count(n)
"""
# [1] 색종이 개수별로 전체 arr를 순회 : 시간 오래 걸림
# N = int(input())
# arr=  [[0] * 1001 for _ in range(1001)]
# for n in range(1, N + 1):
#     sj, si, w, h = map(int, input().split())
#     for i in range(si, si + h):
#         for j in range(sj, sj + w): # 해당번호 색종이 숫자 영역에 표사
#             arr[i][j] = n
#
# for n in range(1, N + 1):
#     cnt = 0
#     for lst in arr:
#         cnt += lst.count(n)
#     print(cnt)

"""
2) 빈도수 체크
0 은 사용하지 않음
=> arr 를 1번 순회 하면서 cnt[arr[i][j]] += 1
"""
# [2] cnts : 빈도수 배열 사용해서, arr 한번만 순회
# N = int(input())
# arr=  [[0] * 1001 for _ in range(1001)]
# for n in range(1, N + 1):
#     sj, si, w, h = map(int, input().split())
#     for i in range(si, si + h):
#         for j in range(sj, sj + w): # 해당번호 색종이 숫자 영역에 표사
#             arr[i][j] = n
#
# cnts = [0] * (N + 1)
# for lst in arr:
#     for n in lst:
#         cnts[n] += 1
#
# print(*cnts[1:], sep = '\n')

# 조금 더 개선
# N = int(input())
# arr=  [[0] * 1001 for _ in range(1001)]
# for n in range(1, N + 1):
#     sj, si, w, h = map(int, input().split())
#     for i in range(si, si + h):
#         # 하나씩 표시하는 방법
#         # lst 단위로 표시
#         arr[i][sj : sj + w] = [n] * w
#
# cnts = [0] * (N + 1)
# for lst in arr:
#     for n in lst:
#         cnts[n] += 1
#
# print(*cnts[1:], sep = '\n')

# 8320 직사각형을 만드는 방법
# 1) 가능한 세로, 가로 체크
"""
for i (1, N + 1): # 세로
    for j (i, N + 1): # 가로
        if i * j <= N:
            ans += 1
"""
# N = int(input())
#
# ans = 0
# for i in range(1, N + 1):
#     for j in range(i, N + 1):
#         if i * j <= N:
#             ans += 1
#
# print(ans)

# 2) 그리디 / 규칙성
# N // i 개수 2 -> 1 개 빼고 3 -> 2개 빼고

# [2] 몫 연산을 통해서 처리
# N = int(input())
# ans = N
#
# for i in range(2, N):
#     n = N // i - (i - 1)
#     if n < 1:
#         break
#     ans += n
# print(ans)

# swea 4613 러시아 국기 같은 깃발
# IM 무조건 전체를 순회 혹은 반복(완전 탐색) backtracking도 아니고 loop -> 가능한 모든 처리
# N 개에서 2개를 뽑아서 (변형)범위를 3개로
# 흰색은 (0, i + 1) 파란색은 (i + 1, j + 1) 빨간색은 (j + 1, N)
"""
for i (0, N - 2)
for j (i + 1, N - 1) # 가능한 모든 i, j 기준선
for s (i + 1) : W 색을 누적
cnt += arr[s].count('W')
for s (i + 1, j + 1):
cnt += arr[s].count('B')

mx = max(mx, count)
"""

# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = [input() for _ in range(N)]
#
#     mx = 0
#     for i in range(N - 2):
#         for j in range(i + 1, N - 1):
#             cnt = 0
#             for s in range(i + 1):
#                 cnt += arr[s].count('W')
#             for s in range(i + 1, j + 1):
#                 cnt += arr[s].count('B')
#             for s in range(j + 1, N):
#                 cnt += arr[s].count('R')
#             mx = max(mx, cnt)
#
#     print(f'#{tc} {N * M - mx}')

# 2628 종이 자르기
# 익숙한 arr 에 0, 1 저장 -> 불편
# => column list / row_list => 오름차순으로 sort()
# C, R = map(int, input().split())
# r_lst = [0, R]
# c_lst = [0, C]
# N = int(input())
# for _ in range(N):
#     t, n = map(int, input().split())
#     if t == 0:
#         r_lst.append(n)
#     else:
#         c_lst.append(n)
#
# r_lst.sort()
# c_lst.sort()
#
# # [2] 가장 긴 길이 찾기
# r_mx = 0
# for i in range(1, len(r_lst)):
#     r_mx = max(r_mx, r_lst[i] - r_lst[i - 1])
#
# c_mx = 0
# for i in range(1, len(r_lst)):
#     c_mx = max(c_mx, c_lst[i] - c_lst[i - 1])
#
# print(r_mx * c_mx)