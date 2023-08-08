T = 10

for test_case in range(1, T + 1):
    N = int(input())
    arr = [(list(map(str, input()))) for i in range(8)]

    result = []
    for k in range(8):
        for l in range(8):
            if k + N > 8 or l + N > 8:
                continue
            ans = ''.join(arr[k][l : l + N])
            result.append(ans)
            ans2 = ''.join(arr[m][k] for m in range(l, l + N))
            result.append(ans2)

    for a in range(8 - N + 1, 8):
        for b in range(8):
            if b + N > 8:
                continue
            ans3 = ''.join(arr[m][a] for m in range(b, b + N))
            result.append(ans3)

    for r in range(8 - N + 1, 8):
        for c in range(8):
            if c + N > 8:
                continue
            ans4 = ''.join(arr[r][c : c + N])
            result.append(ans4)


    cnt = 0
    for a in result:
        if a == a[::-1]:
            cnt += 1

    print(f'#{test_case} {cnt}')
