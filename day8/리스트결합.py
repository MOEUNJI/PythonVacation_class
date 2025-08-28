'''
1. +연산자 : 두 개 이상의 리스트를 직접 연결하여 새로운 리스트를 생성한다.
2. extend() : 기존 리스트의 끝에 다른 리스트의 모든 요소를 추가함
'''

list1 = ["a","b","c"]
list2 = ["d","e"]

# +연산자를 이용한 리스트 결합(새로운 리스트 생성)
list3 = list1 + list2
print(list3)


#extend() : 기존 리스트에 추가
list1.extend(list2)
print(list1)

print("곱하기")
list4 = list2 * 3
print(list4) #['d', 'e', 'd', 'e', 'd', 'e']

print("리스트 길이")
result = len(list4)
print(result) #6

print("리스트에서 특정 값이 있는지 확인 (in 연산자)")
print('d' in list4) #True

print("리스트에서 특정 값의 개수 구하기 (count())")
result2 = list4.count('e')
print(result2) #3

print("리스트의 최대값, 최소값 구하기 (max(), min())")
list5 = [1,2,3,4,5]
print(max(list5)) #5
print(min(list5)) #1