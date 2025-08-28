import time

start_time = time.time()          # 시작 시간 기록
end_time = start_time + 20 * 60   # 20분 뒤 시간 계산

while True:
    now = time.time()             # 현재 시간
    elapsed_minutes = int((now - start_time) // 60)  # 지난 시간(분) 계산

    print(f"{elapsed_minutes}분 경과")  # 경과 시간 출력
    time.sleep(60)                 # 1분 쉬고 다음 반복

    if now >= end_time:           # 20분 이상이면 종료
        break

print("20분이 지났습니다!")
