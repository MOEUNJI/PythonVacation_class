list_in_list = [1, [2, 3], "hello", [True, False]]
print(list_in_list)
print(list_in_list[1][1])#추가!!!!!!!!!!!!!!!1

#중첩 list만들기
python_class = [
   ["철수", "영희", "민수"],  # 1조
   ["지수", "현우", "나영"],  # 2조
   ["동현", "수진", "호영"]   # 3조
]

#1조를 출력하고싶다면?
print(python_class[0])


#2조를 출력하고싶다면?
print(python_class[1])


#3조를 출력하고싶다면?
print(python_class[2])

#3조에 있는 수진이를 출력하고 싶다면?
print(python_class[2][1])


#그럼 민수를 출력해볼까요?
print(python_class[0][2])

#지수가 이름을 로제로 개명했다!
python_class[1][0] = "로제"
print(python_class[1]) # 2조 출력

colors = ["red","orange","green","yello"]
for color_for in colors:
   print(color_for, end=" ")


python_class = [
  ["철수", "영희", "민수"],  # 1조
  ["지수", "현우", "나영"],  # 2조
  ["동현", "수진", "호영"]   # 3조
]
for python_class_for in python_class:
   for student in python_class_for:
       print(student)

