# 3_exercise_solution.py

"""
Day 4 - 2교시: 함수 기본
Exercise 정답
"""

# ============================================
# Exercise 1 정답: 온도 변환 함수
# ============================================

def celsius_to_fahrenheit(celsius):
    """섭씨를 화씨로 변환"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# 테스트
print(f"0도 = {celsius_to_fahrenheit(0)}도")  # 출력: 0도 = 32.0도
print(f"25도 = {celsius_to_fahrenheit(25)}도")  # 출력: 25도 = 77.0도
print(f"100도 = {celsius_to_fahrenheit(100)}도")  # 출력: 100도 = 212.0도


# ============================================
# Exercise 2 정답: 인사말 함수
# ============================================

def greet_with_age_group(name, age):
    """이름과 나이를 받아서 인사말과 연령대를 반환"""
    # 인사말 생성
    greeting = f"안녕하세요, {name}님! {age}살이시군요."
    
    # 연령대 판정
    if age <= 12:
        age_group = "어린이"
    elif age <= 19:
        age_group = "청소년"
    elif age <= 59:
        age_group = "성인"
    else:
        age_group = "어르신"
    
    # 두 개를 튜플로 반환
    return greeting, age_group

# 테스트
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
