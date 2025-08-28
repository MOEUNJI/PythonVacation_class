'''
num = 7 #우리가 일반적으로 사용하던 변수
nums = [0,1,2,3] #여러개의 데이터를 묶은 리스트
'''

numbers = [0,1,2,3] #숫자리스트
alphabets = ['a','b','c'] #문자리스트
bools_type = [True,True,True] #논리값 리스트
greetings = ["hello","오늘은 파이썬","9일째"] #문자열리스트

mixed_list = [1, "apple", 3.14, True] #숫자, 문자, 논리값 혼합리스트
print(mixed_list)
'''
1 = 정수형(int)
2 = "apple": 문자열(str)
3 = 3.14: 실수형(float)
4 = True: 불리언(bool)
'''

print(mixed_list[1])#추가!!!!!!!!!!
mixed_list[1] = "mango"
print(mixed_list)

family = ["mother","father","sister","dog"]
print(family[-1]) # 뒤에서부터 출력 ( dog 출력 )
print(family[-4])

'''
list[start:end:step]


start: 슬라이싱이 시작되는 인덱스 (포함)
end: 슬라이싱이 끝나는 인덱스 (포함되지 않음)
step: 요소를 건너뛰는 간격 (기본값은 1)
'''

numbers = [10,20,30,40,50]
# 첫 번째부터 세 번째 요소까지 추출(마지막 요소는 출력되지 않음)
print(numbers[0:3])  # [10, 20, 30]

# 두 번째부터 네 번째 요소까지 추출(마지막 요소는 출력되지 않음)
print(numbers[1:4])  # [20, 30, 40]

# 뒤에서 두 번째 요소부터 마지막 요소까지
print(numbers[-2:])  # [40, 50]

# 첫 번째부터 뒤에서 두 번째 요소까지
print(numbers[:-2])  # [10, 20, 30]

# 한 요소씩 건너뛰기
print(numbers[::2])  # [10, 30, 50]
# 역순으로 추출
print(numbers[::-1])  # [50, 40, 30, 20, 10]

# 첫 두 요소를 100, 200으로 변경
numbers[:2] = [100, 200]
print(numbers)  # [100, 200, 30, 40, 50]

# 첫 두 요소 삭제
numbers[:2] = []
print(numbers)  # [30, 40, 50]



