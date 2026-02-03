# 2_practice.py

"""
Day 1 - 2교시: 변수와 숫자형
Practice (강사와 함께 실습)

학습 목표:
- 나이 계산하기
- 온도 변환하기
- type() 확인 실습
"""

# ============================================
# 실습 1: 나이 계산하기
# ============================================

# 현재 연도와 태어난 연도를 변수에 저장
current_year = 2026
birth_year = 1995

# 나이 계산
age = current_year - birth_year

# 결과 출력
print("태어난 연도:", birth_year)
print("현재 연도:", current_year)
print("나이:", age, "세")  # 출력: 나이: 31 세


# ============================================
# 실습 2: 온도 변환 (섭씨 → 화씨)
# ============================================

# 섭씨 온도
celsius = 25

# 화씨로 변환
# 공식: 화씨 = (섭씨 × 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

# 결과 출력
print("섭씨", celsius, "도")
print("화씨", fahrenheit, "도")  # 출력: 화씨 77.0 도


# ============================================
# 실습 3: type() 확인 실습
# ============================================

# 여러 변수의 타입 확인
name = "김철수"
age = 25
height = 175.5
is_student = True

# 각 변수의 타입 출력
print("이름:", name, "타입:", type(name))  # 출력: 이름: 김철수 타입: <class 'str'>
print("나이:", age, "타입:", type(age))  # 출력: 나이: 25 타입: <class 'int'>
print("키:", height, "타입:", type(height))  # 출력: 키: 175.5 타입: <class 'float'>
print("학생 여부:", is_student, "타입:", type(is_student))  # 출력: 학생 여부: True 타입: <class 'bool'>
