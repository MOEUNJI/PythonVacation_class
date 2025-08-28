'''
class 예외클래스명(Exception)
   def __init__(self):
       super().__init__("예외메시지):
'''


class AgeError(Exception):
    # 부모클래스가 없는데 왜 super를 쓸까?
    #AgeError는 그냥 새로운 클래스가 아니라, **기존의 Exception 클래스를 상속한 "자식 클래스"**예요.
   def __init__(self):
       super().__init__("사람의 나이는 0살 이상, 150 미만으로 작성할것")
        #super의 생성자를 호출하는 것


try:
   age = int(input("나이를 입력하세요:"))


   if(age < 0 or age > 150): #입력값이 0보다 작거나150보다 크다면
       raise AgeError #예외를 발생시킨다.
except AgeError as e: #예외 발생시 AgeErr에 정의된 메시지를 출력한다.
   print(e)
else:
   print(f"당신은 {age}살 이군요!")
finally:
   print("프로그램을 종료함")