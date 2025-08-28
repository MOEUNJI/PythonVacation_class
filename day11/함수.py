'''
함수의 장점
1. 반복적인 코드 제거 및 재사용성 향상
2. 코드의 가독성 및 유지보수 향상
3. 오류추적 및 디버깅 용이


def 함수이름():
  코드1
  코드2
  코드3


'''


def hello():
   print("안녕하세요")
   print("저는 안나입니다. ")
   print("엘사 동생이에요")

hello()


animals = ["강아지","고양이","햄스터","곰","기린"]
index = 0
def change_animal():
    global index
    if index >= len(animals):
        index = 0
        # 만약 index가 5보다 크거나 같아지면, 리스트의 끝을 넘어가므로 다시 처음 색상(index = 0)으로 돌아갑니다.
    print(f"동물을{animals[index]}로 변경합니다.")
    index += 1

change_animal()
change_animal()
change_animal()
change_animal()
change_animal()
change_animal()


#솜사탕 함수 선언
def candy_fluff(count): #캔디플러프
   print("오늘은 솜사탕을 "+ str(count) +"개 만들어야 합니다.")
#솜사탕함수 호출
candy_fluff(15)


#함수선언
def hello(name):
  print(f"안녕하세요 제 이름은 {name}입니다.")


# 호출
hello("제니")  # 안녕하세요 제 이름은 제니  입니다.
hello("지수")  # 안녕하세요 제 이름은 지수  입니다.


#함수선언
def plus(a,b):
   print(a+b)


plus(10,20) #30
plus(5,20) #25
plus(3,50) #53


def triangle_area(base, height):
    area = (base * height) / 2
    print(f"넓이 = {area}")

# 실행 예시
triangle_area(base=10, height=5)   # 👉 넓이 = 25.0
triangle_area(height=7, base=8)    # 👉 넓이 = 28.0



def triangle_area(base, height):
    area = (base * height) / 2
    print(f"넓이 = {area}")

# 실행 예시
triangle_area(base=10, height=5)   # 👉 넓이 = 25.0
triangle_area(height=7, base=8)    # 👉 넓이 = 28.0



# ---------------------------
# 실행 부분
# ---------------------------

#patients 페이션츠
patients = []  # 빈 리스트 준비
n = int(input("몇 명의 환자를 등록하시겠습니까? : "))

for i in range(n):
    name = input(f"{i+1}번째 환자 이름: ")
    temp = float(input(f"{i+1}번째 환자 체온(℃): "))
    patients.append((name, temp))
    # (이름, 체온) 튜플 형태로 받아 patients의 리스트에 추가해줌
    #리스트 안에는 어떤 자료형이든 들어갈 수 있음


#체크 페이션츠
def check_patients(patients_list,fever=37.5):
    #fever_temp=37.5 → 함수를 호출할 때 따로 발열 기준을 주지 않으면 자동으로 37.5를 기준으로 사용.
    # 필요하면 호출할 때 값을 새로 줄 수 있음.
    print("🏥 환자 발열 검사 결과 🏥")
    for user, fever_check in patients_list:
        # 튜플로 넣어준 2개를 순서대로 네임과 템프로 받아올거임
        # 변수 이름이 같아야 맞는 게 아니라
        #👉 순서(첫 번째, 두 번째 값)에 맞게 들어가는 거예요.
        if fever_check >= fever:
            print(f"{user} : {fever_check}℃ ⚠️ 발열 환자")
        elif fever_check <= 36.0:
            print(f"{user} : {fever_check}℃ ❄️ 저체온증 환자")
        else:
            print(f"{user} : {fever_check}℃ 정상")


check_patients(patients)  # 함수 호출ㅜ


def greet(name,greeting="안녕하세요"):
    print(f"{greeting},{name}!")


greet("철수")
greet("영희","반가워요")