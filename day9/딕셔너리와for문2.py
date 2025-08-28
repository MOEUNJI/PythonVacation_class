fruit_colors = {
   "Red" : "apple",
   "Yellow" : "banana",
   "Purple" : "blueberry"
}

#키값을 출력해주세요(문제)
print(fruit_colors.keys())

for i in fruit_colors.keys():
   print(i)
# i라는 변수를 선언하고 i는 fruit_color의 key값을 반복한다.
sport_star = {
   "축구" : "손흥민",
   "피겨" : "김연아",
   "수영" : "박태환",
   "펜싱" : "박상영"
}
#for문으로 keys출력
for j in sport_star.keys():
   print(j)


#sport_star.keys()를 리스트화 하기
sport_list = list(sport_star.keys())
print(sport_list) #['축구', '피겨', '수영', '펜싱']


# 리스트화 되었다면 리스트메서드를 사용할 수 있을것이다!
# 리스트 맨 마지막에 리스트 메서드를 사용해서 농구 추가하기
sport_list.append("농구")
print(sport_list)

#값을 출력하여
for v in sport_star.values():
    print(v)
#리스트화 한 후
sport_values = list(sport_star.values())
print(sport_values)   # ['손흥민', '김연아', '박태환', '박상영']
#이상화를 추가하고 손흥민을 구자철로 변경
sport_values.append("이상화")
print(sport_values)   # ['손흥민', '김연아', '박태환', '박상영', '이상화']

sport_star["축구"] = "구자철"
print(sport_star)
#이상화가 안 나올것이다. 리스트를 수정한 것이기 때문이다.

sport_star["스케이트"] = "이상화"
print(sport_star)
#이렇게 직접 추가해주어야 딕셔너리 변경이 가능하다.