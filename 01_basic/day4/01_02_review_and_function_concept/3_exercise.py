# 3_exercise.py

"""
Day 4 - 2교시: 함수 기본
Exercise (혼자 풀어보기)

문제 1: 온도 변환 함수
문제 2: 인사말 함수
"""

# ============================================
# Exercise 1: 온도 변환 함수 만들기
# ============================================

"""
섭씨 온도를 화씨 온도로 변환하는 함수를 작성하세요.

요구사항:
1. 함수명: celsius_to_fahrenheit
2. 매개변수: celsius (섭씨 온도)
3. 반환값: 화씨 온도
4. 공식: 화씨 = (섭씨 × 9/5) + 32

테스트:
- celsius_to_fahrenheit(0) → 32.0
- celsius_to_fahrenheit(25) → 77.0
- celsius_to_fahrenheit(100) → 212.0
"""

# TODO: celsius_to_fahrenheit 함수를 작성하세요
# 힌트: def celsius_to_fahrenheit(celsius):


# 테스트 코드 (함수 작성 후 실행)
print(f"0도 = {celsius_to_fahrenheit(0)}도")  # 출력: 0도 = 32.0도
print(f"25도 = {celsius_to_fahrenheit(25)}도")  # 출력: 25도 = 77.0도
print(f"100도 = {celsius_to_fahrenheit(100)}도")  # 출력: 100도 = 212.0도


# ============================================
# Exercise 2: 인사말 함수 만들기 (여러 값 반환)
# ============================================

"""
이름과 나이를 받아서 인사말과 연령대를 함께 반환하는 함수를 작성하세요.

요구사항:
1. 함수명: greet_with_age_group
2. 매개변수: 
   - name (이름)
   - age (나이)
3. 반환값 (2개를 튜플로 반환):
   - greeting: f"안녕하세요, {name}님! {age}살이시군요."
   - age_group: 나이대 문자열
     - 0-12: "어린이"
     - 13-19: "청소년"
     - 20-59: "성인"
     - 60 이상: "어르신"

테스트:
- greet_with_age_group("김철수", 10)
  → ("안녕하세요, 김철수님! 10살이시군요.", "어린이")
- greet_with_age_group("이영희", 15)
  → ("안녕하세요, 이영희님! 15살이시군요.", "청소년")
"""

# TODO: greet_with_age_group 함수를 작성하세요
# 힌트 1: def greet_with_age_group(name, age):
# 힌트 2: if/elif로 연령대 판정
# 힌트 3: return greeting, age_group


# 테스트 코드 (함수 작성 후 실행)
msg, group = greet_with_age_group("김철수", 10)
print(msg)  # 출력: 안녕하세요, 김철수님! 10살이시군요.
print(f"연령대: {group}")  # 출력: 연령대: 어린이

msg, group = greet_with_age_group("이영희", 15)
print(msg)  # 출력: 안녕하세요, 이영희님! 15살이시군요.
print(f"연령대: {group}")  # 출력: 연령대: 청소년

msg, group = greet_with_age_group("박민수", 30)
print(msg)  # 출력: 안녕하세요, 박민수님! 30살이시군요.
print(f"연령대: {group}")  # 출력: 연령대: 성인

msg, group = greet_with_age_group("최할머니", 65)
print(msg)  # 출력: 안녕하세요, 최할머니님! 65살이시군요.
print(f"연령대: {group}")  # 출력: 연령대: 어르신
