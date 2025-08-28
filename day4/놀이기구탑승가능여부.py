height = int(input("키를 입력하세요 (cm): "))  # 숫자로 변환
age = int(input("나이를 입력하세요: "))       # 숫자로 변환


# 탑승 가능 여부 확인
can_ride = height >= 120 and age >= 10 # 키가120 이상, 나이가 10살 이상이어야 함
print("놀이기구를 탈 수 있나요?", can_ride)
