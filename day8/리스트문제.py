# [이름, 점수(문자열), 취미]
students = [
    ["kim",  "95",  "  Pizza "],
    ["lee",  "80",  "pasta"],
    ["park", "?",   "  Piano"],
    ["choi", "77",  "pancake"]
]

print("1) 변수를 만들어서 이름 첫 글자만 대문자로 보여주기")
for i in students:
    name = i[0].capitalize()
    print(name)
print()
#======================================================
print("2) 점수가 숫자인 학생들의 평균(정수) 구하기 (숫자가 아니면 제외)")
total = 0
count = 0
for i in students:
    score_str = i[1]
    if score_str.isdigit():
        total += int(score_str)
        count += 1
avg_int = total // count if count > 0 else 0
print("유효 인원:", count, "평균:", avg_int)
print()
#======================================================
print("3) 취미 공백 제거 + 소문자 통일해서 보여주기")
for i in students:
    hobby_clean = i[2].strip().lower()
    print(hobby_clean)
print()
#======================================================
print("4) 이름이 p 로 시작하는 사람만 (대소문자 무관)")
for i in students:
    if i[0].lower().startswith("p"):
        #.lower() : 이름을 소문자로 바꿈. ("PARK" → "park")
        #.startswith("p") : p로 시작하면 True.
        print(i[0].capitalize())
        # 조건이 참이면 print(s[0].capitalize()) : 원래 이름을 첫 글자만 대문자로 출력.
print()
#======================================================
print("5) 모든 이름에 들어 있는 'a' 글자 총 개수")
a_total = 0
for i in students:
    a_total += i[0].lower().count("a")
print("'a' 총개수:", a_total)
print()
#======================================================
print("6) join 없이 이름들을 한 줄 문자열로 만들기 (join 대신 간단히)")
names_line = ""
for i in students:
    cap = i[0].capitalize()
    if names_line == "":
        names_line = cap
    else:
        names_line = names_line + ", " + cap
print("이름 한 줄:", names_line)

#join을 사용한다면?
parts = []
for s in students:
    cap = s[0].capitalize()
    parts.append(cap)

names_line = ", ".join(parts)
print("이름 한 줄:", names_line)

