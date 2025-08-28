class FileHandler:
   def __init__(self,filename):
       # 클래스의 설계도를 사용할 때 자동으로 실행되는 부분이다.
       #filename : 어떤 파일을 오픈할지 알려주는 매개변수
       self.file = open(filename,'w')
       # 매개변수로 받은 파일을 열고 쓰기모드로 내용을 쓸 준비를 한다.
       print(f"{filename} 파일을 열었습니다.")
       #출력메시지 : 파일이 정상적으로 열렸음을 확인하기


   def write_data(self,data):
       # 매개변수 data에 파일에 쓸 내용을 전달받을것임
       self.file.write(data)
       # 전달받은 내용을 파일에 작성한다.
       #파일은 __init__() 함수로 가장 먼저 실행되어 열려있다.


   def __del__(self):
       self.file.close()
       print("파일을 닫았습니다.")


handler = FileHandler("text.txt")
handler.write_data("hellowwwwww python")
del handler
