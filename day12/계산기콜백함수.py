#함수선언
def calculator(x,y, operation):#calculator는 계산기를 작동시키는 틀이에요.
    # x: 첫 번째 숫자 (예: 2)
    # y: 두 번째 숫자 (예: 3)
    # operation: 계산 방법 (덧셈, 뺄셈, 곱셈, 나눗셈 중 하나)
    return operation(x, y)
    # 여기서 operation은 나중에 덧셈, 뺄셈, 곱셈, 나눗셈 중 하나의 함수가 들어와요.


'''
러면 operation(x, y)는 이렇게 동작해요:

만약 operation이 plus라면 → plus(x, y)를 실행.
만약 operation이 minus라면 → minus(x, y)를 실행.
'''

def plus(x,y): # 더하기 operation 함수 생성
   return x+y

def minus(x,y): # 마이너스 operation 함수 생성
   return x-y

def multiple(x,y): # 곱하기 operation 함수 생성
   return x*y

def divide(x,y): # 나누기 operation 함수 생성
   return x//y

#함수호출
plus_result = calculator(2,3,plus) # calculator호출 매개변수 2,3 연산자는 plus함수
minus_result = calculator(2,3,minus) # calculator호출 매개변수 2,3 연산자는 minus함수
multiple_result = calculator(2,3,multiple) # calculator호출 매개변수 2,3 연산자는 multiple함수
divide_result = calculator(9,3,divide) # calculator호출 매개변수 2,3 연산자는 divide함수

#출력
print(plus_result)
print(minus_result)
print(multiple_result)
print(divide_result)
