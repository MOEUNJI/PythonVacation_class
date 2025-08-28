#raise 에외클래스(예외메시지)
try:
   age = int(input("나이를 입력하세요 : "))


   #입력값이 0보다 작거나 200보다 크다면
   if(age < 0 or age > 150):
       raise Exception("나이는 0 이상 150 이하로 작성하세요")#예외를 발생시킨다.


except Exception as e:
   print(e) #변수에는 작성한 "나이는~ 입력하세요" 메시지가 대입됨
else:
   print(f"당신은 {age}살 이군요!")
finally: #프로그램이 종료되면 종료메시지를 출력
   print("프로그램을 종료합니다.")