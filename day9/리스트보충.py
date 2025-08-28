'''
리스트 추가
append() : 리스트의 마지막에 새로운 요소를 추가한다.
insert() : 리스트의 중간에 새로운 요소를 삽입가능

리스트 삭제
remove() : 특정 값을 가진 요소를 삭제
pop() : 특정 위치에 있는 요소 삭제

리스트 정렬
sort(): 리스트를 오름차순으로 정렬(원본 리스트가 변경됨)
sort(reverse = True) : 리스트를 내림차순으로 정렬
sorted() : 정렬된 새로운 리스트를 반환(원본 리스트가 변경되지 않음)

리스트 반전
reverse() : 원본 리스트를 역순으로 변경

리스트 문자열
join() : 리스트 요소에 연결문자를 추가해 하나의 문자열로 결합
'''


append_nums = [1,2,3]
print(f"append() 추가 전 : {append_nums}")
append_nums.append(4)
print(f"append() 추가 후 : {append_nums}")

print()


# insert() : 리스트의 중간에 새로운 요소를 삽입가능
alphabets = ["a","b","c"]
print(f"insert()추가 전 : {alphabets}") #['a', 'b', 'c']
alphabets.insert(1,"M") # 인덱스 1번에 M추가
print(f"insert()추가 후 : {alphabets}") #['a', 'M', 'b', 'c']

#remove() : 괄호 안에 일치하는 값을 찾아 삭제
remove_nums = [1,2,3,4]
print(f"remove()삭제 전 : {remove_nums}") #[1, 2, 3, 4]
remove_nums.remove(1) # 없는 값 넣으면 에러남
print(f"remove()삭제 후 : {remove_nums}") #[2, 3, 4]

# pop() : 특정 위치에 있는 요소 삭제
colors = ["red","black","yellow","black"]
print(f"pop()삭제 전 : {colors}") # ['red', 'black', 'yellow', 'black']
colors.pop(3) #인덱스번호에 해당하는거 삭제
print(f"pop()삭제 후 : {colors}") #['red', 'black', 'yellow']

#reverse() - 역순
reverse_num = [2,4,6,8,10]
print(f"reverse()적용 전 : {reverse_num}") # [2, 4, 6, 8, 10]
reverse_num.reverse() #역순
print(f"reverse()적용 후 : {reverse_num}") # [10, 8, 6, 4, 2]

#join() - 연결
join_text = ["a","b","c"]
print(f"join(-)적용 전 : {join_text}") # ['a', 'b', 'c']
join_result = "-".join(join_text) #a, b, c를 -로 연결해 하나의 문자열 출력
print(f"join(-)적용 후 : {join_result}") # a-b-c (리스트가 문자열로 변환됨!)

#sort - 오름차순
sort_text = ['나','다','가','사','라']
print(f"sort적용 전 : {sort_text}")
sort_text.sort()
print(f"sort적용 후 : {sort_text}")


numbers = [3,7,8,6,10,4,2,5,0,1]
new_list = []
for num in numbers:
   if num > 5:
       new_list.append(num)
new_list.sort()
print(new_list)


words = ["사과", "바나나", "포도", "딸기", "망고", "바람", "바이올린"]
selected_words = []


for word in words:
   if "바" in word:  # "바"라는 글자가 포함된 단어 찾기
       selected_words.append(word)


print(f"선택된 단어들: {selected_words}")

text = "hello python"
print("hello" in text)   # True
print("java" in text)    # False


names = ["강자영", "이영희", "강민수", "박지훈", "강지영", "최수진"]
kim_family = []


for name in names:
   if name.startswith("강"):  # "강"으로 시작하는지 확인
       kim_family.append(name)


print(f"강씨 성을 가진 사람들: {kim_family}")


'''
새리스트 = [표현식 for 변수 in 반복할리스트 if 조건 ]


*표현식 : for문을 돌면서 새로운 리스트에 추가될 값을 결정
즉 리스트의 요소를 어떻게 변형할지 혹은 어떤 값을 넣을지 결정
1. 변수가 for문을 돌면서 리스트의 값을 가져온다.
2. if문으로 특정 조건을 만족하는 값만 선택할 수 있듬
'''
number = []
for i in range(1,11):
   number.append(i)
print(number)

#컴프리헨션으로 바꿔보면?
number = [i for i in range(1,11)]
# for문을 돌면서 i의 값을 변형 없이 그대로 표현하겠다는 것!
print(number)

#조건을 넣을수도 있음
even_numbers = [i for i in range(1,11) if i % 2 == 0]
print(even_numbers)

#else 조건을 넣을 수도 있음
result = []
for i in range(1,6):
   if i % 2 == 0:
       result.append("짝수")
   else:
       result.append("홀수")
print(result)
# 📌 컴프리헨션을 사용하면?
result2 = ["짝수" if i % 2 == 0 else "홀수" for i in range(1,6)]
print(result2)
#파이썬 **리스트 컴프리헨션(list comprehension)**에서 if/else를 같이 쓰는 경우와
# if만 쓰는 경우의 위치가 달라집니다.

#2중 리스트
list_in_list = [
   [1, 3, 5],
   [6, 9, 12],
   [15, 18, 21]
]

list_in_list_of_three = []

for row in list_in_list:        # 2차원 리스트에서 각 행(row)을 꺼내옴
    for num in row:             # 그 행에서 숫자(num)를 하나씩 꺼냄
        if num % 3 == 0:        # 그 숫자가 3으로 나누어 떨어지면
            list_in_list_of_three.append(num)  # 결과 리스트에 추가

print(list_in_list_of_three)

#인덱스에 접근하는 방법은 2가지가 있다. for문을 사용해서 접근하거나 [][]로 접근할 수 있는데
# 만약 우리가 1행에 있는 3에 접근하고 싶다면 [0][1] 이렇게 접근하면 된다.

print(list_in_list[0][1])

# 만약 3,9,18 이라는 각 행의 같은 인덱스에 접근하고 싶다면?
for row_two in list_in_list:
    print(row_two[1])
    print(row_two)
#이렇게 접근할 수 있다.
#여기서 row_two 는 반복문이 돌 때마다 list_in_list의 원소 하나씩을 담아요.
#첫 번째 반복 → row_two = [1, 3, 5]
#두 번째 반복 →row_two = [6, 9, 12]
#즉, 이미 작은 리스트 하나를 가리키고 있기 때문에,
# 그 안에서 번호를 뽑으려면 **인덱스 하나 [0]만 쓰면 돼요.

#예를들면 직접 인덱스 : "큰 상자(list_in_list)에서 [1]번째 작은 상자 꺼내고 → 작은 상자 안에서 [0]번째 물건 꺼내기"
#반복문 : "반복문이 작은 상자를 하나씩 꺼내서 row_two에 주니까, 작은 상자 안에서 바로 [0]번째 물건 꺼내면 됨"
# 인덱스 2개: 큰 리스트 → 작은 리스트 → 값 (직접 꺼낼 때)
# 인덱스 1개: 작은 리스트만 보고 있을 때 (반복문에서 꺼낼 때)

#위의 2중 리스트를 컴프리헨션으로 변경하여 3의 배수를 출력해보기
list_in_list_of_three2 = [num for row in list_in_list for num in row if num % 3 == 0]
print(list_in_list_of_three2)
#for row in list_in_list : 행 단위로 꺼내오기
# for num in row : 행 안에서 숫자 하나씩 꺼내오기
#if num % 3 == 0 → 3의 배수만 필터링
