def student(name, age, hobby):
    print(f"안녕하세요 저는 {name} 입니다. 나이는 {age}살 입니다.")
    print(f"취미는 {hobby}입니다.")
    
student("모은지",20,"프리다이빙")
student("홍길동",19,"러닝")
student("김도현",25,"쇼핑")

#정해진 아이디와 비밀번호
right_id = "moeunji"
right_pw = 1234

def login(id,pw):
    if right_id == id:
        if right_pw == pw:
            print("로그인 되었습니다.")
        else:  # 비밀번호가 일치하지 않는다면
            print("비밀번호가 일치하지 않습니다.")  # 출력
    else:  # 아이디가 일치하지 않는다면
        print("아이디가 일치하지 않습니다.")  # 출력

# 사용자로부터 아이디와 비밀번호 입력받기
user_id = input("아이디를 입력해주세요")
user_pw = int(input("비밀번호를 입력해주세요")) #숫자형으로 받아옴


login(user_id, user_pw)

