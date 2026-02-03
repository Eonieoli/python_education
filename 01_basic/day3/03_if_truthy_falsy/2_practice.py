# 2_practice.py

"""
Day 3 - 3교시: 조건문 (if) + Truthy/Falsy
Practice (강사와 함께 실습)

학습 목표:
- 성적 등급 판정 (if/elif/else)
- 로그인 검증 (and, Truthy/Falsy)
- 빈 리스트 체크 (Truthy/Falsy 활용)
"""

# ============================================
# 실습 1: 성적 등급 (처음부터 끝까지 타이핑)
# ============================================

# 학생의 점수
score = 88

# if/elif/else로 등급 판정
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"점수: {score}점, 등급: {grade}")  # 출력: 점수: 88점, 등급: B


# ============================================
# 실습 2: 로그인 검증 (TODO)
# ============================================

# 저장된 사용자 정보
correct_username = "user123"
correct_password = "pass1234"

# 사용자가 입력한 정보
input_username = "user123"
input_password = "pass1234"

# TODO: if문으로 로그인 검증을 하세요
# 힌트: and 연산자 사용, 아이디와 비밀번호가 모두 일치해야 함
if input_username == correct_username and input_password == correct_password:
    print("로그인 성공!")  # 출력: 로그인 성공!
else:
    print("로그인 실패!")


# ============================================
# 실습 3: 빈 리스트 체크 (TODO)
# ============================================

# 장바구니 (비어있음)
shopping_cart = []

# TODO: Truthy/Falsy를 활용하여 장바구니가 비어있는지 확인하세요
# 힌트: if shopping_cart: 형태로 사용
if shopping_cart:
    print(f"장바구니에 {len(shopping_cart)}개의 상품이 있습니다")
else:
    print("장바구니가 비어있습니다")  # 출력: 장바구니가 비어있습니다

# 상품 추가 후 다시 확인
shopping_cart = ["노트북", "마우스", "키보드"]

# TODO: 다시 한 번 장바구니를 확인하세요
if shopping_cart:
    print(f"장바구니에 {len(shopping_cart)}개의 상품이 있습니다")
    # 출력: 장바구니에 3개의 상품이 있습니다
else:
    print("장바구니가 비어있습니다")
