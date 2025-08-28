#영어사전 딕셔너리 생성
english_dict = {
   "flower" : "꽃",
   "food" : "음식",
   "floor" : "바닥",
   "sky" : "하늘",
}

#사용자로부터 영어단어 입력받기
user_word = input("영어 단어를 입력하세요:")

#사용자가 입력한 단어가 english_dict에 있는지 확인.
if user_word in english_dict:
   print(f"{user_word} : {english_dict[user_word]}")
else:
   print(f"{user_word}는 사전에 없습니다.")
   add_value = input("단어의 뜻을 입력하세요:")
   english_dict[user_word] = add_value
   # english_dict딕셔너리에 user_word로 입력받은 값을 키로 추가하고 add_value에 들어있는 뜻으로 저장
   # 즉 유저가 book을 검색했다면 키는 book이 되고,
   # 뜻을 책이라고 입력했다면 값은 책이 된다.
   print(f"{user_word} : {english_dict[user_word]}(사전에 추가되었습니다!)")
