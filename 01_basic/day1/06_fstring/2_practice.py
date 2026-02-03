# 2_practice.py

"""
Day 1 - 6교시: f-string
Practice (강사와 함께 실습)

학습 목표:
- 상품 정보를 f-string으로 출력하기
- 계산 결과를 포매팅하여 출력하기
- 사용자 정보를 조합하여 인사말 만들기
"""

# ============================================
# 실습 1: 상품 정보 출력하기
# ============================================

# 상품 정보 변수
product_name = "무선 이어폰"
product_price = 89000
product_stock = 15

# f-string으로 상품 정보 출력
print(f"상품명: {product_name}")
print(f"가격: {product_price:,}원")  # 천단위 콤마
print(f"재고: {product_stock}개")

# 재고 가치 계산 및 출력
total_value = product_price * product_stock
print(f"총 재고 가치: {total_value:,}원")

# 출력 예시:
# 상품명: 무선 이어폰
# 가격: 89,000원
# 재고: 15개
# 총 재고 가치: 1,335,000원


# ============================================
# 실습 2: 계산 결과 포매팅하기
# ============================================

# 거리와 시간 정보
distance_km = 42.195  # 마라톤 거리 (km)
time_hour = 3.5  # 완주 시간 (시간)

# 평균 속도 계산 (km/h)
average_speed = distance_km / time_hour

# 소수점 포매팅으로 출력
print(f"거리: {distance_km}km")
print(f"시간: {time_hour}시간")
print(f"평균 속도: {average_speed:.2f}km/h")  # 소수점 2자리

# 출력 예시:
# 거리: 42.195km
# 시간: 3.5시간
# 평균 속도: 12.06km/h


# ============================================
# 실습 3: 사용자 인사말 만들기
# ============================================

# 사용자 정보
user_name = "김민지"
user_age = 28
user_city = "서울"

# f-string으로 인사말 조합
greeting = f"안녕하세요, {user_city}에 사시는 {user_age}세 {user_name}님!"
print(greeting)

# 여러 줄로 출력
print(f"이름: {user_name}")
print(f"나이: {user_age}세")
print(f"거주지: {user_city}")
print(f"환영합니다, {user_name}님! 좋은 하루 되세요!")

# 출력 예시:
# 안녕하세요, 서울에 사시는 28세 김민지님!
# 이름: 김민지
# 나이: 28세
# 거주지: 서울
# 환영합니다, 김민지님! 좋은 하루 되세요!
