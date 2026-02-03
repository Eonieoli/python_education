"""
Day 3 - Boolean과 비교/논리 연산자 Practice
강사와 함께 실습하기

실습 목표:
1. 나이 비교로 성인 판단하기
2. 로그인 검증 (아이디 AND 비밀번호)
3. 점수 범위 체크 (0~100)

"""

# ============================================================
# Practice 1: 나이 비교 (성인인지 확인)
# ============================================================

print("=" * 60)
print("Practice 1: 성인 판단")
print("=" * 60)

# 한국 기준 만 19세 이상이 성인

# TODO: age 변수에 25 할당
age = 25

# TODO: age가 19 이상인지 비교해서 is_adult에 저장
is_adult = age >= 19

print(f"나이: {age}")
print(f"성인인가? {is_adult}")  # True


# 미성년자 케이스
# TODO: age를 17로 변경
age = 17

# TODO: age가 19 이상인지 비교해서 is_adult에 저장
is_adult = age >= 19

print(f"\n나이: {age}")
print(f"성인인가? {is_adult}")  # False


# 경계값 테스트 (정확히 19세)
# TODO: age를 19로 변경
age = 19

# TODO: age가 19 이상인지 비교
is_adult = age >= 19

print(f"\n나이: {age}")
print(f"성인인가? {is_adult}")  # True

print()


# ============================================================
# Practice 2: 로그인 검증 (아이디 AND 비밀번호)
# ============================================================

print("=" * 60)
print("Practice 2: 로그인 검증")
print("=" * 60)

# 저장된 올바른 정보
correct_id = "admin"
correct_password = "python123"

# 케이스 1: 모두 맞는 경우
input_id = "admin"
input_password = "python123"

# TODO: 아이디와 비밀번호가 모두 맞는지 확인
# (input_id가 correct_id와 같고) AND (input_password가 correct_password와 같음)
login_success = (input_id == correct_id) and (input_password == correct_password)

print(f"입력 아이디: {input_id}")
print(f"입력 비밀번호: {input_password}")
print(f"로그인 성공? {login_success}")  # True


# 케이스 2: 아이디만 틀린 경우
input_id = "user"
input_password = "python123"

# TODO: 로그인 성공 여부 확인
login_success = (input_id == correct_id) and (input_password == correct_password)

print(f"\n입력 아이디: {input_id}")
print(f"입력 비밀번호: {input_password}")
print(f"로그인 성공? {login_success}")  # False


# 케이스 3: 비밀번호만 틀린 경우
input_id = "admin"
input_password = "wrong"

# TODO: 로그인 성공 여부 확인
login_success = (input_id == correct_id) and (input_password == correct_password)

print(f"\n입력 아이디: {input_id}")
print(f"입력 비밀번호: {input_password}")
print(f"로그인 성공? {login_success}")  # False


# 케이스 4: 둘 다 틀린 경우
input_id = "hacker"
input_password = "1234"

# TODO: 로그인 성공 여부 확인
login_success = (input_id == correct_id) and (input_password == correct_password)

print(f"\n입력 아이디: {input_id}")
print(f"입력 비밀번호: {input_password}")
print(f"로그인 성공? {login_success}")  # False

print()


# ============================================================
# Practice 3: 범위 체크 (0 <= 점수 <= 100)
# ============================================================

print("=" * 60)
print("Practice 3: 점수 범위 검증")
print("=" * 60)

# 점수는 0에서 100 사이여야 유효함

# 케이스 1: 정상 점수
score = 85

# TODO: score가 0 이상 100 이하인지 확인
# 방법 1: (score >= 0) and (score <= 100)
# 방법 2: 0 <= score <= 100 (Python 특징!)
is_valid = 0 <= score <= 100

print(f"점수: {score}")
print(f"유효한 점수? {is_valid}")  # True


# 케이스 2: 음수 점수
score = -10

# TODO: 점수 유효성 확인
is_valid = 0 <= score <= 100

print(f"\n점수: {score}")
print(f"유효한 점수? {is_valid}")  # False


# 케이스 3: 100점 초과
score = 150

# TODO: 점수 유효성 확인
is_valid = 0 <= score <= 100

print(f"\n점수: {score}")
print(f"유효한 점수? {is_valid}")  # False


# 케이스 4: 경계값 (0점)
score = 0

# TODO: 점수 유효성 확인
is_valid = 0 <= score <= 100

print(f"\n점수: {score}")
print(f"유효한 점수? {is_valid}")  # True


# 케이스 5: 경계값 (100점)
score = 100

# TODO: 점수 유효성 확인
is_valid = 0 <= score <= 100

print(f"\n점수: {score}")
print(f"유효한 점수? {is_valid}")  # True

print()


# ============================================================
# 보너스: 성적 등급 판정 (범위 + 조건 조합)
# ============================================================

print("=" * 60)
print("보너스: 성적 등급 판정")
print("=" * 60)

score = 85

# TODO: 점수 범위별 등급 판정
# A: 90점 이상
# B: 80점 이상 90점 미만
# C: 70점 이상 80점 미만
# 나머지: 재시험

is_A = score >= 90
is_B = (score >= 80) and (score < 90)
is_C = (score >= 70) and (score < 80)

print(f"점수: {score}")
print(f"A등급? {is_A}")  # False
print(f"B등급? {is_B}")  # True
print(f"C등급? {is_C}")  # False


# 다른 점수로 테스트
score = 95

is_A = score >= 90
is_B = (score >= 80) and (score < 90)
is_C = (score >= 70) and (score < 80)

print(f"\n점수: {score}")
print(f"A등급? {is_A}")  # True
print(f"B등급? {is_B}")  # False
print(f"C등급? {is_C}")  # False

print()


print("=" * 60)
print("Practice 완료!")
print("=" * 60)
print("실습한 내용:")
print("1. 성인 판단 (age >= 19)")
print("2. 로그인 검증 (id and password)")
print("3. 범위 체크 (0 <= score <= 100)")
print("4. 보너스: 성적 등급 판정")
print("=" * 60)
