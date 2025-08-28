#기본함수
def greet(name):
    print(f"안녕하세요, {name}님!")
    
greet("민수")  # → 안녕하세요, 민수님!

#콜백함수 사용하기
def run_callback(callback):
    print("이제 콜백 함수를 실행할게요!")
    callback("영희")  # 여기서 콜백 함수가 실행됨

# greet 함수를 콜백으로 넘겨줌
run_callback(greet)
# greet는 내가 직접 호출하지 않았습니다.
# run_callback 함수가 대신 불러줬죠. 이게 바로 콜백 함수입니다.

def hello(name):
  #hello이라는 함수를 만들기
  # 매개변수인 name은 함수가 실행될 때 외부에서 전달되는 이름.
  print(f"안녕,{name}!")

hello("봄")
#여기까지는 기본 함수!!!!!!!!!!!!!

def call_function_with_name(callback,name):
   #call_function_with_name 함수는 두 가지를 받아요
   #callback: 실행할 "다른 함수"를 받을 이름을 정해줌.
   #name: 이름 데이터를 받음.
   # callback은 키워드 ❌, 그냥 매개변수 이름이다.
   callback(name)#전달받은 함수(callback)을 실행.
   #이 함수 안에서 callback(name)을 호출해서 콜백 함수로 전달된 hello가 실행돼요.
   #callback(name)의 의미는 callback이라는 함수에 name이라는 값을 전달해서 실행하라는 뜻.
   #예를 들어, callback에 hello이라는 함수가 전달되었다면, 이 줄은 hello(name)과 같아짐.
call_function_with_name(hello,"은지")


#콜백 마지막 실습
def dinner(name):
    print(f"{name}님은 저녁을 먹었습니다.")
#저녁을 먹는 함수 생성

def lunch(name):
    print(f"{name}님은 점심을 먹었습니다.")
#점심을 먹는 함수 생성

def eating_function(eat,name):
    eat(name)
#밥을 먹는 함수 생성 ( 콜백함수받는 부분을 eat으로 부를것임)
#즉 eat(name)은
#eating_function 함수를 호출할 때 디너를 호출했다면 dinner(name)이 되는것
#eating_function 함수를 호출할 때 런치를 호출했다면 lunch(name)가 되는것

eating_function(dinner,"은지")
eating_function(lunch,"현민")
    

