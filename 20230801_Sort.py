# 정렬

# Sort
# Sorted

# 정렬 관련된 알고리즘

# 선택 정렬 selection sort
# 삽입 정렬 insert sort
# 버블 정렬 bubble sort

# 3가지 정렬 모두 시간 복잡도 O(n ** 2)
# 장점 : 쉽다, 단점 : 느리다

# counting sort - O(n)

arr = [4, 7, 1, 3, 5, 2]
# 선택정렬으로 오름차순 정리
# 4 <- 기준점 y / 비교대상 x
# 비교대상이 기준점보다 작을 경우 스왑
# 1 7 4 3 5 2 첫번째 정렬

# 1 4 7 3 5 2
# 1 3 7 4 5 2
# 1 2 7 4 5 3 두번째 정렬

# 1 2 4 7 5 3
# 1 2 3 7 5 4 세번째 정렬

# 1 2 3 5 7 4
# 1 2 3 4 7 5 네번째 정렬

# 1 2 3 4 5 7

# 기준점은 0번 인덱스 부터 리스트 길이보다 1 작은 수

for y in range(len(arr) - 1):
    for x in range(y+1, len(arr)):
        if arr[y] > arr[x]:
            arr[y], arr[x] = arr[x], arr[y]

print(arr)

# 삽입 정렬 insert sort
# 장점 : 쉽다, 단점 : 느리다, 특징 : 이미 정렬된 데이터에서 새로 추가된 데이터를 정렬하기 좋음

# 삽입정렬로 오름차순 정리

arr = [4, 7, 1, 3, 5]
# 새로운 배열에 하나씩 내려서 내릴 때 마다 비교해서 스왑해줌

result = [0] * 5

for i in range(5):
    result[i] = arr[i]
    for j in range(i, -1, -1):
        if result[j-1] > result[j]:
            result[j-1], result[j] = result[j], result[j-1]
        else:
            break

print(result)

# 버블 정렬 Bubble sort
# 앞에서 부터 뒤를 비교하면서 계속해서 스왑

a = [8, 3, 12 ,10, 1]

for i in range(len(a)-1, 0, -1): # 4 3 2 1
    for j in range(0, i): # i가 4일 때 j = 0, 1, 2, 3 # i가 3일 때 0, 1, 2...
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)



