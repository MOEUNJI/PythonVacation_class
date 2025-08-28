# 1️⃣ 점수를 계산하는 함수
def calc_score(kor, eng, math):
    total = kor + eng + math
    #받아온 모든 값을 더한다.
    avg = total / 3
    #total을 3으로 나눈 값을 avg에 대입한다.
    #//을 사용하면 몫 나눗셈으로 변경됨
    return avg   # 평균 점수를 리턴

# 2️⃣ 평균 점수를 받아 학점을 매기는 함수
def get_grade(avg):
    #calc_score에서 받은 리턴값 avg를 매개변수로 받아 등급을 나눈다.
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


# 3️⃣ 프로그램 실행
# 학생 점수 입력
kor = int(input("국어 점수를 입력하세요: "))
eng = int(input("영어 점수를 입력하세요: "))
math = int(input("수학 점수를 입력하세요: "))

# 함수1 → 평균 구하기
average = calc_score(kor, eng, math)
#calc_score 함수를 호출하여 실행한 후 값을 입력받고 average에 리턴값을 대입한다.
#즉 에버리지는 리턴값을 가지고 있음

# 함수2 → 평균을 기준으로 학점 구하기
grade = get_grade(average)
#get_grade함수를 호출할건데 average가 가지고 있는 리턴값을 활용하여 매개변수로 넘겨줄것이다.
#get_grade 함수를 실행하고 나온 반환된 등급이 grade에 들어있음

# 최종 결과 출력
print(f"평균 점수: {average:.2f}")
#파이썬에서는 / 연산자를 쓰면 **항상 결과가 float(실수)**로 나옵니다
#// → 몫만 취하는 정수 나눗셈
# / → 항상 실수 나눗셈
print(f"최종 학점: {grade}")