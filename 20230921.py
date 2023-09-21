"""
"""
# LCS / LIS

# LCS - Longest Common Substring (최장 공통 부분 문자열) / Longest Common Subsequence (최장 공통 부분 수열)
# LIS - Longest Increasing Subsequence (최장 증가 부분 수열)


# LCS 최장공통 부분 문자열 (Longest Common Substring)
"""
s1 = "BABJYP"
s2 = "ABCBJY"
연속된 공통 문자열의 길이가 가장 길 때 그 길이는?

        B   A   B   J   Y   P
    0   0   0   0   0   0   0   
A   0   0   1   0   0   0   0    
B   0   1   0   2   0   0   0  
C   0   0   0   0   0   0   0
B   0   1   0   1   0   0   0
J   0   0   0   0   2   0   0
Y   0   0   0   0   0   3   0

비교하는 두 문자가 같다면 11시 방향 값 + 1을 넣을 것
같지 않으면 0
"""

def lcs(s1, s2):
    len1, len2 = len(s1), len(s2)
    arr = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    Max = 0

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if s1[i - 1] == s2[j - 1]:
                arr[i][j] = arr[i - 1][j - 1] + 1
                Max = max(Max, arr[i][j])
            else:
                arr[i][j] = 0

    return Max




s1 = input()
s2 = input()
ret = lcs(s1, s2)
print(ret)

#LCS 최장 공통 부분 수열 (Longest Common Subsequence)
"""
어떠한 문자 뒤에 공통적으로 같는 문자의 길이
두 문자열 중 공통 부분 수열 길이가 가장 길 때는?

        B   A   B   J   Y   P
    0   0   0   0   0   0   0   
A   0   0   1   1   1   1   1    
B   0   1   1   2   2   2   2  
P   0   1   1   2   2   2   3
A   0   1   2   2   2   2   3
B   0   1   2   3   3   3   3
Y   0   1   2   3   3   4   4

만약 비교하는 문자가 같다면 11시 방향 값 + 1
다르다면 위랑 좌측이랑 비교해서 max 값
"""

def lcs(s1, s2):
    len1, len2 = len(s1), len(s2)
    arr = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if s1[i - 1] == s2[j - 1]:
                arr[i][j] = arr[i - 1][j - 1] + 1

            else:
                arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])

    return arr[len1][len2]




s1 = input()
s2 = input()
ret = lcs(s1, s2)
print(ret)

# LIS 최장 증가 부분 수열  (Longest Increasing Subsequence)

"""
6
10 20 10 30 20 50

수열을 입력 받았을 때 증가되는 길이가 가장 길 때를 입력받으세요

기록 테이블을 1로 초기화
증가가 됐을 경우 비교대상에 적힌 값 + 1 vs 현재 적힌 값 비교해서 max값
"""

n = int(input()) # 정수의 개수
arr = list(map(int, input().split()))

result = [1] * n

for y in range(n):
    code = arr[y]   # 기준점
    for x in range(n):
        value = arr[x]  # 비교 대상
        if code > value:
            result[y] = max(result[x] + 1, result[y])

print(max(result))
