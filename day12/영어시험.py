def english_quiz(questions, answers, name):
    # 함수 정의: questions(문제 리스트), answers(정답 리스트), name(학생 이름)을 입력으로 받음

    score = 0
    # 점수 저장용 변수. 처음엔 0점에서 시작
    student_answers = []
    # 학생이 실제로 입력한 답을 모아둘 빈 리스트

    for i in range(len(questions)):  # 인덱스로 접근
        # range(3) -> 0,1,2 즉, 마지막 숫자 n은 포함되지 않습니다.
        #questions = ["사과","바나나","체리"]
        #range(len(questions)) = range(3) = 0, 1, 2
        #questions[0] → "사과"
        #questions[1] → "바나나"
        #questions[2] → "체리"

        ans = input(f"'{questions[i]}'의 영어 단어를 입력하세요: ")
        # i를 0부터 questions의 길이-1까지 증가시키며 반복
        # 예: questions가 3개면 i는 0,1,2가 됨
        student_answers.append(ans)
        # 방금 입력받은 학생 답안을 리스트에 저장

        if ans.lower() == answers[i].lower():
            # 소문자로 바꿔 비교 → 'Apple'과 'apple'을 같은 것으로 인정
            score += 10
            # 정답이면 10점 추가

    print(f"{name}의 점수는 {score}점 입니다.")
    print("입력한 답:", student_answers)
    # 모든 문제가 끝나면 최종 점수 출력

questions = ["사과", "바나나", "체리"]
# 출제용 한글 단어 리스트 (문제)
answers = ["apple", "banana", "cherry"]
# 정답(영어) 리스트. questions와 1:1로 순서가 맞아야 함

name = input("학생 이름을 입력하세요: ")
# 학생 이름 입력받기
english_quiz(questions, answers, name)
# 위에서 정의한 함수 실행(채점 시작)S
