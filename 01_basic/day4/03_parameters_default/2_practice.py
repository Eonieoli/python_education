# 2_practice.py

"""
Day 4 - 3교시: 매개변수 - 위치와 기본값
Practice (강사와 함께 실습)

학습 목표:
- 기본값을 활용한 인사 함수 작성
- 프로필 출력 함수 만들기
"""

# ============================================
# 실습 1: 인사 함수 (기본값 활용) - 처음부터 끝까지
# ============================================

# 기본값을 사용하는 인사 함수를 만들어봅시다
def welcome_message(name, language="Korean"):
    """
    다국어 환영 메시지
    - name: 사용자 이름
    - language: 언어 설정 (기본값: "Korean")
    """
    if language == "Korean":
        return f"환영합니다, {name}님!"
    elif language == "English":
        return f"Welcome, {name}!"
    else:
        return f"Hello, {name}!"

# 기본값 사용 (Korean)
msg1 = welcome_message("김철수")
print(msg1)  # 출력: 환영합니다, 김철수님!

# 영어로 변경
msg2 = welcome_message("John", "English")
print(msg2)  # 출력: Welcome, John!


# ============================================
# 실습 2: 프로필 출력 함수 (TODO)
# ============================================

# TODO: 학생 프로필을 출력하는 함수를 작성하세요
# 힌트: name, age는 필수, major(전공)는 "미정"을 기본값으로
def print_student_profile(name, age, major="미정"):
    return f"이름: {name}, 나이: {age}, 전공: {major}"

# 테스트
profile1 = print_student_profile("박민수", 20)
print(profile1)  # 출력: 이름: 박민수, 나이: 20, 전공: 미정

profile2 = print_student_profile("이영희", 22, "컴퓨터공학")
print(profile2)  # 출력: 이름: 이영희, 나이: 22, 전공: 컴퓨터공학


# ============================================
# 실습 3: 상품 정보 함수 (TODO)
# ============================================

# TODO: 상품 정보를 포맷팅하는 함수를 작성하세요
# 요구사항:
# - name: 상품명 (필수)
# - price: 가격 (필수)
# - stock: 재고 (기본값: 0)
# - category: 카테고리 (기본값: "기타")
def format_product_info(name, price, stock=0, category="기타"):
    return f"[{category}] {name} - {price}원 (재고: {stock}개)"

# 테스트
info1 = format_product_info("노트북", 1500000)
print(info1)  # 출력: [기타] 노트북 - 1500000원 (재고: 0개)

info2 = format_product_info("마우스", 30000, 50, "컴퓨터")
print(info2)  # 출력: [컴퓨터] 마우스 - 30000원 (재고: 50개)
