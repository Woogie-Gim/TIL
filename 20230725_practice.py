# set - 중복을 허용하지 않는
s = {1, 2, 3, 4, 5}

# 값 추가
s.add(6)
print(s) #{1, 2, 3, 4, 5, 6}
s.update([11, 12, 13, 14])
print(s) #{1, 2, 3, 4, 5, 6, 11, 12, 13, 14}

# 값 삭제

s1 = {1, 2, 3, 4, 5, 6}
s1.remove(6)
print(s1) #{1, 2, 3, 4, 5}
#s.remove(6666) #KeyError: 6666

# 키 에러 없이 값을 제거 하고 싶다. discard
s1.discard(2)
print(s1) #{1, 3, 4, 5}
s1.discard(2222)
print(s1) # 키 에러 발생 안함

# 집합

s1 = [1, 2, 3, 4]
s2 = [2, 4, 6, 8]

s1, s2 = set(s1), set(s2)

# 교집합
print(s1 & s2) # {2, 4} # & -> 엠퍼센드 and 연산자를 의미
s3 = s1 & s2
print(s3)
s4 = list(s3)
print(s4) # [2, 4]

# 합집합
print(s1 | s2) #{1, 2, 3, 4, 6, 8}

# 차집합
print(s1 - s2) # {1, 3}

# dictionary - 내부적으로 hash 라는 자료구조를 이용해서 만들어 놓은 자료형 입니다
# 파이썬에서만 쓰임

st = {'kevin' : 1, 'john' : 2, 'bob' : 3}

#키와 밸류를 딕셔너리에 추가
st['kate'] = 4 #{'kevin': 1, 'john': 2, 'bob': 3, 'kate': 4}
print(st)

# 키와 벨류를 딕셔너리에서 삭제
del st['kate']
print(st) #{'kevin': 1, 'john': 2, 'bob': 3}

# 딕셔너리에서 key만 따로 빼오기
lst = st.keys()
print(lst) # dict_keys(['kevin', 'john', 'bob'])
print(list(lst)) #['kevin', 'john', 'bob']

# 밸류만 따로 빼오기
lst = st.values()
print(lst) #dict_values([1, 2, 3])
print(list(lst)) #[1, 2, 3]

# 딕셔너리에서 keyd와 value를 빼오기
lst = st.items()
print(lst) # dict_items([('kevin', 1), ('john', 2), ('bob', 3)])
print(list(lst)) # [('kevin', 1), ('john', 2), ('bob', 3)] 튜플로 묶임

st = {'kevin' : 1, 'john' : 2, 'bob' : 3}

# 값 출력
print(st['kevin']) # 1

# print(st['kevinnnnnnnn']) # 없는 키의 값 출력 시 KeyError: 'kevinnnnnnnn'

# key error 없이 출력을 할 때 -> get() 사용
print(st.get('kevin')) # 1
print(st.get('kevinnnnnnnnn')) # None
print(st.get('kevinnnnnnnnn', '없는 key 값 입니다')) #없는 key 값 입니다

# 딕셔너리 삭제 (del, pop)

st = {'kevin' : 1, 'john' : 2, 'bob' : 3}

st.pop('kevin')
print(st) # {'john': 2, 'bob': 3}
st.pop('kevinnnnnnnnnnnnnn', -1) # pop함수 사용해서 삭제할 때 없는 키의 값을 삭제 시
print(st)                        # default parameter를 넣으면 key error 발생 방지할 수 있음

# 라이브 내용은 없지만
# 알면 도움이 될만한 클래스를 하나 소개
# counter 라는 클래스 사용법

from collections import Counter
lst = ['apple', 'mango', 'banana', 'apple', 'banana', 'mango', 'apple']

# counter 클래스는 중복된 데이터가 각각 몇개씩 있는지 알려주는 클래스
print(Counter(lst)) #Counter({'apple': 3, 'mango': 2, 'banana': 2})

ret = dict(Counter(lst))

print(ret) #{'apple': 3, 'mango': 2, 'banana': 2}

#  문자열 중에서 가장 많이 사용된 알파벳이 무엇인지 알고 싶을 때 사용 가능
st = 'an applemango'
print(Counter(st)) #Counter({'a': 3, 'n': 2, 'p': 2, ' ': 1, 'l': 1, 'e': 1, 'm': 1, 'g': 1, 'o': 1})
ret = dict(Counter(st))
print(ret) #{'a': 3, 'n': 2, ' ': 1, 'p': 2, 'l': 1, 'e': 1, 'm': 1, 'g': 1, 'o': 1}

# 가장 많이 사용된 알파벳을 출력하시오
# sort 연습 후 가장 많이 사용된 알파벳 출력
ret = sorted(ret.items(), key = lambda x : x[1], reverse = True)
# items를 사용하면 key와 value를 튜플로 반환하는데
# x[1] -> 즉, 알파벳 별로 사용된 개수를 기준으로 sort됨
# reverse = True 를  통해서 내림차순으로 정렬

print(ret) # [('a', 3), ('n', 2), ('p', 2), (' ', 1), ('l', 1), ('e', 1), ('m', 1), ('g', 1), ('o', 1)]
print(ret[0][0]) # a -> 가장 많이 존재하는 알파벳 출력해보기!


# 알면 좋은 방법 (가장 많이 사용된 문자 출력하기 예시) -> Counter 라는 클래스 안에
# mostcommon 이라는 메서드가 있어서 그것을 이용하는 예시를 보겠습니다

st = 'an applemango'
ret = Counter(st).most_common(1) # 1은 1등을 말함 (최빈수)
print(ret) # [('a', 3)]
print(ret[0][0]) # a

# 추가적으로 counter 클래스를 사용하면 문자열의 덧셈과 뺄셈도 가능
# 예시
a = Counter('apple')
b = Counter('mango')

print(a + b) # Counter({'a': 2, 'p': 2, 'l': 1, 'e': 1, 'm': 1, 'n': 1, 'g': 1, 'o': 1})
# a 문자열에서 사용된 알파벳 개수 + b 문자열에서 사용된 알파벳 개수
print(a - b) # Counter({'p': 2, 'l': 1, 'e': 1})
# a문자열에서 b문자열에서 사용된 알파벳을 뺀 후, 사용된 알파벳 개수도 확인 가능

# 추가적으로 copy는 매우 중요