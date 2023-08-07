# 재귀 Recursion
# 함수 자기 자신을 계속 호출하는 함수
# 예시 주사위 던지기

"""
for i in range(1, 7):
    for j in range(1, 7):
        print(i, j)

주사위 개수가 늘어날 수록 시간복잡도는 느려진다

3중 4중 ....

주사위 개수를 입력받는다고 하면 for문의 개수를 설정하기엔 어렵다
"""

# 주사위 n개를 던져서 나오는 경우의 수를 재귀함수로 표현

n = int(input())

path = [0] * n

def abc(level):
    if level == n:
        for i in range(n):
            print(path[i], end= ' ')
        print()
        return
    for i in range(6):
        path[level] = i + 1
        abc(level + 1)
        # 함수 자기 자신을 호출하는
abc(0)

"""
main -> abc()
abc() -> abc()
abc() -> abc() .....

코드가 끝나지 않고 무한 반복

따라서 가장 먼저 해야할 일은 무한 호출을 막아야 한다

abc(0) -> abc(level) -> abc(level + 1)

if level == 2:
    return

abc(0)호출 -> abc(0) -> abc(1) -> return
return -> abc(1) / return 은 함수가 호출된 곳으로
"""

# 1 3 5 7 7 5 3 1

def abc(level):
    print(level)
    if level == 7:
        print(level)
        return
    abc(level + 2)
    print(level)

abc(1)

def abc(level):
    if level == 2:
        return
    abc(level + 1)
    abc(level + 1)

abc(0)


def abc(level):
    if level == 2:
        return

    for i in range(2):
        abc(level + 1)

abc(0)

# 12
def abc(level):
    if level == 2:
        return
    for i in range(2):
        print('#', end = '')
        abc(level + 1)
        print('#', end = '')

abc(0)

# 13
def abc(level):
    print('#', end='')
    if level == 2:
        return
    for i in range(2):
        abc(level + 1)
        print('#', end = '')

abc(0)

# 7
def abc(level):

    if level == 2:
        print('#', end='')
        return

    print('#', end='')
    for i in range(2):
        abc(level + 1)

abc(0)

# 110
def abc(level):

    if level == 2:
        return

    for i in range(2):
        abc(level + 1)

    print(level, end='')

abc(0)

def abc(level):
    print('#', end='')
    if level == 2:
        print('#', end='')
        return
    print('#', end='')

    for i in range(2):
        print('#', end='')
        abc(level + 1)
        print('#', end='')
    print('#', end='')

abc(0)