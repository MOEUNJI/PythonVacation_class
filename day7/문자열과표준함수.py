print("안녕하세요")
print('python')
print("12345")
print("Hello World")

text = "안녕하세용가리~"
print(text[0])
print(text[-1])

# text[0] = "언"

'''
대소문자 변환
1. upper(어퍼) - 대문자로 변환
2. lower(로월) -  소문자로 변환
3. capitalize(캐피털라이즈) - 첫 글자만 대문자로 변환


문자열찾기
1. fine() - 특정 글자가 어디에 있는지 찾기
2. count() - 특정 글자가 몇번 등장하는지 세기


문자열 변경하기
1. replace() - 특정 글자를 다른 글자로 바꾸기


문자열 나누고 합치기
1. split() - 특정 기준으로 문자열 나누기 ( 리스트로 변환 )
2. join() - 리스트를 문자열로 합치기


공백 제거하기
1. strip() - 양쪽 공백 제거 ( day2- 문자열 실슴 완 )
2. lstrip() - 왼쪽 공백 제거
3. rstrip() - 오른쪽 공백 제거


문자열이 특정 조건을 만족하는지 확인하기
1. startswith(스타트스위치) - 특정 문자로 시작하는지 확인
2. endswith() - 특정 문자로 끝나는지 확인
3. isdigit(이즈디짓) - 숫자로만 이루어졌는지 확인
4. isalpha(이즈알파) - 알파벳으로만 이루어졌는지 확인


문자열 길이 구하기
len() - 문자열 길이(글자 개수) 구하기
'''

hello = "hello"
print(hello.upper())

python = "PYTHON"
print(python.lower())

money = "money"
print(money.capitalize())

find_text = "fine text"
print(find_text.find("text")) # 5 ( 5번째 인덱스 )
print(text.find("java"))    # -1 (없으면 -1)

#count() - 특정 글자가 몇 번 등장하는지 세기
banana = "banana"
print(banana.count("a"))  # 3

replace_text = "I like dog"
print(replace_text.replace("dog", "cat"))  # I like cat

#split() - 특정 기준으로 문자열 나누기 (리스트로 변환)
split_text = "apple,banana,grape"
print(split_text.split(","))  # ['apple', 'banana', 'grape']

# join() - 리스트를 문자열로 합치기
words = ['apple', 'banana', 'grape']
print(",".join(words))  # apple, banana, grape

# startswith() - 특정 문자로 시작하는지 확인
swith_text = "start swith"
print(swith_text.startswith("start"))  # True
print(swith_text.startswith("swith"))  # False

# endswith() - 특정 문자로 끝나는지 확인
print(swith_text.endswith("start"))  # False
print(swith_text.endswith("swith"))  # True

# isdigit(이즈디짓) - 숫자로만 이루어졌는지 확인
isdinit_text = "12345"
print(isdinit_text.isdigit())  # True

isdinit_text = "123abc"
print(isdinit_text.isdigit())  # False

# isalpha() - 알파벳으로만 이루어졌는지 확인
isalpha_text = "Python"
print(isalpha_text.isalpha())  # True

isalpha_text = "Python3"
print(isalpha_text.isalpha())  # False (숫자가 포함되어 있음)

# len() - 문자열 길이(글자 개수) 구하기
len_text = "eunji"
print(len(len_text))  # 5