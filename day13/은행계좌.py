'''
BankAccount는 “은행 계좌”라는 개념을 코드로 만든 틀(클래스) 입니다.
이 틀로 만든 실제 물건(객체/인스턴스)이 계좌주(owner) 와 잔액(balance) 을 가지고 있고,
돈을 넣는 deposit, 돈을 빼는 withdraw, 잔액을 확인하는 check_balance
같은 행동(메서드) 을 할 수 있게 합니다.
'''
class BankAccount:
    #BankAccount라는 클래스(설계도) 를 정의합니다.
    #이 안에 계좌가 가져야 할 데이터(속성) 와 행동(메서드) 를 넣을것임.
    def __init__(self, owner, balance=0):
        #생성자입니다. 새로운 계좌 객체를 만들 때 자동으로 딱 한 번 호출됩니다.
        #매개변수
        #self: 지금 막 만들어지는 그 객체 자신을 가리키는 이름입니다. (다른 언어의 this와 유사)
        #owner: 계좌 주인의 이름(또는 식별 값)
        # balance=0: 초기 잔액. 값을 안 주면 기본값 0을 사용합니다.

        self.owner = owner
        self.balance = balance
        #인스턴스 변수(객체 개별 데이터) 설정입니다.
        #왼쪽의 self.owner, self.balance가 객체에 저장되는 실제 칸이고,
        # 오른쪽 owner, balance는 생성자에 들어온 전달값이에요.
        #ex ) self.owner ← "김철수"

    def deposit(self, amount): #입금 메서드 생성
        #입금 메서드. 호출 시 amount만큼 잔액을 늘립니다.
        self.balance += amount
        #현재 잔액(self.balance)에 입금액을 더해서 다시 저장합니다.
        print(f"{self.owner}님 의 계좌로 {amount}원 입금하였습니다. 현재 잔액: {self.balance}원")

    def withdraw(self, amount):
        #출금 메서드. amount만큼 뺄 수 있는지(잔액이 충분한지) 확인합니다.
        if self.balance >= amount:
            #잔액이 출금 메서드를 호출해 입력받은 금액보다 크다면
            self.balance -= amount
            #잔액에서 입력받은 값을 뺀 후
            print(f"{self.owner}님 의 계좌에서 {amount}원 출금하였습니다. 현재 잔액: {self.balance}원")
            #얼마가 출금되었는지 작성해준 후 현재 남은 잔액도 출력해줌
        else:
            # 잔액보다 입력받은 출금하려는 수가 크다면
            print("잔액 부족!")
            # “잔액 부족!” 을 출력합니다.

    def check_balance(self):
        print(f"{self.owner}님 의 계좌 현재 잔액: {self.balance}원")
        #잔액 확인 메서드. 현재 잔액을 출력만 합니다.

bank1 = BankAccount("김철수", 1000)
bank1.check_balance()
bank1.deposit(500)
bank1.withdraw(300)
print()
bank1 = BankAccount("모은지", 5000)
bank1.check_balance()
bank1.deposit(15000)
bank1.withdraw(300)



class Person:
    def __init__(self):
        print("생성자가 호출됨!")

p = Person()  # 객체가 만들어지면서 자동으로 __init__ 실행
# p


class Person2:
    def say_hello(self):
        print("안녕하세요!")

p2 = Person2()        # 객체 생성 (생성자 자동 호출)
p2.say_hello()       # 메서드 직접 호출