'''
이 코드는 나이와 학생 여부에 따라 티켓 가격을 계산하는 프로그램입니다.


나이가 20대이고, 학생이라면 성인 요금에 10% 할인된 가격을 적용합니다.
나이가 20대인데 학생이 아니라면 가격 할인이 없다.
나이가 20세 미만이라면 어린이 요금을 적용합니다.
'''
# 나이 입력
age = int(input("나이를 입력해주세요: "))


# 1. True : 참 : 1
# 2. False : 거짓 : 0
# 학생 여부: 20세 미만이면 무조건 False, 아니면 입력받아서 True/False 변환
student = False if (age < 20 or age >= 30) else bool(int(input("학생인가요? (1: 예, 0: 아니오): ")))

# 요금 설정
adult_price = 10000
child_price = 6000

# 할인 조건: 나이가 20세 이상 30세 미만이고 학생인 경우만 할인
discount = (20 <= age < 30) and student

# 기본 요금: 20세 이상이면 성인 요금, 아니ㅁ면 어린이 요금
basic_price = adult_price if age >= 20 else child_price

# 최종 요금 계산
result = basic_price * 0.9 if discount else basic_price

# 결과 출력
print("최종 티켓 가격은", int(result), "원 입니다.")




