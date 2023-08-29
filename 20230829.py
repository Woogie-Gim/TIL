# 최대공약수 / 최소공배수 / 소수구하기 / Sliding window / two pointer

# 최대공약수 Greatest Common Division

N, M = map(int, input().split())
ans = 0
for i in range(2, min(N, M) + 1):
    if N % i == 0 and M % i == 0:
        ans = i

print(ans)

# 유클리드 호제법 -> 연산 회수가 줄어든다
#               -> 최초의 알고리즘

"""
36  24
    24로 나눈 나머지
24  12
     12로 나눈 나머지
12   0 <- 이 구간에서 0이 나왔을 때
12 는 최대 공약수


30   75
75   30
30   15
15    0 <- 최대 공약수는 15

a    b
b   a%b
.
.
.
      0 일 때 최대 공약수
"""

"""
유클리드 호제법 내 코드
n, m = map(int, input().split())

while m:
    temp = n
    n = m
    m = temp % m

print(n)
"""

# 유클리드 호제법 교수님 코드

a, b = map(int, input().split())
temp = 0

while b:
    temp = a % b
    a = b
    b = temp

print(a)

# 최소 공배수 (Least Common Multiple)

"""
LCM = GCD * (a / GCD) * (b / GCD)

ex) 8 36
gcd = 4
lcm = 4 * (8 / 4) * (36 / 4) = 72
"""

# prime number
# 1과 자기 자신으로만 나눌 수 있는 수

a = int(input())
ans = []

for i in range(2, a + 1):
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag = 1 # 소수 아님
            break
    if flag == 0:
        ans.append(i)

print(ans)

# 소수 구하는 알고리즘 - 에라토스테네스의 체

"""
1   2   3   4   5   6   7   8   9   10
11  12  13  14  15  16  17  18  19  20
21  22  23  24  25  26  27  28  29  30
31  32  33  34  35  36  37  38  39  40
41  42  43  44  45  46  47  48  49  50

1 제외 해당하는 수 보다 큰 배수를 지워 나감

1   2   3      5      7      9   
11     13     15     17     19  
21     23     25     27     29  
31     33     35     37     39  
41     43     45     47     49

1   2   3     5      7        
11     13          17     19  
     23     25          29  
31          35     37       
41     43        47     49


1    2   3    5    7        
11     13          17     19  
     23               29  
31               37       
41     43        47     49

2  3  5  7                        
11     13          17     19  
     23               29  
31               37       
41     43        47     

내 코드
n = int(input())
ans = []
for k in range(2, n):
    ans.append(k)

for i in range(2, 8):
    for j in range(i, n):
        if not j in ans:
            continue
        if i == j:
            continue
        if j % i == 0:
            ans.remove(j)

print(ans)
"""

# 교수님 코드
import math
a = int(input())
end = int(math.sqrt(a)) # 제곱근 구하기
# end = int(a ** 0.5)
check = [0] * (a + 1) # 소수 체크 1 체크 시 소수 아님

for i in range(2, end + 1):
    if check[i] == 1:
        continue
    for j in range(i + i, a + 1, i): # i가 2일 때 4부터 2씩 증가된 값을 지우기
        check[j] = 1

for i in range(2, a + 1):
    if check[i] == 0:
        print(i, end = ' ')

# Sliding Window
# 연속되는 구간 합
# 10개의 정수입력 연속하는 2개의 합 중에 max 값 출력
# O(n)의 속도로 해결할 수 있음

# n 개의 정수에서
# m 사이즈의 연속 되는 구간의 합 중
# 가장 큰 값 출력하기

n, m = map(int, input().split())
arr = list(map(int, input().split())) # n 개의 정수 입력

sum = 0

for i in range(m):
    sum += arr[i]

Max = sum

for i in range(n - m):
    sum += arr[i + m]
    sum -= arr[i]
    if sum > Max:
        Max = sum

print(Max)

# two pointer
# 구간 합을 구할 때 사용
# 구간의 size가 정해지지 않은 구간의 합을 구할 때 two pointer 사용

# n : 10 - 정수의 개수 / m : 5 - 타겟 (구간의 합이 5가 되는 경우 찾기)
# 1 2 3 4 2 5 3 1 1 2
# Q. 10개의 정수 중 구간의 합이 5가 되는 경우??

"""
high
1 2 3 4 2 5 3 1 1 2
low

pointer를 두개 만들어줌
sum = 0
target = 5
구간합이 target 이 되는 경우의 수

결론 : 합이 target 보다 크거나 같다면 범위를 좁혀주기
합이 target 보다 작다면 범위를 넓혀주기
  h
1 2 3 4 2 5 3 1 1 2
l
sum = 1
범위 늘려주기

    h
1 2 3 4 2 5 3 1 1 2
l
sum = 3
범위 좁혀주기

    h
1 2 3 4 2 5 3 1 1 2
  l
sum = 2
cnt += 1
범위 좁혀주기

    h
1 2 3 4 2 5 3 1 1 2
    l
sum = 0
범위 늘려주기

      h
1 2 3 4 2 5 3 1 1 2
    l
sum = 3
범위 좁혀주기

      h
1 2 3 4 2 5 3 1 1 2
      l
sum = 0
범위 늘려주기

        h
1 2 3 4 2 5 3 1 1 2
      l
sum = 4
범위 늘려주기

          h
1 2 3 4 2 5 3 1 1 2
      l
sum = 6
범위 좁혀주기

          h
1 2 3 4 2 5 3 1 1 2
        l
sum = 2
범위 늘려주기

            h
1 2 3 4 2 5 3 1 1 2
        l
sum = 7
범위 좁혀주기

            h
1 2 3 4 2 5 3 1 1 2
          l
sum = 5
cnt += 1
범위 좁혀주기

            h
1 2 3 4 2 5 3 1 1 2
            l
sum = 0
범위 늘려주기

              h
1 2 3 4 2 5 3 1 1 2
            l
sum = 3
범위 늘려주기

                h
1 2 3 4 2 5 3 1 1 2
            l
sum = 5
cnt += 1
범위 좁혀주기

                h
1 2 3 4 2 5 3 1 1 2
              l
sum = 1
범위 늘려주기

                  h
1 2 3 4 2 5 3 1 1 2
              l
sum = 2
범위 늘려주기

                    h
1 2 3 4 2 5 3 1 1 2
              l
sum = 4
범위 늘려주기
h 가 끝을 넘어갔을 때 도착했을 때 l 만 밀어주기
                    h
1 2 3 4 2 5 3 1 1 2
                l
sum = 3
                    h
1 2 3 4 2 5 3 1 1 2
                  l
sum = 2
n = l 
끝
"""

n, target = map(int, input().split())
arr = list(map(int, input().split()))
sum, cnt = 0, 0
high, low = 0, 0


while 1:
    if sum >= target or high == n:
        sum -= arr[low]
        low += 1
    elif sum < target:
        sum += arr[high]
        high += 1
    if sum == target:
        cnt += 1
    if low == n:
        break

print(cnt)
