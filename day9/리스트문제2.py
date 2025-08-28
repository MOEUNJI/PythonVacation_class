# 원본 문자열 데이터
raw = [
    " kim , python , 95 ",
    " lee, Java , 82 ",
    "park , python , 100",
    "choi, c , 77 ",
    " jang , python , 89 ",
]

students = []  # [이름, 과목, 점수]

# 전처리
for line in raw:
    parts = line.split(",")
    clean_parts = []
    for p in parts:
        clean_parts.append(p.strip())

    name = clean_parts[0]
    lang = clean_parts[1]
    score_str = clean_parts[2]

    name = name.capitalize()
    lang = lang.upper()

    # 점수는 숫자라고 가정(필요하면 isdigit 체크 추가 가능)
    score = int(score_str)

    students.append([name, lang, score])

# 전체 인원 수
total = len(students)

# PYTHON 수강자 수
python_count = 0
for i in students:
    if i[1] == "PYTHON":
        python_count += 1

# PYTHON 수강자 이름 리스트
py_names = []
for i in students:
    if i[1] == "PYTHON":
        py_names.append(i[0])

# 전체 점수 리스트
all_scores = []
for i in students:
    all_scores.append(i[2])

# PYTHON 점수 리스트
py_scores = []
for i in students:
    if i[1] == "PYTHON":
        py_scores.append(i[2])

# === 평균(함수 없이, round 없이 1자리 버림) ===
# 전체 평균
if len(all_scores) > 0:
    overall_avg = (sum(all_scores) * 10) // len(all_scores) / 10
else:
    overall_avg = 0.0

# PYTHON 평균
if len(py_scores) > 0:
    py_avg = (sum(py_scores) * 10) // len(py_scores) / 10
else:
    py_avg = 0.0

# 이름에서 'a' 총 개수
a_total = 0
for i in students:
    a_total += i[0].lower().count("a")

# 이름이 'J'로 시작
j_list = []
for i in students:
    if i[0].startswith("J"):
        j_list.append(i[0])

# 출력
print("전체 인원:", total)
print("PYTHON 인원:", python_count)
print("PYTHON 수강자:", ", ".join(py_names))
print("전체 평균:", overall_avg)   # 예: 88.6 (버림)
print("PYTHON 평균:", py_avg)      # 예: 94.6 (버림)
print("'a' 총개수:", a_total)
print("이름 J 시작:", j_list)
