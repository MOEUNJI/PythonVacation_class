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
# i + 1 하면 1씩 더해져서 출력될 것
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

#2중 리스트
matrix = [
   [1, 3, 5],
   [6, 9, 12],
   [15, 18, 21]
]
multiples_of_three = [num for row in matrix for num in row if num % 3 == 0]
print(multiples_of_three)