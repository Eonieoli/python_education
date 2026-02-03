# 2_practice.py

"""
Day 1 - 7교시: 입출력 + 형변환
Practice (강사와 함께 실습)

학습 목표:
- 나이 입력받아 계산하기
- BMI 계산기 만들기
- 두 숫자 덧셈 프로그램
"""

# ============================================
# 실습 1: 나이 입력받아 계산하기
# ============================================

# 태어난 연도를 입력받습니다
print("=== 나이 계산 프로그램 ===")
birth_year_str = input("태어난 연도를 입력하세요: ")

# 문자열을 정수로 변환
birth_year = int(birth_year_str)

# 현재 연도 설정
current_year = 2026

# 나이 계산
age = current_year - birth_year

# 결과 출력
print(f"현재 연도: {current_year}년")
print(f"태어난 연도: {birth_year}년")
print(f"당신은 {age}세입니다.")


# ============================================
# 실습 2: BMI 계산기
# ============================================

# BMI(체질량지수) = 몸무게(kg) / (키(m) × 키(m))
print("\n=== BMI 계산기 ===")

# 키와 몸무게를 입력받습니다
height_cm_str = input("키를 입력하세요 (cm): ")
weight_str = input("몸무게를 입력하세요 (kg): ")

# 문자열을 숫자로 변환
height_cm = float(height_cm_str)  # 소수점 가능하므로 float
weight = float(weight_str)

# 키를 미터로 변환
height_m = height_cm / 100

# BMI 계산
bmi = weight / (height_m * height_m)

# 결과 출력
print(f"키: {height_cm}cm")
print(f"몸무게: {weight}kg")
print(f"BMI: {bmi:.1f}")  # 소수점 1자리까지


# ============================================
# 실습 3: 두 숫자 덧셈
# ============================================

print("\n=== 두 숫자 더하기 ===")

# 첫 번째 숫자 입력받기
first_num_str = input("첫 번째 숫자를 입력하세요: ")
first_num = int(first_num_str)

# 두 번째 숫자 입력받기
second_num_str = input("두 번째 숫자를 입력하세요: ")
second_num = int(second_num_str)

# 덧셈 계산
result = first_num + second_num

# 결과 출력
print(f"{first_num} + {second_num} = {result}")
