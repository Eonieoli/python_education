# 3_exercise_solution.py

"""
Day 1 - 2교시: 변수와 숫자형
Exercise - 쇼핑몰 가격 계산 & BMI 계산기 (정답)
"""

# ============================================
# 문제 1: 쇼핑몰 가격 계산 (정답)
# ============================================

# 주어진 데이터
tshirt_price = 29000
tshirt_quantity = 2
jeans_price = 59000
jeans_quantity = 1
discount_rate = 0.1


# 정답 코드

# 1. 각 상품의 소계
tshirt_subtotal = tshirt_price * tshirt_quantity  # 58000
jeans_subtotal = jeans_price * jeans_quantity  # 59000

# 2. 전체 합계
total = tshirt_subtotal + jeans_subtotal  # 117000

# 3. 할인 금액
discounted_total = total * (1 - discount_rate)  # 105300.0

# 결과 출력
print("티셔츠 소계:", tshirt_subtotal, "원")
print("청바지 소계:", jeans_subtotal, "원")
print("전체 합계:", total, "원")
print("할인 후:", discounted_total, "원")


# ============================================
# 문제 2: BMI 계산기 (정답)
# ============================================

# 주어진 데이터
height_cm = 175
weight = 70


# 정답 코드

# 1. 키를 미터로 변환
height_m = height_cm / 100  # 1.75

# 2. BMI 계산
bmi = weight / (height_m * height_m)  # 22.857142857142858

# 결과 출력
print("키:", height_cm, "cm, 몸무게:", weight, "kg")
print("키(미터):", height_m, "m")
print("BMI:", bmi)
