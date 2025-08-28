'''
보통의 함수 작성 방법
def 함수이름(매개변수):
   return 결과


============================
람다함수 작성 방법
   lambda 매개변수:return값
람다함수 특징
   이름이 없어서 익명함수라고도 불림
   한 줄로 작성
'''


#두 숫자를 더하는 일반 함수 생성
def add(x, y):
   return x + y
print(add(5,1))


#람다함수로 더하기 함수 생성
lambda_add = lambda x,y: x+y
print(lambda_add(5,5))

#list, range를 사용해서 lambda함수로 1~20 사이의 짝수만 골라 리스트로 출력합니다.)
numbers = list(range(1,21))
#range는 연속된 숫자를 출력하는 함수로 여기서는 20까지 출력한다.
#list로 감싸주어서 20개가 들어있는 리스트 객체로 만든다
# 예를들면 range(20) → [0, 1, 2, 3, ..., 19]


even_numbers = list(filter(lambda x : x % 2 == 0,numbers))
print(even_numbers)
#filter(함수, iterable 이터러블) : 는 조건에 맞는 요소만 걸러주는 함수
#함수: 조건을 만족하면 True, 아니면 False를 반환.
#iterable: 검사할 데이터(리스트, 튜플 등).
# 람다함수는 filter에 전달될 검사받을 함수이다.

#lambda x : x % 2 == 0
#x - > 매개변수
#x % 2 == 0 -> 리턴값
# 람다 함수(익명 함수). x를 받아서 x % 2 == 0(짝수 검사)의 True/False를 반환.

#numbers : filter 함수가 “어떤 데이터를 대상으로 검사할지”를 알려주는 역할이에요.

#리스트로 감싸는 이유
# filter()는 **리스트가 아니라 “이터레이터(iterator)”**를 돌려줍니다.
# 이터레이터는 “필요할 때 하나씩 꺼내 쓸 수 있는 값의 흐름”이지, 리스트처럼 한눈에 모여있는 자료가 아니에요.
#예를 들면 비슷한것으로는 for문의 i의 역할정도라고 생각하면 된다.
#그래서 리스트로 눈으로 확인하려고 한 번 더 리스트로 감싼 것이다.




