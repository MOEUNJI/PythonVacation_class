import time

print(time.time())       # 1970년 1월 1일부터 지금까지 초 단위 (Timestamp)
print(time.ctime())

print("3초 대기 시작")
time.sleep(3)  # 3초 동안 멈춤
print("3초 후 출력됨")