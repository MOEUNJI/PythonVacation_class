str_banana = "banana"
set_banana = set(str_banana)
print(str_banana[0]) # 스트링은 b가 잘 출력되는데 !
# print(set_banana[0]) # 세트는 에러가 남!

str_banana = "banana" # 바나나 생성
set_banana = set(str_banana) #바나나를 세트로 변환
print(set_banana) #세트 출력해보면 n,a,b만 남은것을 볼 수 있음(중복제거)

list_banana = list(set_banana) #세트바나나를 리스트로 변환
tuple_banana = tuple(set_banana) #세트바나나를 튜플로 변환

print(list_banana) #['a', 'n', 'b']
print(tuple_banana[1]) #n
print(tuple_banana) #('a', 'n', 'b')


#마구잡이 알파벳에서 중복을 삭제하고 오름차순정렬
#1. 중복 삭제
str_random = "sdpflneklfcmsljiahnklsdmclslx" #마구잡이 알파벳 생성
str_random = set(str_random) #중복제거
print(str_random)


sorted_list_change = sorted(set(str_random))#이렇게 하면 원본이 바뀌지 않는 상태로 오름차순 + 중복제거됨
print(sorted_list_change)
print(str_random)#원본이 바뀌는 것은 아님


#마구잡이 알파벳에서 중복을 삭제하고 오름차순정렬
#1. 중복 삭제
str_random = "sdpflneklfcmsljiahnklsdmclslx" #마구잡이 알파벳 문자열 생성
str_random = set(str_random) #세트로 감싸서 중복제거(set 자료형으로 바뀜 )
print(str_random)


sorted_list_change = sorted(set(str_random))
#이렇게 하면 원본이 바뀌지 않는 상태로 오름차순 + 중복제거됨
#sorted()는 새로운 리스트를 반환하는 함수
print(sorted_list_change)
print(str_random)#원본이 바뀌는 것은 아님

set2 = {1,2,3}


# add()메서드를 통한 요소 추가
set2.update({4,3})


'''
요소 삭제하기
remove() : 특정 요소를 제거(요소가 없으면 오류 발생).
discard() : 특정 요소를 제거(요소가 없어도 오류 발생하지 않음).
pop() : 임의의 요소를 제거하고 반환(순서 없음).
clear() : 세트의 모든 요소를 제거
'''
set_c = {'a','s','d','f','g','h','j','k','l'}

set_c.remove("a")
print(set_c)
# set_c.remove("강아지")
# print(set_c)

# discard()메서드를 통한 요소 삭제
set_c.discard("고양이") # 없는 요소를 작성해도 오류나지 않음
print(set_c) # 뒤죽박죽 출력될것{'f', 's', 'h', 'k', 'j', 'l', 'd', 'g'}


# pop()메서드를 통한 요소 삭제
set_red = {'r','e','d'}
print(set_red) # 뒤죽박죽 출력될것{{'r', 'd','e'}

print(set_red.pop()) #삭제된 값 표시
print(set_red) #삭제하고 남은 세트 표시