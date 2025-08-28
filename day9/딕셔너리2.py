me = {
  "name" : "MoEunJi", # key : value
  "age" : 20, # 숫자나 불리언 값은 따옴표 없이 사용 가능
  "phone" : "010-1234-5678",
  "class" : ["c언어", "python","java"] # 값을 리스트로도 가질 수 있다
}




my_phone = {
   "name" : "아이폰16",
   "color" : "white",
   "storage" : "256GB"
}
print(me)

print(my_phone["color"]) #white
print(me["class"]) #['c언어', 'python', 'java']
#딕셔너리 이름 [키]
#대괄호 안에 키를 입력하면 벨류값이 나옴

friends = {}

#딕셔너리에 정보 추가하기
friends["도현"] = 19
friends["소민"] = 27
print(friends)
print(friends["소민"])

#소민이의 나이를 25살로 수정하기
friends["소민"] = 25
print(friends["소민"])

#딕셔너리에서 소민 삭제
del friends["소민"]
print(friends)

#딕셔너리 초기화
friends.clear()
print(friends)