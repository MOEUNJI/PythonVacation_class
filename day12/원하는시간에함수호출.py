import time

def timer(second,callback): #타이머 역할
   # second: 몇 초 동안 기다릴지를 지정하는 숫자.
   # callback: 기다린 후에 실행할 함수를 콜백으로 받음.
   print("타이머 시작")
   print(f"{second}초 뒤에 요청한 함수를 호출합니다.")

   time.sleep(second)#매개변수값
   # time.sleep(second) : 프로그램을 second만큼 멈춰서 기다리게 함
   # time.sleep(5) → 5초 동안 아무 작업도 하지 않고 기다림.
   #sleep : time모듈에 포함되어있는 함수 ( 프로그램을 일정 시간 동안 멈추게(일시 정지) 하는 함수 )
   callback()
   # second에 입력한 초를 기다린 후 전달받은 함수를 실행해요.
   print("타이머 종료")

def callback():
   #타이머가 끝난 후 실행할 작업
   print("5초 뒤 실행될 함수입니다.")
   
timer(5,callback)
#second = 5 → 5초 동안 기다림.
#callback = callback() → 기다린 후에 callback() 함수를 실행.
