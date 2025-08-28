'''
1. keys() : 딕셔너리의 모든 key값들을 모아 리스트와 유사한 형태로 반환
2. values() : 딕셔너리의 모든 값을 반환
3. items() : 딕셔너리의 모든 키(key)와 값(value) 쌍을 반환합니다.
4. update(other_dict) : 딕셔너리에 다른 딕셔너리의 키-값 쌍을 추가하거나 덮어씁니다.
'''



my_dict = {
   "name" : "kelly",
   "age" : 20,
   "city" : "New York"
}

keys = my_dict.keys() #my_dict의 모든 키들을 뽑아서 리스트처럼 보이게 만들어줌
print(keys)  # 결과: dict_keys(['name', 'age', 'city'])
print()
#my_dict.keys() 를 하면 진짜 리스트가 아니라 dict_keys 객체라는 특별한 타입을 반환합니다.
# 그래서 print(keys) 했을 때 dict_keys(['name', 'age', 'city']) 처럼 보이는 거예요.
#진짜 리스트가 필요하다면 list()로 감싸주면 됩니다.

lists = list(my_dict.keys()) #my_dict의 모든 키들을 리스트화
print(lists)  # 결과: ['name', 'age', 'city']
print()

print("values()")
values = my_dict.values()
print(values)  # 결과: dict_values(['kelly', 25, 'New York'])
print()
#이것도 real list로 바꾸고 싶다면?
values_list = list(my_dict.values()) #my_dict의 모든 키들을 리스트화
print(values_list)  # 결과: ['name', 'age', 'city']
print()

print("items()")
items = my_dict.items()
print(items)
# 결과: dict_items([('name', 'Alice'), ('age''New York')])
print()

items_list = list(my_dict.items()) #my_dict의 모든 키들을 리스트화
print(items_list)  #[('name', 'kelly'), ('age', 20), ('city', 'New York')]
print()

print("update()")
my_dict.update({"age":26,"hobby":"freediving"})
print(my_dict)
print()

#딕셔너리 키 기준 오름차순
print(sorted(my_dict))
#딕셔너리의 키들을 알파벳 순으로 내림차순 정렬한 리스트입니다

print(sorted(my_dict,reverse=True)) #['name', 'hobby', 'city', 'age']
#파이썬의 딕셔너리(dict) 에는 .sort() 메서드가 없습니다.
# 왜냐하면 .sort() 는 리스트(list) 전용 메서드예요.
#대신, sorted() 함수를 써서 정렬된 새로운 리스트를 반환하는 방식으로 다루게 됩니다.
#기본은 오름차순(작은 → 큰)인데,
# reverse=True 를 쓰면 내림차순(큰 → 작은) 으로 정렬됩니다.


