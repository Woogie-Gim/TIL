# 문자열 / 리스트 관련 메소드
# 이해하고 넘어가면 안됨!!! 직접 타이핑 해보고
# 썼다 지웠다 하면서 익숙하게 만드는 작업 훈련

# 문자열 관련 메소드

st = 'apple,banana,mango'

# .find 내가 원하는 문자 또는 문자열이 몇 번 인덱스에 있는지 확인

index = st.find('a') # 0
# 쉽게 생각하면 for문 돌아서 앞에서 부터 찾기 시작
index = st.find('z') # -1
# 없는 문자열일 경우 -1을 출력

index = st.find('a', 1) #7
# 인덱스 1번부터 찾아라

# .find(찾을 문자/문자열, 시작index)

# 대소문자 확인

# .isupper 전부 대문자인지 판별
print(st.isupper()) #False

# .islower 전부 소문자인지 판별
print(st.islower()) #True

# .count('x') 문자열 내에 x 가 몇개인지
print(st.count('a'))

# join 합치기
# 리스트 안에 문자열 또는 문자를 하나의 문자열로 만들 때
# 구분자.join 을 이용해서 합치기

st = ['a', 'p', 'p', 'l', 'e']
str2 = "".join(st)
print(str2) #apple

# 공백없이 a / p / p / l / e 를 합쳐서 하나의 문자열로 만듦

st = ['apple', 'banana', 'mango']
str3 = ",".join(st)
print(str3) #apple,banana,mango

# 대문자 바꾸기
st = 'apple,banana,mango'
str2 = st.upper()
print(str2) #APPLE,BANANA,MANGO

# 소문자 바꾸기
st = input().lower().split() #소문자로 입력받기
print(st) #['apple,banana']

# 공백 지우기
st = ' apple'
str2 = st.lstrip() #왼쪽 공백 제거
print(st)
print(str2)

st = ' apple '
str2 = st.rstrip() # 오른쪽 공백 제거
str3 = st.strip() # 전체 공백 제거
print(str2)
print(str3) 

# lst = [1, 2, 3, 4] lst[0] = 100 가능
# st = 'apple' st[3] = 'z' 인덱스로 접근해서 변경 불가능

st = 'apple'
str2 = st.replace('ap', 'ma') #replace (바꿀 문자열, 바뀔 문자열)
print(str2)

# 리스트 관련 메소드

st = ['apple', 'banan', 'mango']
st.append('orange') # 리스트에 값 추가 -> append 항상 끝에 추가
print(st)

st.insert(1, 'orange') # 리스트 중간에 값 삽입
print(st) 

st = [1, 2, 3]
str2 = [4, 5]

st.extend(str2) # 리스트 확장 -> extend
print(st) #[1, 2, 3, 4 ,5]

st += str2 # st = st + str2
print(st) #[1, 2, 3, 4, 5, 4, 5]

st.pop() # 맨 뒤에 있는 마지막 원소 제거
print(st)

st.remove(4) # 제거 할 값을 인자값으로 넣기
# 제거 할 값 중 첫 번째로 발견된 값을 제거
print(st)

del st[3:] # 인덱스 3부터 끝까지 삭제
print(st)

del st[1]
print(st)

st = [1, 2, 3, 4, 5]
st.reverse() # 리스트 원소의 값 뒤집기
print(st)

# sort 정렬
a1 = [6, 3, 9]
print(a1)
a1.sort() # 오름차순 디폴트 reverse=False 가 생략되어 있음
print(a1)
a1.sort(reverse=True) # 내림 차순 출력
print(a1)

# a1 = 'asdf'
# a1.sort()
# print(a1) # 문자열은 인덱스로 접근 불가 / sort 불가

a1 = 'asdf'
a1 = sorted(a1)
a1 = ''.join(a1)
print(a1)

# sort와 sorted의 차이

ret = sorted(a1)
print(ret)

# sort는 리스트 원본 값의 위치를 변경
# sorted는 원본 데이터를 정렬하는 것이 아닌 정렬된 값을 반환
# sorted 된 값은 ret에 할당 되어 있다

lst = list(range(10))
print(lst)

ret1 = sorted(lst, key = lambda x:x) # 오름차순 / 매개변수 : return value
print(ret1)

ret2 = sorted(lst, key = lambda x:-x) # 내림차순 / return값이 0 -1 -2 ...
# 음수로 붙인 후 오름차순으로 정리하다 보니 내림차순으로 정렬됨
print(ret2)

ret3 = sorted(lst, key = lambda x:x, reverse=True) #정석 내림차순 정렬
print(ret3)

lst = [(3, 'banana'), (2, 'apple'), (1, 'carrot')]
ret = sorted(lst, key = lambda x:x[1], reverse=True)
print(ret)
# 인덱스 0 값이 같다면 다음 인덱스에 따라서 sort 한다