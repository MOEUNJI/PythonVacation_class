'''
class 클래스명:
   클래스 변수
   생성자
   메서드


클래스 정의하기
   * 클래스 이름은 보통 대문자로 시작한다.
   * 클래스 내부에 메서드(함수)나 속성을 추가하여 동작을 정의한다.


속성 정의하기(__init__ 메서드)
   *__init__ 메서드는 객체가 생성될 때 자동으로 호출되는 생성자이다.
   * 생성자에서 객체의 초기상태(속성)을 설정한다.
   * self는 현재 생성되는 객체 자신을 가리키는 변수로, 클래스 내부 메서드에서
     항상 첫 매개변수로 전달된다.


행동 정의하기(메서드 추가)
   * 메서드는 클래스가 제공하는 기증(행동)을 정의한다.
   * 메서드도 항상 self를 첫 매개변수로 사용한다.
'''

class Person:
    def __init__(self,name,age,nationality):
        self.name = name
        self.age = age
        self.nationality = nationality

    def introduce(self):
        print(f"이름 : {self.name}, 나이 : {self.age}, 국적 : {self.nationality}.")

person1 = Person("모은지",20,"Korea")
person2 = Person("한현종",20,"USA")
person3 = Person("백현민",30,"japan")

# 속성과 메서드 사용
print(person1.name)  # 모은지
print(person1.age)   # 25
person1.introduce()  # 안녕하세요, 제 이름은 모은지이고, 25살입니다.
person2.introduce()
